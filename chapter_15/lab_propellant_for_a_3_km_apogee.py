# Engineering Lab: propellant mass for a 3000 m apogee
import numpy as np
from scipy.optimize import brentq
from rocket import fly, T_BURN, M_DRY, ISP

TARGET = 3000.0                  # required apogee, m


def miss(m_prop):
    """Apogee minus target, m, for a given propellant mass."""
    return fly(m_prop)[1].y[0, -1] - TARGET


for m in [0.5, 1.0, 1.5, 2.0, 2.5]:
    print(f'm_prop = {m:.1f} kg  ->  miss = {miss(m):8.1f} m')

m_req = brentq(miss, 1.0, 2.5, xtol=1e-4)    # kg
burn, coast = fly(m_req)
h, v, m = np.hstack([burn.y, coast.y])
a = np.sqrt(1.4 * 287.053 * (288.15 - 0.0065 * h))   # m/s
print(f'Propellant needed: {m_req:.3f} kg')
print(f'Apogee {coast.y[0, -1]:.1f} m at t = {coast.t[-1]:.2f} s')
print(f'Burnout speed {burn.y[1, -1]:.1f} m/s, '
      f'peak Mach {np.max(v / a):.3f}')
print(f'Lift-off thrust-to-weight: '
      f'{m_req / T_BURN * ISP / (M_DRY + m_req):.1f}')
