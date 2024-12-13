import paho.mqtt.subscribe as subscribe
from io import BytesIO
import base64
import json

from matplotlib.figure import Figure

def get_device_data():
    try:
        messsage = subscribe.simple("paho/test/topic", hostname="51.138.188.250")
        result = json.loads(message.payload.decode())
        return result

    except Exception:
        print(Exception)

def falls_graph():
    device_data = get_device_data()
    residents = device_data['residents']
    falls = device_data['falls']

    fig = Figure()
    ax = fig.add_subplot()

    bar_labels = residents

    ax.bar(residents, falls, label=bar_labels)

    ax.set_ylabel('Antal fald')
    ax.set_title('Fald')
    ax.legend(title='Beboere')

    buf = BytesIO()

    fig.savefig(buf, format='png')

    return base64.b64encode(buf.getbuffer()).decode('ascii')
