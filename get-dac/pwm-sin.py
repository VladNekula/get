import time
import numpy as np
import pwm_dac as pwm

amp = 3.2
freq = 10
fs = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.3)

    t = 0
    dt = 1 / fs

    while True:
        val = (np.sin(2 * np.pi * freq * t) + 1) / 2
        dac.set_voltage(val * amp)

        time.sleep(dt)
        t += dt

finally:
    dac.deinit()
