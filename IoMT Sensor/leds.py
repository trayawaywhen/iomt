import machine
import time

led1 = machine.Pin(33, machine.Pin.OUT)


def on_off(led, on_ms, off_ms):
    """
    Tænder og slukker den valgte led
    led = valgte led der skal tændes og slukkes
    on_ms = Hvor lang tid leden skal forblive tændt i millisekunder
    off_ms = Hvor lang tid leden skal forblive slukket i millisekunder
    """
    led.on()
    print("on")
    time.sleep_ms(on_ms)
    led.off()
    print("off")
    time.sleep_ms(off_ms)

def on(led):
    """
    Tænder den valgte led
    led = valgte led der skal tændes og slukkes
    """
    led.on()

def off(led):
    """
    Slukker den valgte led
    led = valgte led der skal tændes og slukkes
    """
    led.off()


# while True:
#     led1.on()
#     print("on")
#     time.sleep_ms(500)
#     led1.off()
#     print("off")
#     time.sleep_ms(500)

