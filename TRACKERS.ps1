$name = "4"

$LongName = "merelaager-$name"
$ShortName = "$name"

meshtastic --set-owner "$LongName" --set-owner-short "$ShortName" `
  --set device.role TRACKER `
  --set lora.region EU_868 `
  --set lora.modem_preset SHORT_FAST `
  --set lora.override_duty_cycle true `
  --set lora.config_ok_to_mqtt true `
  --set position.gps_mode ENABLED `
  --set position.gps_update_interval 15 `
  --set position.position_broadcast_secs 900 `
  --set position.position_broadcast_smart_enabled true `
  --set position.broadcast_smart_minimum_distance 30 `
  --set position.broadcast_smart_minimum_interval_secs 15 `
  --set telemetry.environment_measurement_enabled true `
  --set telemetry.environment_screen_enabled true `
  --set telemetry.environment_update_interval 300 `
  --ch-index 0 `
  --ch-set name "Merelaager" `
  --ch-set psk "base64:puavdd7vtYJh8NUVWgxbsoG2u9Sdqc54YvMLs+KNcMA=" `
  --ch-set module_settings.position_precision 32 `
  --pos-fields TIMESTAMP HEADING SPEED
