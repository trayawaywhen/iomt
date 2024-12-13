import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import json

def subscribe():
    message = subscribe.simple("sensor/data", hostname="")
    result = json.loads(message.payload.decode())
    return result


def publish(data):
    publish.single("paho/test/topic", data, hostname="51.138.188.250")


esp_data = subscribe()

publish(esp_data)

