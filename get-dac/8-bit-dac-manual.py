import RPi.GPIO as GPIO

dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT, initial = 0)

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)

def dec2bin(value):
        return[int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            print(number, dec2bin(number))

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()