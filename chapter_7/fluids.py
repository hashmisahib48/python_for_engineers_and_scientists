"""Pipe-flow functions for water lines (SI units throughout)."""
import math

RHO_WATER = 998.21     # density of water at 20 degC, kg/m^3
MU_WATER = 1.0016e-3   # dynamic viscosity at 20 degC, Pa s
G = 9.80665            # standard gravity, m/s^2


def reynolds(v, d, rho=RHO_WATER, mu=MU_WATER):
    """Reynolds number for mean speed v (m/s) in a bore d (m)."""
    return rho * v * d / mu


def friction_factor(re, rel_rough):
    """Darcy friction factor: 64/Re if laminar, else Swamee-Jain."""
    if re < 2300:
        return 64 / re
    re = max(re, 4000.0)        # transitional band: use Re = 4000
    x = rel_rough / 3.7 + 5.74 / re**0.9
    return 0.25 / math.log10(x)**2


def pressure_drop(v, d, length, rough, rho=RHO_WATER):
    """Friction pressure drop (Pa) along a straight pipe."""
    f = friction_factor(reynolds(v, d, rho), rough / d)
    return f * (length / d) * rho * v**2 / 2


if __name__ == '__main__':
    # self-test against Example 3.1: 1.2 m/s, 30 m of 25 mm steel
    dp = pressure_drop(1.2, 0.025, 30.0, 0.045e-3)
    print(f'Self-test: dp = {dp / 1000:.2f} kPa (expect 24.13)')
