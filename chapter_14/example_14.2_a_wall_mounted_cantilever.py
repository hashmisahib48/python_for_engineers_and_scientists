# Example 14.2  A wall-mounted cantilever truss
import numpy as np
import matplotlib.pyplot as plt
from truss2d import assemble, member_forces
from fem1d import solve_fixed

nodes = np.array([[0.0, 0.0], [0.0, 1.5], [2.0, 0.0],
                  [2.0, 1.5], [4.0, 0.0]])         # m
members = [(0, 2), (2, 4), (1, 3), (3, 4), (2, 3), (1, 2)]
E = 207e9                            # steel, Pa
A = np.full(len(members), 400e-6)    # member areas, m^2
F = np.zeros(2 * len(nodes))
F[2 * 4 + 1] = -10e3                 # 10 kN down at node 4, N

K = assemble(nodes, members, E, A)
u, R = solve_fixed(K, F, fixed=[0, 1, 2, 3], values=0.0)
N = member_forces(nodes, members, E, A, u)

for m, (i, j) in enumerate(members):
    print(f'Member {i}-{j}: N = {N[m] / 1e3:7.2f} kN, '
          f'stress = {N[m] / A[m] / 1e6:6.1f} MPa')
print(f'Tip deflection: {u[9] * 1e3:.3f} mm')
print(f'Wall reactions (kN): {np.round(R[:4] / 1e3, 2)}')

scale = 100                          # magnify the displacements
xy = nodes + scale * u.reshape(-1, 2)
for m, (i, j) in enumerate(members):
    plt.plot(nodes[[i, j], 0], nodes[[i, j], 1], 'k:', lw=1)
    color = '#D93636' if N[m] > 0 else '#1E78D2'
    plt.plot(xy[[i, j], 0], xy[[i, j], 1], color, lw=2.5)
plt.axis('equal')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title(f'Deformed shape x {scale} (red: tension)')
plt.show()
