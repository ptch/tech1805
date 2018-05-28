import RPi.GPIO as GPIO
import time

GPIO_BUZZER = 21
GPIO.setwarning(False)
GPIO.setmote(GPIO.BCM)
GPIO.setup(GPIO_BUZZER, GPIO.OUT, initial = GPIO.LOW)
Hz = 440 * 3
p = GPIO.PWM(GPIO_BUZZER, 1)
p.ChangeFrequency(Hz)
p.start(50)
time.sleep(0.05)
p.stop()
time.sleep(0.05)
p.ChangeFrequency(Hz)
p.start(50)
time.sleep(0.05)
p.stop()
GPIO.cleanup()
