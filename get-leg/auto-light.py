import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
l2 = 6
GPIO.setup(l2, GPIO.IN)
period = 0.05

while True:
    GPIO.output(led, not GPIO.input(l2))
    time.sleep(period)