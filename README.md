# GPS Trackers

## T-BEAM Receiver Configuration
```
$name = "0"

$LongName = "merelaager-receiver"
$ShortName = "$name"

meshtastic --set-owner "$LongName" --set-owner-short "$ShortName" `
  --set device.role CLIENT_MUTE `
  --set lora.region EU_868 `
  --set lora.modem_preset SHORT_FAST `
  --set position.position_broadcast_secs 1800 `
  --set position.position_broadcast_smart_enabled false `
  --set network.wifi_enabled true `
  --set network.wifi_ssid "Merelaager" `
  --set network.wifi_psk "Merelaager.123" `
  --set mqtt.enabled true `
  --set mqtt.address "mqtt.meshtastic.org" `
  --set mqtt.root "msh/EU_868/merelaager" `
  --set mqtt.tls_enabled false `
  --set mqtt.json_enabled true `
  --ch-index 0 `
  --ch-set name "MerelaagerSailboats" `
  --ch-set psk "base64:puavdd7vtYJh8NUVWgxbsoG2u9Sdqc54YvMLs+KNcMA=" `
  --ch-set module_settings.position_precision 32 `
  --ch-set uplink_enabled true `
  --ch-set downlink_enabled false
```

## T-ECHO Tracker Configuration (4 of these)
```
$name = "1"

$LongName = "merelaager-$name"
$ShortName = "$name"

meshtastic --set-owner "$LongName" --set-owner-short "$ShortName" `
  --set device.role TRACKER `
  --set lora.region EU_868 `
  --set lora.modem_preset SHORT_FAST `
  --set lora.override_duty_cycle true `
  --set lora.config_ok_to_mqtt true `
  --set position.gps_mode ENABLED `
  --set position.position_broadcast_secs 60 `
  --set position.position_broadcast_smart_enabled true `
  --set position.broadcast_smart_minimum_interval_secs 10 `
  --set position.broadcast_smart_minimum_distance 5 `
  --set telemetry.environment_measurement_enabled true `
  --set telemetry.environment_screen_enabled true `
  --set telemetry.environment_update_interval 300 `
  --ch-index 0 `
  --ch-set name "MerelaagerSailboats" `
  --ch-set psk "base64:puavdd7vtYJh8NUVWgxbsoG2u9Sdqc54YvMLs+KNcMA=" `
  --ch-set module_settings.position_precision 32
```
