from umqtt.simple2 import MQTTClient
import network
import time
import alarm
import json

SSID = 'gruppe8'
PASSWORD = '88201818'

MQTT_BROKER = '192.168.1.100'
MQTT_TOPIC = 'sensor/data'

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("ESP32 IP", wlan.ifconfig())
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to WiFi')

def publish_data(client):
    sensor_value = alarm.alarm()
    message = json.dumps({"fall" : sensor_value[0], "temperature" : sensor_value[1], "resident" : "Lise"})
    if sensor_value[0] == True:
        client.publish(MQTT_TOPIC, message)
        print(f"Published: {message}")
    else:
        print("Ingen alarm")

connect_wifi()
client = MQTTClient('esp32_sensor', MQTT_BROKER)
client.connect()

while True:
    publish_data(client)
    time.sleep(0.2)