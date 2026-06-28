import json
from datetime import datetime, timezone
import paho.mqtt.client as mqtt

BOATS = {
    0x479e21ea: "QUBA1",
    0x0fd8badc: "Receiver",
}

def fmt_time(ts):
    if not ts:
        return "??:??:??"
    return datetime.fromtimestamp(ts).strftime("%H:%M:%S")

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe("msh/EU_868/merelaager/2/json/Merelaager/#")

def on_message(client, userdata, message):
    try:
        packet = json.loads(message.payload.decode())
        node_id = packet["from"]
        name = BOATS.get(node_id, f"!{node_id:08x}")
        ptype = packet.get("type")

        if ptype == "position":
            pos = packet["payload"]
            time_str = fmt_time(pos.get("time") or packet.get("timestamp"))
            lat = pos["latitude_i"] / 1e7
            lon = pos["longitude_i"] / 1e7
            extras = ""
            speed = pos.get("ground_speed")
            heading = pos.get("ground_track")
            if speed is not None:
                knots = speed * 1.944
                if knots >= 0.5:
                    extras += f"  {knots:.1f} kn"
            if heading is not None and 0 <= heading <= 359:
                extras += f"  {heading}°"
            print(f"[{time_str}] ⛵ {name}: {lat}, {lon}{extras}")

        elif ptype == "telemetry":
            time_str = fmt_time(packet.get("timestamp"))
            env = packet["payload"].get("environment_metrics", {})
            if env:
                temp = env.get("temperature")
                hum = env.get("relative_humidity")
                pres = env.get("barometric_pressure")
                print(f"[{time_str}] 🌡 {name}: {temp}°C  {hum}%  {pres} hPa")

    except Exception as e:
        print(f"Error: {e}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("meshdev", "large4cats")
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.meshtastic.org", 1883)
print("Waiting for data..")
client.loop_forever()
