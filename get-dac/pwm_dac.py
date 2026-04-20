import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, pin, freq, max_v):
        self.pin = pin
        self.max_v = max_v

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

        self.pwm = GPIO.PWM(pin, freq)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup()

    def set_voltage(self, v):
        if not (0 <= v <= self.max_v):
            return
        duty = v / self.max_v * 100
        self.pwm.ChangeDutyCycle(duty)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.3)
        while True:
            try:
                v = float(input("Введите напряжение: "))
                dac.set_voltage(v)
            except ValueError:
                print("Ошибка")
    finally:
        dac.deinit()
