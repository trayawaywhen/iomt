from machine import I2C, Pin
from time import sleep

i2c = I2C(0, scl=Pin(18), sda=Pin(19))

print("running scanner")

while True:
    devices_identified = i2c.scan()
    devices_count = len(devices_identified)
    print("Total number of devices: %d" % devices_count)
    
    if devices_count == 112:
        print("pulls ups missing")
    else:
        for i in range(devices_count):
            print("Device found at address: 0x%02X" % devices_identified[i])
    print()
    sleep(1)

# # I2C Scanner MicroPython
# from machine import Pin, SoftI2C
# 
# # You can choose any other combination of I2C pins
# i2c = SoftI2C(scl=Pin(18), sda=Pin(19))
# 
# print('I2C SCANNER')
# devices = i2c.scan()
# 
# if len(devices) == 0:
#   print("No i2c device !")
# else:
#   print('i2c devices found:', len(devices))
# 
#   for device in devices:
#     print("I2C hexadecimal address: ", hex(device))
