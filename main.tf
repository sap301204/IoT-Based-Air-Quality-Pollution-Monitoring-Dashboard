resource "aws_iot_thing" "device" {
  name = "AirQualityDevice"
}
resource "aws_dynamodb_table" "telemetry" {
  name           = "AirQualityData"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "device_id"
  attribute {
    name = "device_id"
    type = "S"
  }
}