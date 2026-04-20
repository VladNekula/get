import time
import numpy as np
import mcp4725_driver as mcp

amp = 5.0
freq = 10
fs = 1000

try:
    dac = mcp.MCP4725(5.0)

    t = 0
    dt = 1 / fs

    while True:
        val = (np.sin(2 * np.pi * freq * t) + 1) / 2
        dac.set_voltage(val * amp)

        time.sleep(dt)
        t += dt

finally:
    dac.deinit()
