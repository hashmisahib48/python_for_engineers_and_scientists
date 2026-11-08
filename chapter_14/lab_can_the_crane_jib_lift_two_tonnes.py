# Engineering Lab  A 24 m crane jib as a plane truss
import numpy as np
import matplotlib.pyplot as plt
from truss2d import assemble, member_forces
from fem1d import solve_fixed

n_bay, bay, depth = 12, 2.0, 1.5      # bays; bay length, depth, m
E, rho, g = 207e9, 7850.0, 9.81       # steel: Pa, kg/m^3; m/s^2
m_load, s_yield = 2000.0, 250e6       # payload, kg; yield, Pa
A_chord, A_web = 3000e-6, 800e-6      # member areas, m^2

# node 2i is on the bottom chord, node 2i+1 on the top chord
nodes = np.array([[bay * i, depth * k] for i in range(n_bay + 1)
                  for k in range(2)])
members, A = [], []
for b in range(0, 2 * n_bay, 2):          # b: bottom node of a bay
    members += [(b, b + 2), (b + 1, b + 3),     # two chords
                (b + 2, b + 3), (b + 1, b + 2)]  # web members
    A += [A_chord, A_chord, A_web, A_web]
A = np.array(A)
L = np.array([np.hypot(*(nodes[j] - nodes[i])) for i, j in members])
F = np.zeros(2 * len(nodes))              # nodal forces, N
for m, (i, j) in enumerate(members):      # self-weight to both ends
    F[[2 * i + 1, 2 * j + 1]] -= rho * g * A[m] * L[m] / 2
tip = 2 * n_bay                           # bottom node at the tip
F[2 * tip + 1] -= m_load * g              # payload, N
K = assemble(nodes, members, E, A)
u, R = solve_fixed(K, F, fixed=[0, 1, 2, 3], values=0.0)
s = member_forces(nodes, members, E, A, u) / A     # stress, Pa

print(f'Jib mass: {rho * A @ L:.0f} kg')
print(f'Tip deflection: {-u[2 * tip + 1] * 1e3:.1f} mm')
for m in [s.argmax(), s.argmin()]:
    print(f'Member {members[m]}: stress {s[m] / 1e6:.1f} MPa')
print(f'Safety factor on yield: {s_yield / abs(s).max():.2f}')
xy = nodes + 10 * u.reshape(-1, 2)        # deformation x 10
for m, (i, j) in enumerate(members):
    c = plt.cm.coolwarm(0.5 + s[m] / (2 * abs(s).max()))
    plt.plot(xy[[i, j], 0], xy[[i, j], 1], color=c, lw=2)
plt.axis('scaled'); plt.xlabel('x (m)'); plt.show()
