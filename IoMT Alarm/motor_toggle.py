from machine import Pin
from time import sleep

VIBR_PIN = 25

vibr_motor = Pin(VIBR_PIN, Pin.OUT)

def on_off(motor, time_on):
    """
        motor == hvilken motor
        time_on == tid i sekunder, at motoren er tændt
    """
    motor.on()
    sleep(time_on)
    motor.off()
    
def on(motor):
    motor.on()
    
def off(motor):
    motor.off()