from machine import Pin, SoftI2C
from time import sleep

# CONFIGURATION
# Soft I2C pins
pinScl = 18
pinSda = 19

# The MCP3021 I2C address
deviceAddress = 0x48

# The ADC to voltage ratio (the voltage divider).
# To find it make a single measurement and make a note
# of the voltage and ADC values. Then calculate Unom
# Unom = 1023 * Ureal / ADCvalue
uNom = 3.25

# PROGRAM
i2c = SoftI2C(scl=Pin(pinScl), sda=Pin(pinSda))

def temperatur(deviceAddress, uNom, i2c):
    # Measure and get the two bytes from the ADC
    adcBytes = i2c.readfrom(deviceAddress, 2)
    
    # Put the bytes in UpperDataByte and LowerDataByte
    UpperDataByte = int(adcBytes[0])
    LowerDataByte = int(adcBytes[1])
    
    # Print the raw received bytes
#     print("ADC Upper Data Byte: 0x%02X" % UpperDataByte)
#     print("ADC Lower Data Byte: 0x%02X" % LowerDataByte)

    # Step A1, right justify D5-D0 into position
    lowerData = LowerDataByte >> 2
#     print("lowerData, D5-D0   : 0x%02X" % lowerData)
    
    # Step A2, left justify D7-D6 into position
    upperData = (UpperDataByte << 6) & 0xC0  # Mask out D9-D8!
#     print("upperData, D7-D6   : 0x%02X" % upperData)
    
    # Step A3, merge D7-D6 with D5-D0
    lowerByte = upperData + lowerData
#     print("lowerByte, D7-D0   : 0x%02X" % lowerByte)
    
    # Step A4, right justify D9-D8 into position
    upperByte = UpperDataByte >> 2
#     print("upperByte, D9-D8   : 0x%02X" % upperByte)
    
    # Step A5, merge upperByte (D9-D8) with lowerByte (D7-D0)
    adcValue = (upperByte << 8) + lowerByte
#     print("adcValue, hex      : 0x%04X" % adcValue)
#     print("adcValue, dec      : %d" % adcValue)
    
    # Calculate the voltage
    voltage = adcValue * uNom / 1023.0
#     print("Voltage            : %.2f V" % voltage)
    
#     print("mv", voltage*1000)
#     print("mv under 0C", (voltage * 1000) - 1034)
    
    celsius = ((voltage * 1000) - 1034) / -5.45
#     print(celsius)
    return celsius
    
    # Pause before next measurement
#     sleep(1)
#     print()

