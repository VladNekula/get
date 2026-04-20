import time
import r2r_dac as r2r

amp = 3.2
freq = 10
fs = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3)

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
