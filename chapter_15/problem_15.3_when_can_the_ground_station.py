# Problem 15.3: when can the ground station talk to the satellite?
import numpy as np
from scipy.integrate import solve_ivp

MU, RE, J2 = 3.986004418e14, 6378137.0, 1.08263e-3   # WGS 84, SI
W_E = 7.292115e-5                     # Earth rotation, rad/s
a, inc = RE + 420e3, np.radians(51.64)
LAT, LON = np.radians(40.0), np.radians(0.0)   # station


def rhs(t, s):                        # as in Listing 15.6
    r, rn = s[:3], np.linalg.norm(s[:3])
    k = 1.5 * J2 * MU * RE**2 / rn**5
    acc = -MU * r / rn**3 + k * r * (5 * (r[2] / rn)**2 - [1, 1, 3])
    return np.concatenate([s[3:], acc])


v0 = np.sqrt(MU / a)
s0 = [a, 0, 0, 0, v0 * np.cos(inc), v0 * np.sin(inc)]
t = np.arange(0, 86400.0, 10.0)                  # s
x, y, z = solve_ivp(rhs, (0, t[-1]), s0, t_eval=t,
                    rtol=1e-10, atol=1e-6).y[:3]
th = W_E * t                                     # Earth angle, rad
sat = np.array([x * np.cos(th) + y * np.sin(th),
                -x * np.sin(th) + y * np.cos(th), z])   # ECEF, m
up = np.array([np.cos(LAT) * np.cos(LON),
               np.cos(LAT) * np.sin(LON), np.sin(LAT)])
rho = sat - RE * up[:, None]                     # station -> sat
el = np.degrees(np.arcsin(up @ rho / np.linalg.norm(rho, axis=0)))
seen = (el > 10.0).astype(int)       # 10 deg mask
starts = np.flatnonzero(np.diff(seen) == 1) + 1
ends = np.flatnonzero(np.diff(seen) == -1) + 1
print('pass  rises (h:min)  duration (min)  max elevation (deg)')
for k, (i, j) in enumerate(zip(starts, ends)):
    hh, mm = divmod(int(t[i]) // 60, 60)       # rise time
    dur = (t[j] - t[i]) / 60                    # min
    print(f'{k + 1:4d}  {hh:9d}:{mm:02d}  {dur:14.1f}  '
          f'{el[i:j].max():19.1f}')
print(f'Contact per day: {seen.sum() * 10 / 60:.1f} min')
