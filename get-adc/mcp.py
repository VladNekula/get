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
