import RPi.GPIO as GPIO
import time

GPIO_LED = 2
GPIO_BUTTON = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.setup(GPIO_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    GPIO.wait_for_edge(GPIO_BUTTON, GPIO.FALLING)
    while True:
        sw_status = GPIO.input(GPIO_BUTTON)
        if sw_status == 0:
            GPIO.output(GPIO_LED, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(GPIO_LED, GPIO.LOW)
            time.sleep(0.1)
        else:
            GPIO.output(GPIO_LED, GPIO.LOW)
