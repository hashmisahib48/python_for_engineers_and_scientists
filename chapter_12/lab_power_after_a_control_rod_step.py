# Point reactor kinetics, one delayed group: a 100 pcm rod step
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

beta = 0.0065       # delayed neutron fraction (U-235)
lam = 0.08          # precursor decay constant, 1/s
gen = 5.0e-5        # prompt neutron generation time, s
rho = 0.0010        # reactivity added by the rod, 100 pcm


def kinetics(t, y):
    """y = [P, C]: relative power and precursor level."""
    p, c = y
    return [(rho - beta) / gen * p + lam * c,
            beta / gen * p - lam * c]


y0 = [1.0, beta / (lam * gen)]          # critical before the step
for method in ['RK45', 'Radau']:
    sol = solve_ivp(kinetics, (0.0, 60.0), y0, method=method,
                    rtol=1e-6, atol=1e-9)
    print(f'{method:6s}: P(60 s) = {sol.y[0, -1]:.4f} P0, '
          f'{sol.nfev:5d} calls of f')

jac = np.array([[(rho - beta) / gen, lam], [beta / gen, -lam]])
s = np.sort(np.linalg.eigvals(jac).real)  # inverse time constants
print(f'Eigenvalues: {s[0]:.3f} and {s[1]:.5f} 1/s')
print(f'Stable period: {1 / s[1]:.1f} s')
print(f'Euler is stable only for dt < {2 / abs(s[0]):.4f} s')
t = np.linspace(0.0, 60.0, 601)
sol = solve_ivp(kinetics, (0.0, 60.0), y0, method='Radau',
                t_eval=t, rtol=1e-6, atol=1e-9)
plt.plot(t, sol.y[0])
plt.xlabel('Time after the rod step t (s)')
plt.ylabel('Relative power P/P0')
plt.show()
