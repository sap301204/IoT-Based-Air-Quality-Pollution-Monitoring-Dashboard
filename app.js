const client = mqtt.connect('wss://broker.hivemq.com:8884/mqtt');

client.on('connect', () => {
  console.log('Connected to MQTT WebSocket');
  client.subscribe('airquality/data');
});

client.on('message', (topic, message) => {
  const data = JSON.parse(message.toString());
  document.getElementById("temp").innerText = data.temperature + " °C";
  document.getElementById("hum").innerText = data.humidity + " %";
  document.getElementById("pm").innerText = data.pm25 + " µg/m³";
  document.getElementById("co2").innerText = data.air_quality;
});