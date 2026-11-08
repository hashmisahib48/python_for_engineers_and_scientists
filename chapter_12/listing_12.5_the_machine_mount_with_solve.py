# The damped machine mount again, solved with SciPy's solve_ivp
import numpy as np
from scipy.integrate import solve_ivp

m, k, c = 250.0, 4.0e5, 1000.0   # kg, N/m, N s/m
x0 = 0.005                       # initial displacement, m


def f(t, y):
    x, v = y
    return [v, -(c * v + k * x) / m]


t_out = np.linspace(0.0, 1.5, 751)          # report times, s
wn, zeta = np.sqrt(k / m), c / (2 * np.sqrt(k * m))
wd = wn * np.sqrt(1 - zeta**2)
exact = x0 * np.exp(-zeta * wn * t_out) * (np.cos(wd * t_out)
        + zeta / np.sqrt(1 - zeta**2) * np.sin(wd * t_out))

for rtol in [1e-3, 1e-6, 1e-9]:
    sol = solve_ivp(f, (0.0, 1.5), [x0, 0.0], t_eval=t_out,
                    rtol=rtol, atol=rtol * 1e-3)
    err = np.max(np.abs(sol.y[0] - exact))
    print(f'rtol = {rtol:.0e}: {sol.nfev:5d} calls of f, '
          f'largest error {err:.1e} m')
print(sol.message)
print('sol.y has shape', sol.y.shape)
