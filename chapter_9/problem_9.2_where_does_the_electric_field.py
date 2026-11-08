# Problem 9.2: where does the electric field of two charges vanish?
import numpy as np

K_E = 8.9875517923e9                  # Coulomb constant, N m^2/C^2
q = np.array([4.0e-9, 1.0e-9])        # charges, C
xq = np.array([0.0, 0.30])            # charge positions x, m
yq = np.array([0.0, 0.0])             # charge positions y, m

x = np.linspace(-0.0995, 0.3995, 500)  # grid, m (misses charges)
y = np.linspace(-0.1495, 0.1495, 300)
xx, yy = np.meshgrid(x, y)            # each (300, 500)

# (2, 1, 1) charge data against (300, 500) grid -> (2, 300, 500)
dx = xx - xq[:, np.newaxis, np.newaxis]
dy = yy - yq[:, np.newaxis, np.newaxis]
r3 = np.hypot(dx, dy)**3
kq = K_E * q[:, np.newaxis, np.newaxis]
ex = (kq * dx / r3).sum(axis=0)       # superposition, V/m
ey = (kq * dy / r3).sum(axis=0)
e_mag = np.hypot(ex, ey)

i, j = np.unravel_index(e_mag.argmin(), e_mag.shape)
x0 = 0.30 / (1 + np.sqrt(q[1] / q[0]))    # exact, on the axis
print(f'Field array: {e_mag.shape}, {e_mag.size} points')
print(f'Weakest field: {e_mag[i, j]:.2f} V/m '
      f'at x = {x[j]:.4f} m, y = {y[i]:.4f} m')
print(f'Exact null on the axis: x = {x0:.4f} m')
print(f'Field 5 cm away, (x0, 0.05): '
      f'{e_mag[np.abs(y - 0.05).argmin(), j]:.0f} V/m')
print(f'Median field on the grid: {np.median(e_mag):.0f} V/m')
