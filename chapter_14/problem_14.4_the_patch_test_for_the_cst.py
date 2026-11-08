# Problem 14.4  The MacNeal-Harder patch test for the CST
import numpy as np
from scipy.sparse.linalg import spsolve
from cst import d_matrix, b_matrix, assemble

E, nu, t = 1.0e6, 0.25, 0.001     # test values, consistent units
nodes = np.array([[0.0, 0.0], [0.24, 0.0], [0.24, 0.12],
                  [0.0, 0.12], [0.04, 0.02], [0.18, 0.03],
                  [0.16, 0.08], [0.08, 0.08]])
quads = [(0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7),
         (4, 5, 6, 7)]                     # counterclockwise
tris = np.array([[a, b, c] for a, b, c, d in quads]
                + [[a, c, d] for a, b, c, d in quads])
D = d_matrix(E, nu)
K = assemble(nodes, tris, D, t)

x, y = nodes[:, 0], nodes[:, 1]
u_exact = np.column_stack([1e-3 * (x + y / 2),
                           1e-3 * (y + x / 2)]).ravel()
fixed = np.arange(8)                       # DOFs of nodes 0-3
free = np.arange(8, 16)                    # DOFs of nodes 4-7
u = np.zeros(16)
u[fixed] = u_exact[fixed]
rhs = -K[free][:, fixed] @ u[fixed]        # no loads inside
u[free] = spsolve(K[free][:, free], rhs)

print(f'Largest displacement error: '
      f'{np.abs(u - u_exact).max():.2e}')
S, areas = np.zeros((len(tris), 3)), np.zeros(len(tris))
for e, tri in enumerate(tris):
    dofs = np.column_stack([2 * tri, 2 * tri + 1]).ravel()
    B, areas[e] = b_matrix(nodes[tri])
    S[e] = D @ B @ u[dofs]                 # [sx, sy, txy]
print(f'{len(tris)} triangles, areas {areas.min():.4f} to '
      f'{areas.max():.4f}, total {areas.sum():.4f}')
print('Smallest stresses:', np.round(S.min(axis=0), 6))
print('Largest stresses: ', np.round(S.max(axis=0), 6))
