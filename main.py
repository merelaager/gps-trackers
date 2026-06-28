import json, time
from datetime import datetime
import paho.mqtt.client as mqtt

BOATS = {
    0x479e21ea: "QUBA1",
    0x0fd8badc: "Receiver",
}

def on_connect(client, userdata, flags, rc, props):
    client.subscribe("msh/EU_868/merelaager/2/json/#")
    print("Connected")

def on_message(client, userdata, msg):
    try:
        p = json.loads(msg.payload)
        name = BOATS.get(p["from"], f"!{p['from']:08x}")
        pay = p.get("payload", {})
        ts = datetime.fromtimestamp(pay.get("time") or p.get("timestamp", time.time())).strftime("%H:%M:%S")

        if p.get("type") == "position":
            lat = pay["latitude_i"] / 1e7
            lon = pay["longitude_i"] / 1e7
            spd = pay.get("ground_speed", 0) * 1.944
            hdg = pay.get("ground_track", 0) / 1e6
            print(f"[{ts}] ⛵ {name}: {lat:.6f}, {lon:.6f} speed={spd:.1f} kn, heading={hdg:.1f}°")

        elif p.get("type") == "telemetry":
            temp = pay.get("temperature")
            hum  = pay.get("relative_humidity")
            pres = pay.get("barometric_pressure")
            if temp is not None:
                print(f"[{ts}] 🌡  {name}: {temp:.1f}°C  {hum:.0f}%  {pres:.1f} hPa")

    except Exception as e:
        print(f"Error: {e}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, clean_session=True)
client.username_pw_set("meshdev", "large4cats")
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.meshtastic.org", 1883)
client.loop_forever()
