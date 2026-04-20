import time
import mcp4725_driver as mcp

amp = 5.0
freq = 10
fs = 1000

try:
    dac = mcp.MCP4725(5.0)

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
