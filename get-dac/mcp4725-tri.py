import time
import mcp4725_driver as mcp

amp = 5.0
freq = 10
fs = 1000

dac = None

try:
    dac = mcp.MCP4725(5.0)

    t = 0
    dt = 1 / fs

    while True:
        val = abs(2 * (t * freq - int(t * freq + 0.5)))
        voltage = val * amp

        voltage = max(0, min(voltage, 5.0))

        dac.set_voltage(voltage)

        time.sleep(dt)
        t += dt

finally:
    if dac:
        dac.deinit()
