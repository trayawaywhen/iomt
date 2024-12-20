import time
import motor_toggle
import buzzer_state

timestamp = time.time()

motor_toggle.on(motor_toggle.vibr_motor)

while True:
    buzzer_state.alarm(buzzer_state.buzzer)
    
    if time.time() - timestamp >= 300:
        motor_toggle.off(motor_toggle.vibr_motor)
    time.sleep(1)
    
    