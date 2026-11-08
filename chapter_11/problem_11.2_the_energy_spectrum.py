# Problem 11.2  The energy spectrum of fission neutrons
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def chi(e):
    """Watt spectrum for U-235 thermal fission, per MeV."""
    return 0.453 * np.exp(-1.036 * e) * np.sinh(np.sqrt(2.29 * e))


def slope(e, h=1e-5):
    """Central-difference derivative of chi, per MeV^2."""
    return (chi(e + h) - chi(e - h)) / (2 * h)


total, _ = quad(chi, 0.0, np.inf)
mean, _ = quad(lambda e: e * chi(e), 0.0, np.inf)
fast, _ = quad(chi, 1.0, np.inf)
peak = brentq(slope, 0.1, 2.0)

print(f'Integral of chi:          {total:.4f}')
print(f'Mean neutron energy:      {mean / total:.3f} MeV')
print(f'Fraction above 1 MeV:     {fast / total:.3f}')
print(f'Most probable energy:     {peak:.4f} MeV')
