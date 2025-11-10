import random, time, json

while True:
    data = {
        "temperature": round(random.uniform(25, 32), 2),
        "humidity": round(random.uniform(40, 60), 2),
        "air_quality": random.randint(300, 600),
        "pm25": random.randint(10, 150)
    }
    print(json.dumps(data))
    time.sleep(3)