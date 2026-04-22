import RPi.GPIO as GPIO

dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.158

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT, initial=0)

def voltage_to_number(voltage):
    if not (0 <= voltage <= dynamic_range):
        print("Вне диапазона")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    binary = [int(bit) for bit in bin(number)[2:].zfill(8)]
    GPIO.output(dac_bits, binary)

try:
    while True:
        try:
            v = float(input("Введите напряжение: "))
            number_to_dac(voltage_to_number(v))
        except ValueError:
            print("Ошибка ввода")
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
