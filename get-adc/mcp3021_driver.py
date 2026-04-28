import smbus

class MCP3021:
    def __init__(self, dynamic_range, verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)

        lower = data » 8
        upper = data & 0xFF

        number = (upper « 6) | (lower » 2)

        if self.verbose:
            print(f"Data: {data}, upper: {upper:x}, lower: {lower:x}, number: {number}")

        return number

    def get_voltage(self):
        number = self.get_number()
        voltage = number / 1023 * self.dynamic_range
        return voltage
