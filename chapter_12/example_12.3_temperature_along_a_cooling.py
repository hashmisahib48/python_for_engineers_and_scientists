# Temperature in an aluminum pin fin: finite differences (BVP)
import numpy as np
import matplotlib.pyplot as plt

k = 237.0           # thermal conductivity of pure aluminum, W/(m K)
d, L = 0.003, 0.10  # fin diameter and length, m
h = 30.0            # convection coefficient, W/(m^2 K)
t_base, t_air = 80.0, 25.0          # base, air temperature, deg C
m = np.sqrt(4 * h / (k * d))        # fin parameter, 1/m
area = np.pi * d**2 / 4             # cross-section area, m^2


def fin_fd(n):
    """Solve for theta = T - T_air on n + 1 nodes."""
    dx = L / n
    a, b = np.zeros((n + 1, n + 1)), np.zeros(n + 1)
    a[0, 0], b[0] = 1.0, t_base - t_air     # base: T fixed
    for i in range(1, n):                   # interior nodes
        a[i, i - 1:i + 2] = [1.0, -(2 + (m * dx)**2), 1.0]
    a[n, n - 1] = 2.0                       # convective tip
    a[n, n] = -(2 + (m * dx)**2 + 2 * h * dx / k)
    return np.linspace(0.0, L, n + 1), np.linalg.solve(a, b)


mL, hk = m * L, h / (m * k)
q_exact = (np.sqrt(h * np.pi * d * k * area) * (t_base - t_air)
           * (np.sinh(mL) + hk * np.cosh(mL))
           / (np.cosh(mL) + hk * np.sinh(mL)))
print(f'm L = {mL:.4f}   exact q = {q_exact:.5f} W')
print('   n   T_tip (C)   q_fin (W)   error in q (W)')
for n in [5, 10, 20, 40]:
    x, th = fin_fd(n)
    dx = L / n                          # heat flow in at the base
    q = -k * area * (-3 * th[0] + 4 * th[1] - th[2]) / (2 * dx)
    err = q - q_exact
    print(f'{n:4d} {th[-1] + t_air:11.3f} {q:11.5f} {err:13.2e}')
plt.plot(100 * x, th + t_air, 'o-')
plt.xlabel('Distance from the base x (cm)')
plt.ylabel('Fin temperature T (°C)')
plt.show()
