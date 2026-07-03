# GPS Trackers

## Example data packets (MQTT Explorer):
The data can be subscribed on MQTT open servers:
```
Server: mqtt.meshtastic.org
Protocol: mqtt://
Port: 1883
Username: meshdev
Password: large4cats
Topic: msh/EU_868/merelaager/#
```

```
{"channel":0,"from":1201545706,"hop_start":2,"hops_away":0,"id":3702202712,"payload":{"barometric_pressure":1010.40435791016,"relative_humidity":36.5791015625,"temperature":34.5},"rssi":-26,"sender":"!0fd8badc","snr":10,"timestamp":1782654887,"to":4294967295,"type":"telemetry"}
```

```
{"channel":0,"from":1201545706,"hop_start":2,"hops_away":0,"id":2215193927,"payload":{"ground_track":18212000,"latitude_i":589260443,"longitude_i":248635653,"precision_bits":32,"time":1782654734,"timestamp":1782654724},"rssi":-27,"sender":"!0fd8badc","snr":9.75,"timestamp":1782654737,"to":4294967295,"type":"position"}
```

```
{"channel":0,"from":1201545706,"hop_start":2,"hops_away":0,"id":3436437898,"payload":{"ground_speed":4,"ground_track":3993000,"latitude_i":589257621,"longitude_i":248633915,"precision_bits":32,"time":1782655471,"timestamp":1782655471},"rssi":-55,"sender":"!0fd8badc","snr":9.75,"timestamp":1782655474,"to":4294967295,"type":"position"}
```
