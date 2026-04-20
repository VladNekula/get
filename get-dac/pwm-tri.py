import time
import pwm_dac as pwm

amp = 3.2
freq = 10
fs = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.3)

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
