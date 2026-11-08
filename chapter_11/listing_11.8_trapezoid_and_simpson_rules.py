# Listing 11.8  Trapezoid and Simpson rules for compression work
import numpy as np
from scipy.integrate import simpson, trapezoid

P1 = 100e3            # initial pressure, Pa
V1 = 2.0e-3           # initial volume, m^3
V2 = 0.5e-3           # final volume, m^3


def p(v):
    """Pressure on the isotherm p V = p1 V1, Pa."""
    return P1 * V1 / v


def trap(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (b - a) / n * (y[0] / 2 + y[1:-1].sum() + y[-1] / 2)


def simp(f, a, b, n):                     # n must be even
    x = np.linspace(a, b, n + 1)
    y = f(x)
    s = y[0] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum() + y[-1]
    return (b - a) / (3 * n) * s


w_exact = P1 * V1 * np.log(V1 / V2)       # work done on gas, J
print(f'Exact work: {w_exact:.6f} J')
print('   n   trapezoid error   Simpson error')
for n in [2, 4, 8, 16, 32]:
    et = trap(p, V2, V1, n) - w_exact
    es = simp(p, V2, V1, n) - w_exact
    print(f'{n:4d} {et:17.3e} {es:15.3e}')
x = np.linspace(V2, V1, 9)
print(f'SciPy, n = 8: trapezoid {trapezoid(p(x), x=x):.6f} J, '
      f'simpson {simpson(p(x), x=x):.6f} J')
