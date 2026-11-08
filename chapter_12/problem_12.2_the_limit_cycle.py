# Problem 12.2: limit cycle of a Van der Pol oscillator circuit
import numpy as np
from scipy.integrate import solve_ivp

ind, cap = 10e-3, 0.1e-6     # tank inductance H, capacitance F
t_ref = np.sqrt(ind * cap)   # time unit of the scaled equation, s


def vdp(t, y, mu):
    """y = [x, dx/dt] in dimensionless form."""
    x, v = y
    return [v, mu * (1 - x**2) * v - x]


def up(t, y, mu):            # x crosses zero going upward
    return y[0]


up.direction = 1
print('  mu   x0   period T   amplitude   f (kHz)')
for mu in [0.1, 1.0, 5.0]:
    for x0 in [0.1, 3.0]:
        sol = solve_ivp(vdp, (0.0, 200.0), [x0, 0.0], args=(mu,),
                        events=up, rtol=1e-10, atol=1e-10,
                        dense_output=True)
        tz = sol.t_events[0]             # upward zero crossings
        period = tz[-1] - tz[-2]
        tt = np.linspace(tz[-2], tz[-1], 2001)
        amp = np.max(np.abs(sol.sol(tt)[0]))
        f_khz = 1e-3 / (period * t_ref)  # frequency, kHz
        print(f'{mu:4.1f} {x0:4.1f} {period:10.4f} {amp:10.4f}'
              f'{f_khz:10.3f}')
