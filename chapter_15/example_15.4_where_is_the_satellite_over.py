# Example 15.4: orbit with the J2 bulge and its ground track
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

MU, RE = 3.986004418e14, 6378137.0  # WGS 84 GM m^3/s^2, radius m
J2, W_E = 1.08263e-3, 7.292115e-5   # oblateness, Earth spin rad/s
a, inc = RE + 420e3, np.radians(51.64)   # circular orbit, ISS-like


def rhs(t, s):
    r, v = s[:3], s[3:]
    rn = np.linalg.norm(r)
    z2 = 5 * (r[2] / rn)**2
    k = 1.5 * J2 * MU * RE**2 / rn**5
    acc = -MU * r / rn**3 + k * r * (z2 - [1, 1, 3])
    return np.concatenate([v, acc])


v0 = np.sqrt(MU / a)
s0 = [a, 0, 0, 0, v0 * np.cos(inc), v0 * np.sin(inc)]
T = 2 * np.pi * np.sqrt(a**3 / MU)            # period, s
sol = solve_ivp(rhs, (0, 86400), s0, rtol=1e-10, atol=1e-6,
                t_eval=np.arange(0, 86401, 20.0))
x, y, z = sol.y[:3]
lat = np.degrees(np.arcsin(z / np.linalg.norm(sol.y[:3], axis=0)))
lon = np.degrees(np.arctan2(y, x) - W_E * sol.t)
lon = (lon + 180) % 360 - 180                 # wrap to -180..180
hx, hy, _ = np.cross(sol.y[:3].T, sol.y[3:].T)[-1]
raan = np.degrees(np.arctan2(hx, -hy))        # node after 1 day
rate = -1.5 * 2 * np.pi / T * J2 * (RE / a)**2 * np.cos(inc) * 86400
print(f'Period {T / 60:.2f} min, {86400 / T:.2f} orbits per day')
print(f'Node drift in 1 day: {raan:.3f} deg '
      f'(theory {np.degrees(rate):.3f} deg)')
lon[np.abs(np.diff(lon, append=lon[-1])) > 180] = np.nan
plt.figure(figsize=(7, 3.2))
plt.plot(lon[:950], lat[:950])                # first 5.3 h
plt.xlabel('Longitude (deg)')
plt.ylabel('Latitude (deg)')
plt.show()
