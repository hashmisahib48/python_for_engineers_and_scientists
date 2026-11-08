# Problem 15.2: orbital lifetime of a 3U CubeSat
import numpy as np
from scipy.integrate import solve_ivp

MU, RE = 3.986004418e14, 6378137.0    # m^3/s^2, m
B = 2.2 * 0.02 / 4.0                  # C_D A / m, m^2/kg
# exponential atmosphere: base altitude km, density kg/m^3, H km
H0 = np.array([180, 200, 250, 300, 350, 400, 450, 500])
RHO0 = np.array([5.464e-10, 2.789e-10, 7.248e-11, 2.418e-11,
                 9.518e-12, 3.725e-12, 1.585e-12, 6.967e-13])
SH = np.array([29.740, 37.105, 45.546, 53.628, 53.298,
               58.515, 60.828, 63.822])


def density(h_km):
    """Piecewise exponential model, valid 180-550 km."""
    k = np.searchsorted(H0, h_km, side='right') - 1
    return RHO0[k] * np.exp(-(h_km - H0[k]) / SH[k])


def dadt(t, s):
    a = s[0]                                  # semi-major axis, m
    return [-np.sqrt(MU * a) * density((a - RE) / 1e3) * B]


def reentry(t, s):                            # stop at 180 km
    return s[0] - (RE + 180e3)


reentry.terminal = True
DAY = 86400.0
print('start (km)  first rate (km/day)  lifetime (days)  (years)')
for h0 in [350, 400, 450]:
    sol = solve_ivp(dadt, (0, 30 * 365 * DAY), [RE + h0 * 1e3],
                    events=reentry, rtol=1e-8)
    t_end = sol.t_events[0][0] / DAY                   # days
    rate = -dadt(0, [RE + h0 * 1e3])[0] * DAY / 1e3    # km/day
    print(f'{h0:10d}  {rate:19.3f}  {t_end:15.0f}  '
          f'{t_end / 365.25:7.2f}')
