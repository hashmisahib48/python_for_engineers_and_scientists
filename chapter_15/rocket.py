# Project 1: vertical ascent of a sounding rocket, drag + mass loss
import numpy as np
from scipy.integrate import solve_ivp

G0 = 9.80665                  # standard gravity, m/s^2
M_DRY = 6.0                   # rocket + payload, no propellant, kg
ISP = 170.0                   # specific impulse of the motor, s
T_BURN = 6.0                  # burn time, s
AREA = np.pi * 0.10**2 / 4    # frontal area, d = 0.10 m, m^2
CD = 0.45                     # drag coefficient (subsonic)


def air_density(h):
    """ISA troposphere density, kg/m^3 (h in m, h < 11 km)."""
    return 1.225 * (1 - 0.0065 * h / 288.15)**4.2559


def fly(m_prop, cd=CD):
    """Burn, then coast to apogee; return both solve_ivp results."""
    mdot = m_prop / T_BURN               # mass flow rate, kg/s

    def rhs(t, s):
        h, v, m = s
        burning = t < T_BURN
        thrust = mdot * G0 * ISP if burning else 0.0     # N
        drag = 0.5 * air_density(h) * cd * AREA * v * abs(v)
        return [v, (thrust - drag) / m - G0,
                -mdot if burning else 0.0]

    def apogee(t, s):                    # event: v = 0
        return s[1]
    apogee.terminal, apogee.direction = True, -1
    burn = solve_ivp(rhs, (0, T_BURN), [0, 0, M_DRY + m_prop],
                     rtol=1e-8, max_step=0.05)
    coast = solve_ivp(rhs, (T_BURN, 300), burn.y[:, -1],
                      events=apogee, rtol=1e-8, max_step=0.1)
    return burn, coast
