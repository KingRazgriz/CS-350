import RPI.GPIO as GPIO
import time

LED_PIN = 18

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 60)
pwm.start(0)

try:
    while True:
        # Fade In
        for duty_cycle in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)

        # Fade Out
        for duty_cycle in range(100, -1, -5)
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStopping PWM & Cleaning up GPIO. Process Complete!")
    pwm.stop()
    GPIO.cleanup()