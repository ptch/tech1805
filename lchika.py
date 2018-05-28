import RPi.GPIO as GPIO
import time

GPIO_LED = 2
GPIO.setwarning(False)
GPIO.setmote(GPIO.BCM)
GPIO.setup(GPIO_LED, GPIO.OUT)
while True:
    GPIO.output(GPIO_LED, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(GPIO_LED, GPIO.LOW)
    time.sleep(0.2)

