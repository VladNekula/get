import time
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

adc = MCP3021(dynamic_range=3.3)

voltage_values = []
time_values = []
duration = 3.0

try:
    start = time.time()

    while time.time() - start < duration:
        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start)

    plot_voltage_vs_time(time_values, voltage_values, 3.3)
    plot_sampling_period_hist(time_values)

finally:
    adc.deinit()

    #Traceback (most recent call last):
  #File "/home/b01-511/Repositories/get/get-adc/mcp.py", line 15, in <module>
    #voltage_values.append(adc.get_voltage())
  #File "/home/b01-511/Repositories/get/get-adc/mcp3021_driver.py", line 27, in get_voltage
    #number = self.get_number()
  #File "/home/b01-511/Repositories/get/get-adc/mcp3021_driver.py", line 14, in get_number
    #data = self.bus.read_word_data(self.address, 0)
#TimeoutError: [Errno 110] Connection timed out
