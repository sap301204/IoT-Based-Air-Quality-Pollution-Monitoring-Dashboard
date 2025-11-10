# 🌍 IoT-Based Air Quality & Pollution Monitoring Dashboard

A complete IoT system that monitors air quality parameters (CO₂, PM2.5, temperature, humidity) in real time using **ESP32** and visualizes data on an **MQTT Web Dashboard**.

## ⚙️ Features
- Real-time sensor telemetry via MQTT  
- Web-based dashboard (HTML + JS + WebSocket MQTT)  
- Configurable thresholds and alerts  
- Works with local or public MQTT brokers  

## 🧰 Tech Stack
- **Hardware:** ESP32, MQ135, PMS5003, DHT22  
- **Protocols:** MQTT, WiFi  
- **Cloud/Dashboard:** HiveMQ, HTML/CSS/JS  

## 🚀 Quick Start
```bash
# Firmware upload
arduino-cli upload -p COM3 --fqbn esp32:esp32:esp32 firmware/main.ino

# Start local dashboard
cd web-ui
python -m http.server 8000
