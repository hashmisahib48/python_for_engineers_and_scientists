# Example 11.1  Where is a Molniya satellite after t hours?
import math
from scipy.optimize import brentq

MU = 398600.4418        # Earth's gravitational parameter, km^3/s^2
R_E = 6378.137          # Earth's equatorial radius, km
a = 26600.0             # semi-major axis, km
e = 0.74                # eccentricity, -

T = 2 * math.pi * math.sqrt(a**3 / MU)          # period, s


def kepler_newton(m, e, tol=1e-12):
    """Solve E - e sin E = M by Newton; returns (E, steps)."""
    ecc = m if e < 0.8 else math.pi              # starting value
    for n in range(1, 30):
        f = ecc - e * math.sin(ecc) - m
        dx = f / (1 - e * math.cos(ecc))
        ecc -= dx
        if abs(dx) < tol:
            return ecc, n
    raise RuntimeError('Kepler iteration failed')


print(f'Period T = {T:.0f} s = {T / 3600:.3f} h')
print(' t (h)   M (rad)   E (rad)  steps  nu (deg)  alt (km)')
worst = 0.0
for hour in range(12):
    m = 2 * math.pi * hour * 3600 / T            # mean anomaly
    ecc, n = kepler_newton(m, e)
    check = brentq(lambda x: x - e * math.sin(x) - m,
                   0.0, 2 * math.pi)
    worst = max(worst, abs(ecc - check))
    nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(ecc / 2),
                        math.sqrt(1 - e) * math.cos(ecc / 2))
    alt = a * (1 - e * math.cos(ecc)) - R_E
    print(f'{hour:5d} {m:9.4f} {ecc:9.4f} {n:5d} '
          f'{math.degrees(nu) % 360:9.1f} {alt:9.0f}')
print(f'Largest difference from brentq: {worst:.1e} rad')
