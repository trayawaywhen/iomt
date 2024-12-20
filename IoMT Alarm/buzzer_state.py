from machine import Pin, PWM
from time import sleep

BUZZ_PIN = 33
buzzer = PWM(Pin(BUZZ_PIN, Pin.OUT))
buzzer.duty(0)

def alarm(buzzer):
    for i in range(12):
        for i in range(4):
            buzzer.duty(512)
            buzzer.freq(500)
            sleep(0.05)
            buzzer.duty(0)
            sleep(0.05)
        for i in range(4):
            buzzer.duty(512)
            buzzer.freq(100)
            sleep(0.05)
            buzzer.duty(0)
            sleep(0.05)