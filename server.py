import json
from models import Session, SensorData
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
from time import sleep

# Create a session
session = Session()


while True:
    print("Waiting for fall...")
    message = subscribe.simple("sensor/data", hostname="192.168.1.100")
    result = json.loads(message.payload.decode())

    if result != None:
        fall = result['fall']
        temperature = result['temperature']
        resident = result["resident"]

        # Create a new JsonData instance
        sensor_data = SensorData(fall=fall, temperature=temperature, resident=resident)

        # Add and commit the new data
        session.add(sensor_data)
        session.commit()
        session.close()

        payload = fall
        payload_string = str(payload)

        publish.single("alarm/data", payload_string, hostname="192.168.1.100")

        print("Done deal")

        sleep(12)

