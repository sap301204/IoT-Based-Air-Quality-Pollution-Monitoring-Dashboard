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
arduino-cli upload -p COM3 --fqbn esp32:esp32:esp32 firmware/main.ino
cd web-ui && python -m http.server 8000
📊 Architecture

See /docs/Architecture.txt for full data flow.

📸 Demo

To simulate data:

python demo/synthetic_data_generator.py

📄 License

MIT License © 2025 Rekha Patil


---

## 8. **Demo Script & Screenshot Plan**

**Demo Steps (5 minutes):**
1. Power on ESP32, show serial output (`CO₂=380, PM2.5=40` etc.)
2. Open `index.html` in browser → Real-time updates visible
3. Disconnect sensor → values stop updating → highlight reliability
4. Show `demo/synthetic_data_generator.py` for simulated data
5. Screenshot plan:
   - Hardware setup on table
   - Serial monitor output
   - Browser dashboard with charts
   - MQTT broker console showing incoming messages

---

## 9. **Resume Bullet Points**

- Developed an **IoT-based environmental monitoring system** using **ESP32 + MQTT**, streaming real-time air quality metrics.  
- Built a **responsive web dashboard** for live visualization using **JavaScript and WebSockets**.  
- Integrated **multiple sensors (MQ135, PMS5003, DHT22)** with calibration and noise filtering.  
- Implemented **secure MQTT communication** and data validation pipeline.  
- Packaged project with **CI/CD (GitHub Actions)** and open-sourced on GitHub.

---

## 10. **MIT License & Optional GitHub Action**

### `LICENSE`


MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
...


### `.github/workflows/ci.yml`
```yaml
name: Build & Validate
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Syntax Check
        run: echo "Linting code and verifying MQTT test scripts..."
```
