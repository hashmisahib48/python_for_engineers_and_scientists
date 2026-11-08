# Ballistic re-entry of a capsule: deceleration and parachute point
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

MU, R_E = 3.986004418e14, 6.371e6   # GM m^3/s^2, Earth radius m
RHO0, H, G0 = 1.225, 7200.0, 9.80665   # kg/m^3, m, m/s^2
beta = 1500.0 / (1.3 * np.pi * 1.0**2)    # m/(Cd A), kg/m^2
v0, gam0 = 7800.0, np.radians(-2.0)        # entry speed, angle


def f(t, s):               # s = [x, z, vx, vz], Earth center at 0
    x, z, vx, vz = s
    r, v = np.hypot(x, z), np.hypot(vx, vz)
    rho = RHO0 * np.exp(-(r - R_E) / H)     # air density, kg/m^3
    a_d = rho * v / (2 * beta)              # drag / speed, 1/s
    a_g = MU / r**3                         # gravity / r, 1/s^2
    return [vx, vz, -a_d * vx - a_g * x, -a_d * vz - a_g * z]


def chute(t, s):                    # zero at an altitude of 10 km
    return np.hypot(s[0], s[1]) - R_E - 10e3


chute.terminal = True               # stop the integration there
s0 = [0.0, R_E + 120e3, v0 * np.cos(gam0), v0 * np.sin(gam0)]
sol = solve_ivp(f, (0, 3000), s0, events=chute, max_step=1.0,
                rtol=1e-8, atol=1e-6)
x, z, vx, vz = sol.y              # each row is one variable
alt, v = np.hypot(x, z) - R_E, np.hypot(vx, vz)
n_g = RHO0 * np.exp(-alt / H) * v**2 / (2 * beta) / G0
k = np.argmax(n_g)                  # index of peak deceleration
print(f'Peak deceleration: {n_g[k]:.2f} g at {alt[k] / 1e3:.1f} km')
t_c = sol.t_events[0][0]           # time of the event, s
print(f'Parachute: t = {t_c:.0f} s, v = {v[-1]:.0f} m/s')
print(f'Downrange: {R_E * np.arctan2(x[-1], z[-1]) / 1e3:.0f} km')
plt.plot(sol.t, n_g)
plt.xlabel('Time since entry interface t (s)')
plt.ylabel('Deceleration (g)')
plt.show()
