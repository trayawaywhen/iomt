import time
import gyro
import temperatur

def alarm():
    temp_status = temperatur.temperatur(temperatur.deviceAddress, temperatur.uNom, temperatur.i2c)
    fald_status = gyro.gyro_mål(gyro.timestamp, gyro.gyro_x_averages, gyro.gyro_y_averages, gyro.gyro_z_averages, gyro.list_pos, gyro.farmor_status)
    return fald_status, temp_status

print(alarm()[0])