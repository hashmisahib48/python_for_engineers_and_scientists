# Section 14.5  A tapered bar with many elements, solved sparse
import time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

E, P, L = 69e9, 5.0e3, 0.40    # aluminum, Pa; load, N; length, m
r1, r2 = 0.010, 0.004              # end radii, m


def tip_displacement(n):
    """Tip displacement of the cone with n bar elements, m."""
    x = np.linspace(0.0, L, n + 1)
    r_mid = r1 + (r2 - r1) * (x[:-1] + x[1:]) / (2 * L)
    k = E * np.pi * r_mid**2 / np.diff(x)       # N/m
    e = np.arange(n)                             # element numbers
    rows = np.concatenate([e, e, e + 1, e + 1])
    cols = np.concatenate([e, e + 1, e, e + 1])
    vals = np.concatenate([k, -k, -k, k])
    K = coo_matrix((vals, (rows, cols))).tocsr()
    F = np.zeros(n + 1)
    F[-1] = P
    u = spsolve(K[1:, 1:], F[1:])               # node 0 fixed
    return u[-1]


exact = P * L / (E * np.pi * r1 * r2)
print(f'Exact tip displacement: {exact * 1e3:.6f} mm')
for n in [10, 100, 1000, 100_000]:
    t0 = time.perf_counter()
    d = tip_displacement(n)
    dt = time.perf_counter() - t0
    err = abs(d - exact) / exact
    print(f'n = {n:6d}: {d * 1e3:.6f} mm, error {err:.1e}, '
          f'{dt * 1e3:.1f} ms')
