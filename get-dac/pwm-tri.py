import time
import pwm_dac as pwm

amp = 3.2
freq = 10
fs = 1000

dac = None

try:
    dac = pwm.PWM_DAC(12, 500, 3.3)

    t = 0
    dt = 1 / fs

    while True:
        val = abs(2 * (t * freq - int(t * freq + 0.5)))
        voltage = val * amp

        voltage = max(0, min(voltage, 3.3))

        dac.set_voltage(voltage)

        time.sleep(dt)
        t += dt

finally:
    if dac:
        dac.deinit()
