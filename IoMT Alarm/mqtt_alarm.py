from umqtt.simple2 import MQTTClient
import network
import time
import motor_toggle
import buzzer_state

timestamp = time.time()

# WiFi credentials
SSID = 'gruppe8'
PASSWORD = '88201818'

# MQTT broker addresse
MQTT_BROKER = '192.168.1.100'
MQTT_TOPIC = 'alarm/data'

# Forbinder til WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print('Forbinder til WiFi')

# Callbackington
def message_callback(topic, msg, retain=False, duplicate=False):
    print(f"Faldhændelse opfanget, send hjælp: {msg.decode()}")
    # Alarmius Triggerius
    if msg.decode() == "True":
        print("ALARM!!!")
        motor_toggle.on(motor_toggle.vibr_motor)
        buzzer_state.alarm(buzzer_state.buzzer)
        time.sleep(1)
        motor_toggle.off(motor_toggle.vibr_motor)
        time.sleep(1)
    else:
        print("ERROR WRONG MESSAGE!!!")
        

def alarm():
    print("Faaaaaald")  # Replace with actual alarm action

# Main program
connect_wifi()
client = MQTTClient('esp32_alarm', MQTT_BROKER)
client.set_callback(message_callback)
client.connect()
client.subscribe(MQTT_TOPIC)

# while True:
#     client.check_msg()  # Tjekker besked sendt fra broker
#     time.sleep(1)