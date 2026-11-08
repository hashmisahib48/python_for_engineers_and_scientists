# Problem 1.3  Switching on the series RLC circuit
import math
import cmath

v_s = 12.0          # battery voltage, V
res = 10.0          # resistance, ohm
ind = 50e-3         # inductance, H
cap = 100e-6        # capacitance, F

disc = res**2 - 4 * ind / cap                   # negative, ohm^2
s1 = (-res + cmath.sqrt(disc)) / (2 * ind)      # root, 1/s
s2 = (-res - cmath.sqrt(disc)) / (2 * ind)      # root, 1/s

alpha = -s1.real                    # decay rate, 1/s
w_d = s1.imag                       # damped frequency, rad/s
zeta = alpha * math.sqrt(ind * cap)             # alpha / w_0
over = math.exp(-zeta * math.pi / math.sqrt(1 - zeta**2))
t_p = math.pi / w_d                 # first peak, s
v_p = v_s * (1 - math.exp(-alpha * t_p) * (math.cos(w_d * t_p)
             + alpha / w_d * math.sin(w_d * t_p)))   # V

print('Roots (1/s):', s1, s2)
print('Sum, product:', s1 + s2, s1 * s2)
print('1/(L C) (1/s^2):', 1 / (ind * cap))
print('Damping ratio:', round(zeta, 4))
print('Ringing frequency (Hz):', round(w_d / (2 * math.pi), 2))
print('Overshoot (%):', round(over * 100, 1))
print('First peak (ms, V):', round(t_p * 1e3, 2), round(v_p, 2))
print('Settling time, 2 % (ms):', round(4 / alpha * 1e3, 1))
print('Critical R (ohm):', round(2 * math.sqrt(ind / cap), 2))
