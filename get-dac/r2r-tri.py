import time
import numpy as np
import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        if not isinstance(number, int):
            print("Нужно целое число")
            return
        if not (0 <= number <= 255):
            print("Число вне диапазона")
            return

        binary = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, binary)

        if self.verbose:
            print(f"Число: {number}, биты: {binary}")

    def set_voltage(self, svoltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Напряжение вне диапазона")
            return

        number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.16, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()

amp = 3.2
freq = 10
fs = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3)

    t = 0
    dt = 1 / fs

    while True:
        period = 1 / freq
        x = (t % period) / period
        val = 2*x if x < 0.5 else 2*(1-x)

        dac.set_voltage(val * amp)

        time.sleep(dt)
        t += dt

finally:
    dac.deinit()
