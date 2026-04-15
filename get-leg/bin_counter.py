import RPi.GPIO as GPIO
import time

leds = [16, 12, 25, 17, 27, 23, 22, 24]
num = 0

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
state = 0
period = 0.2

while True:
    if GPIO.input(up):
        num += 1
        print(num, dec2bin(num))
        time.sleep(period)

    def dec2bin(value):
        return[int(element) for element in bin(value)[2:].zfill(8)]