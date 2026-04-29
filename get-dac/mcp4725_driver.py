import smbus

class MCP4725:
    def __init__(self, max_v, addr=0x61):
        self.bus = smbus.SMBus(1)
        self.addr = addr
        self.max_v = max_v

    def deinit(self):
        self.bus.close()

    def set_number(self, n):
        if not isinstance(n, int):
            print("Только целые числа")
            return

        if not (0 <= n <= 4095):
            print("Вне диапазона")
            return

        high = (n » 8) & 0x0F
        low = n & 0xFF

        # правильная команда для MCP4725
        self.bus.write_i2c_block_data(self.addr, 0x40, [high « 4, low])

    def set_voltage(self, v):
        if not isinstance(v, (int, float)):
            print("Не число")
            return

        if not (0 <= v <= self.max_v):
            print("Вне диапазона")
            return

        n = int(v / self.max_v * 4095)
        self.set_number(n)

if __name__ == "__main__":
    try:
        dac = MCP4725(5.0)

        while True:
            try:
                v = float(input("Введите напряжение: "))
                dac.set_voltage(v)
            except ValueError:
                print("Ошибка")

    finally:
        dac.deinit()
