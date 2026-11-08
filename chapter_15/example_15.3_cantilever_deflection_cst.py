# Example 15.3: CST cantilever against beam theory, mesh study
import numpy as np
import matplotlib.pyplot as plt
from cst_beam import cantilever

L, h, t = 0.50, 0.05, 0.01        # length, depth, thickness, m
E, nu, P = 200e9, 0.30, 1000.0    # steel, Pa, -, tip load N
Iz = t * h**3 / 12                 # second moment of area, m^4
G = E / (2 * (1 + nu))            # shear modulus, Pa
d_eb = P * L**3 / (3 * E * Iz)              # Euler-Bernoulli, m
d_tim = d_eb + P * L / (5 / 6 * G * h * t)  # plus shear, m
print(f'Euler-Bernoulli {d_eb * 1e3:.4f} mm, '
      f'Timoshenko {d_tim * 1e3:.4f} mm')

ndof, ratio = [], []
for nx, ny in [(10, 2), (20, 4), (40, 8), (80, 16), (160, 32)]:
    xy, u = cantilever(nx, ny, L, h, t, E, nu, P)
    tip = -u[2 * ((ny // 2) * (nx + 1) + nx) + 1]   # mid-depth, m
    ndof.append(u.size)
    ratio.append(tip / d_tim)
    print(f'{nx:4d} x {ny:2d}  {u.size:6d} dof  '
          f'tip {tip * 1e3:.4f} mm  FE/Tim {tip / d_tim:.4f}')

plt.figure(figsize=(5, 2.6))
plt.semilogx(ndof, ratio, 'o-')
plt.axhline(1.0, color='gray', ls='--')
plt.xlabel('Degrees of freedom')
plt.ylabel('FE / Timoshenko tip deflection')
plt.show()
