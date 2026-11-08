# Problem 9.1: exit Mach number of a rocket nozzle
import numpy as np

G = 1.2                # ratio of specific heats, -
R = 355.0              # gas constant of the exhaust, J/(kg K)
T0, P0 = 3200.0, 7.0e6  # chamber temperature K, pressure Pa
EPS = 8.0              # nozzle area ratio A_e / A*

m = np.linspace(0.05, 5.0, 99_001)          # Mach numbers, -
tr = 1 + (G - 1) / 2 * m**2                 # T0 / T
ar = (2 / (G + 1) * tr)**((G + 1) / (2 * (G - 1))) / m   # A / A*

sup = m > 1.0                               # supersonic branch
k = np.abs(ar[sup] - EPS).argmin()
m_e = m[sup][k]
t_e = T0 / tr[sup][k]                       # exit temperature, K
p_e = P0 * tr[sup][k]**(-G / (G - 1))       # exit pressure, Pa
v_e = m_e * np.sqrt(G * R * t_e)            # exit velocity, m/s

print(f'Smallest A/A* on the grid: {ar.min():.6f} '
      f'at M = {m[ar.argmin()]:.3f}')
print(f'Subsonic M for A/A* = {EPS}: '
      f'{m[~sup][np.abs(ar[~sup] - EPS).argmin()]:.4f}')
print(f'Exit Mach number: {m_e:.4f} (A/A* = {ar[sup][k]:.5f})')
print(f'Exit temperature: {t_e:.1f} K')
print(f'Exit pressure: {p_e / 1e3:.1f} kPa')
print(f'Exit velocity: {v_e:.0f} m/s')
