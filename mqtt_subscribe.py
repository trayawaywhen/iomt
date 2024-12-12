import paho.mqtt.subscribe as subscribe

def get_rpi_data():
    messsage = subscribe.simple("paho/test/topic", hostname="51.138.188.250")
    result = json.loads(message.payload.decode())
    return result

