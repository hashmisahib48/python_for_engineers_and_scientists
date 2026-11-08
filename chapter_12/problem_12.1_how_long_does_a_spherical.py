# Problem 12.1: draining a spherical water tank through an orifice
import numpy as np
from scipy.integrate import solve_ivp

g = 9.80665                 # standard gravity, m/s^2
R, cd = 1.5, 0.61           # tank radius m, discharge coefficient
a_hole = np.pi * 0.050**2 / 4      # orifice area, m^2
h0 = 2 * R - 1e-6           # full tank, just below the top, m


def dhdt(t, y):
    h = max(y[0], 1e-9)                 # keep h positive
    area = np.pi * (2 * R * h - h**2)   # free-surface area, m^2
    return [-cd * a_hole * np.sqrt(2 * g * h) / area]


def half(t, y):              # depth equals the radius
    return y[0] - R


def empty(t, y):             # depth down to 1 mm
    return y[0] - 0.001


def t_exact(h):              # exact time to fall from 2R to h, s
    big_f = 4 * R / 3 * h**1.5 - 0.4 * h**2.5
    full = 4 * R / 3 * (2 * R)**1.5 - 0.4 * (2 * R)**2.5
    return np.pi * (full - big_f) / (cd * a_hole * np.sqrt(2 * g))


empty.terminal = True
sol = solve_ivp(dhdt, (0.0, 1e5), [h0], events=[half, empty],
                rtol=1e-8, atol=1e-10)
t_half, t_empty = sol.t_events[0][0], sol.t_events[1][0]
print(f'Half full: {t_half / 60:7.3f} min, '
      f'exact {t_exact(R) / 60:.3f}')
print(f'Empty:     {t_empty / 60:7.3f} min, '
      f'exact {t_exact(0.001) / 60:.3f}')
print(f'Second half takes {(t_empty - t_half) / t_half:.2f} times '
      'as long as the first')
