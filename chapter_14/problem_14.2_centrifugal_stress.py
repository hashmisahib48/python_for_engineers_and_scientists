# Problem 14.2  Centrifugal stress in a tapered turbine blade
import numpy as np
from scipy.integrate import quad
from fem1d import bar_k, assemble, solve_fixed

rho, E = 8200.0, 200e9           # nickel superalloy: kg/m^3, Pa
omega = 12000 * 2 * np.pi / 60   # 12 000 rpm in rad/s
r0, r1 = 0.30, 0.36              # root and tip radius, m
A0, taper = 2.0e-4, 0.5          # root area, m^2; A_tip / A_root


def area(r):
    return A0 * (1 + (taper - 1) * (r - r0) / (r1 - r0))   # m^2


def blade(n):
    """Root-element stress and root reaction stress, Pa."""
    r = np.linspace(r0, r1, n + 1)
    le, A_mid = r[1] - r[0], area((r[:-1] + r[1:]) / 2)
    k_list = [bar_k(E, A_mid[e], le) for e in range(n)]
    K = assemble(n + 1, [(e, e + 1) for e in range(n)], k_list)
    w = rho * omega**2 * A_mid * le / 6     # load factor, N/m
    F = np.append(w * (2 * r[:-1] + r[1:]), 0.0)   # loads, N
    F[1:] += w * (r[:-1] + 2 * r[1:])
    u, R = solve_fixed(K, F, fixed=[0], values=[0.0])
    return E * (u[1] - u[0]) / le, -R[0] / A0


F_c = rho * omega**2 * quad(lambda r: area(r) * r, r0, r1)[0]  # N
s_exact = F_c / A0                          # root stress, Pa
print(f'Exact root stress: {s_exact / 1e6:.2f} MPa')
n = 1
while True:
    s_el, s_R = blade(n)
    err = abs(s_el - s_exact) / s_exact
    print(f'n = {n:3d}: element {s_el / 1e6:7.2f} MPa ({err:.2%}), '
          f'reaction {s_R / 1e6:7.2f} MPa')
    if err < 0.01:
        break
    n *= 2
