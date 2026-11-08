# Example 11.4  Heat capacity of solids from the Debye model
import numpy as np
from scipy.integrate import quad
R = 8.314462618          # molar gas constant, J/(mol K)


def integrand(x):
    return x**4 * np.exp(x) / np.expm1(x)**2


def c_debye(t, theta):
    """Molar heat capacity C_v, J/(mol K), at temperature t, K."""
    val, err = quad(integrand, 0.0, theta / t)
    return 9 * R * (t / theta)**3 * val


# name, Debye temperature (K), measured c_p at 298.15 K, J/(mol K)
solids = [('copper', 343.0, 24.44), ('aluminum', 428.0, 24.20),
          ('diamond', 2230.0, 6.11)]
print('solid      theta (K)   Debye C_v   measured c_p')
for name, theta, cp in solids:
    cv = c_debye(298.15, theta)
    print(f'{name:9s} {theta:9.0f} {cv:11.2f} {cp:13.2f}')

c_num = c_debye(10.0, 343.0)                   # copper at 10 K
c_t3 = 12 * np.pi**4 / 5 * R * (10.0 / 343.0)**3
print(f'Copper at 10 K: quad {c_num:.5f}, '
      f'T^3 law {c_t3:.5f} J/(mol K)')
