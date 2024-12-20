from machine import SoftI2C
from machine import Pin
import time
from mpu6050 import MPU6050
import sys


pinScl = 18
pinSda = 19

deviceAddress = 0x48

uNom = 3.25


i2c = SoftI2C(scl=Pin(pinScl), sda=Pin(pinSda))

imu = MPU6050(i2c)

gyro_x_averages = []
gyro_y_averages = []
gyro_z_averages = []
list_pos = 0
timestamp = 0
farmor_status = False

def threshold(gyro_x_averages, gyro_y_averages, gyro_z_averages, fall_threshold):
    if sum(gyro_x_averages)/len(gyro_x_averages) >= fall_threshold or sum(gyro_y_averages)/len(gyro_y_averages) >= fall_threshold:
        return True
    else:
        return False

def gyro_mål(timestamp, gyro_x_averages, gyro_y_averages, gyro_z_averages, list_pos, farmor_status):
    for i in range(5):
        readings_limit = 5
        gyro_x_readings = []
        gyro_y_readings = []
        gyro_z_readings = []
        for i in range(20):
            imu_values = imu.get_values()
            gyro_x_readings.append(abs(imu_values["gyroscope x"]/100))
            gyro_y_readings.append(abs(imu_values["gyroscope y"]/100))
            gyro_z_readings.append(abs(imu_values["gyroscope z"]/100))
        gyro_x = sum(gyro_x_readings) / len(gyro_x_readings)
        gyro_y = sum(gyro_y_readings) / len(gyro_y_readings)
        gyro_z = sum(gyro_z_readings) / len(gyro_z_readings)
        
        if len(gyro_x_averages) >= readings_limit:
            gyro_x_averages[list_pos] = gyro_x
            gyro_y_averages[list_pos] = gyro_y
            gyro_z_averages[list_pos] = gyro_z
            if list_pos >= len(gyro_x_averages)-1:
                list_pos = 0
            list_pos += 1
        else:
            gyro_x_averages.append(gyro_y)
            gyro_y_averages.append(gyro_x)
            gyro_z_averages.append(gyro_z)
            
#         print(f"\nx: {gyro_x}")
#         print(f"y: {gyro_y}")
#         print(f"z: {gyro_z}")
        
        if threshold(gyro_x_averages, gyro_y_averages, gyro_z_averages, 200) == True:
            farmor_status = True
            timestamp = time.time()
#         elif threshold(gyro_x_averages, gyro_y_averages, gyro_z_averages, 300) == False and time.time() - timestamp >= 5:
#             farmor_status = False
    
#     print(farmor_status)
    
    return farmor_status
# while True:
#     gyro_mål(timestamp, gyro_x_averages, gyro_y_averages, gyro_z_averages, list_pos, farmor_status)
#     time.sleep_ms(200)

