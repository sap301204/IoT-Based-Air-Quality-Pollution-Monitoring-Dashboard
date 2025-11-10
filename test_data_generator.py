import time, json, random
while True:
    data = {
        'device_id': 'AQM001',
        'co2': random.randint(300, 800),
        'pm25': random.randint(10, 150),
        'temp': random.uniform(20, 35),
        'humidity': random.uniform(30, 70)
    }
    print(json.dumps(data))
    time.sleep(2)