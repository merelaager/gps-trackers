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
