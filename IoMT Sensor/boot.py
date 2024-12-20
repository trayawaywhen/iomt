import sys
sys.path.reverse()
import time
import publisher

while True:
    publisher.publish_data(publisher.client)
    time.sleep(0.2)