# Example 14.4  A cantilever beam meshed with CST elements
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import spsolve
from cst import d_matrix, b_matrix, assemble

E, nu = 207e9, 0.30              # steel: Pa, Poisson's ratio
Lb, h, t = 1.0, 0.10, 0.01       # length, depth, thickness, m
P, nx, ny = 1000.0, 40, 8        # tip load, N; cells along, across
D = d_matrix(E, nu)
I, G = t * h**3 / 12, E / (2 * (1 + nu))      # m^4, Pa
d_beam = P * Lb**3 / (3 * E * I) + P * Lb / (5 / 6 * G * t * h)
nodes = np.array([[x, y] for x in np.linspace(0, Lb, nx + 1)
                  for y in np.linspace(-h / 2, h / 2, ny + 1)])
c = np.arange(nx * (ny + 1)).reshape(nx, ny + 1)[:, :-1].ravel()
a, b = c + ny + 1, c + ny + 2           # other corners of each cell
tris = np.vstack([np.column_stack([c, a, b]),
                  np.column_stack([c, b, c + 1])])
F = np.zeros(2 * len(nodes))
tip = np.arange(nx * (ny + 1), len(nodes))
F[2 * tip + 1] = -P / ny                # shear load on the tip
F[2 * tip[[0, -1]] + 1] = -P / (2 * ny)
free = np.arange(2 * (ny + 1), len(F))  # nodes at x = 0 clamped
K = assemble(nodes, tris, D, t)
u = np.zeros(len(F))
u[free] = spsolve(K[free][:, free], F[free])
d_tip = -u[2 * (nx * (ny + 1) + ny // 2) + 1]   # mid-depth, m
print(f'{len(u)} DOF: tip deflection CST {d_tip * 1e3:.4f} mm, '
      f'beam {d_beam * 1e3:.4f} mm')
s_x = np.array([D[0] @ b_matrix(nodes[tr])[0]
                @ u[np.column_stack([2 * tr, 2 * tr + 1]).ravel()]
                for tr in tris])          # bending stress, Pa
cen = nodes[tris].mean(axis=1)          # element centroids, m
k = np.argmin(np.hypot(cen[:, 0] - Lb / 2, cen[:, 1] - h / 2))
s_beam = P * (Lb - cen[k, 0]) * cen[k, 1] / I       # M y / I, Pa
print(f'Mid-span, top: CST {s_x[k] / 1e6:.2f} MPa, '
      f'beam {s_beam / 1e6:.2f} MPa')
xy = nodes + 20 * u.reshape(-1, 2)      # deformation x 20
plt.tripcolor(xy[:, 0], xy[:, 1], tris, s_x / 1e6, cmap='RdBu_r')
plt.colorbar(label='σx (MPa)'); plt.xlabel('x (m)'); plt.show()
