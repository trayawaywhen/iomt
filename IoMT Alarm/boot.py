import sys
sys.path.reverse()
import time
import mqtt_alarm
print("\n\n\nLets get this shit fired up!!!")

while True:
#     try:
    mqtt_alarm.client.check_msg()  # Tjekker besked sendt fra broker
#     except:
#         print("Error")
#         sleep(0.1)
