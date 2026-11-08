# Example 1.5  Series RLC circuit on a 230 V, 50 Hz supply
import math
import cmath

v_rms = 230.0       # supply voltage (rms), V; phase reference
f = 50.0            # supply frequency, Hz
res = 10.0          # resistance, ohm
ind = 50e-3         # inductance, H
cap = 100e-6        # capacitance, F

w = 2 * math.pi * f                         # angular freq., rad/s
z = res + 1j * (w * ind - 1 / (w * cap))    # impedance, ohm
i = v_rms / z                               # current phasor, A
f_0 = 1 / (2 * math.pi * math.sqrt(ind * cap))  # resonance, Hz

print('Impedance Z (ohm):', z)
print('|Z| (ohm):', round(abs(z), 3))
print('Phase of Z (deg):', round(math.degrees(cmath.phase(z)), 2))
print('Current |I| (A):', round(abs(i), 3))
print('Phase of I (deg):', round(math.degrees(cmath.phase(i)), 2))
print('Power factor:', round(math.cos(cmath.phase(z)), 4))
print('Real power (W):', round(abs(i)**2 * res, 1))
print('Resonant frequency (Hz):', round(f_0, 2))
