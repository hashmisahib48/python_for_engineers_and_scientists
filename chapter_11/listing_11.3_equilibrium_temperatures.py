# Listing 11.3  Equilibrium temperatures of a two-node spacecraft
from scipy.optimize import fsolve

SIGMA = 5.670374419e-8   # Stefan-Boltzmann constant, W/(m^2 K^4)
S = 1361.0               # solar irradiance at 1 au, W/m^2
ALPHA = 0.25             # solar absorptivity of the panel, -
EPS = 0.85               # infrared emissivity of both nodes, -
A1, A2 = 1.0, 0.5        # radiating areas of the nodes, m^2
G = 2.0                  # conductance of the link, W/K
Q = 150.0                # electronics dissipation in node 2, W


def balance(temps):
    """Net heat flow into each node, W; zero at equilibrium."""
    t1, t2 = temps
    link = G * (t1 - t2)                         # node 1 -> 2, W
    r1 = ALPHA * S * A1 - EPS * SIGMA * A1 * t1**4 - link
    r2 = Q + link - EPS * SIGMA * A2 * t2**4
    return [r1, r2]


guess = [300.0, 300.0]                           # K
t1, t2 = fsolve(balance, guess)
print(f'Panel:       T1 = {t1:.2f} K = {t1 - 273.15:.2f} degC')
print(f'Electronics: T2 = {t2:.2f} K = {t2 - 273.15:.2f} degC')
r1, r2 = balance([t1, t2])
print(f'Residuals: {r1:.1e} W and {r2:.1e} W')
print(f'Heat through the link: {G * (t1 - t2):.2f} W')
