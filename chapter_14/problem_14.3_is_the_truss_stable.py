# Problem 14.3  Is a truss stable? Ask the eigenvalues of K
import numpy as np
from truss2d import assemble

nodes = np.array([[0.0, 0.0], [0.0, 1.5], [2.0, 0.0],
                  [2.0, 1.5], [4.0, 0.0], [4.0, 1.5]])   # m
base = [(0, 2), (2, 4), (1, 3), (3, 5), (2, 3), (4, 5), (1, 2)]
E, A = 207e9, 400e-6             # steel, Pa; member area, m^2
free = np.arange(4, 12)          # nodes 0 and 1 are pinned


def check(members):
    """Eigenvalues (N/m) and zero-energy modes of K_ff."""
    K = assemble(nodes, members, E, np.full(len(members), A))
    lam, vec = np.linalg.eigh(K[np.ix_(free, free)])
    zero = lam < 1e-9 * lam.max()
    return lam, vec[:, zero]


lam, modes = check(base)
print(f'Original truss: {modes.shape[1]} mechanism(s)')
print('Smallest eigenvalues (MN/m):', np.round(lam[:3] / 1e6, 3))
mode = modes[:, 0] / np.abs(modes[:, 0]).max()
mode = np.round(mode, 3) + 0.0          # no '-0.00'
for k in range(len(free) // 2):
    print(f'  node {k + 2}: dx = {mode[2 * k]:5.2f}, '
          f'dy = {mode[2 * k + 1]:5.2f}')
for extra in [(0, 3), (3, 4), (2, 5)]:
    lam, modes = check(base + [extra])
    print(f'Add member {extra}: {modes.shape[1]} mechanism(s), '
          f'smallest eigenvalue {lam[0]:.3e} N/m')
