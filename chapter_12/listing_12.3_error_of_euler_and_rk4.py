# Accuracy of Euler and RK4 on the cooling ball of Listing 12.1
import math
from odesteps import euler_step, rk4_step

tau = 7832.0 * 434.0 * 0.020 / (6.0 * 150.0)   # time constant, s
t_air, t_init, t_end = 25.0, 300.0, 300.0      # deg C, deg C, s


def f(t, temp):
    return -(temp - t_air) / tau


def march(step, h):
    """Take steps of size h from t = 0 to t_end; return y(t_end)."""
    t, y = 0.0, t_init
    for n in range(round(t_end / h)):
        y = step(f, t, y, h)
        t = t + h
    return y


exact = t_air + (t_init - t_air) * math.exp(-t_end / tau)
print(f'Exact T({t_end:.0f} s) = {exact:.6f} deg C')
print('   h (s)   Euler error   RK4 error   (K)')
for h in [60.0, 30.0, 15.0, 7.5, 3.75]:
    e1 = march(euler_step, h) - exact
    e4 = march(rk4_step, h) - exact
    print(f'{h:8.2f} {e1:13.3e} {e4:11.3e}')
