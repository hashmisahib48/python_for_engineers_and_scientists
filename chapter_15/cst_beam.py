# CST plane-stress model of a cantilever (module for Example 15.3)
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve


def cantilever(nx, ny, L, h, t, E, nu, P):
    """Clamp x = 0, push end x = L down with P; return xy, u (m)."""
    x, y = np.meshgrid(np.linspace(0, L, nx + 1),
                       np.linspace(-h / 2, h / 2, ny + 1))
    xy = np.column_stack([x.ravel(), y.ravel()])
    nd = np.arange(len(xy)).reshape(ny + 1, nx + 1)   # node numbers
    tri = []
    for j in range(ny):
        for i in range(nx):
            a, c = nd[j, i], nd[j + 1, i + 1]
            tri += [(a, a + 1, c), (a, c, c - 1)]
    D = E / (1 - nu**2) * np.array([[1, nu, 0], [nu, 1, 0],
                                    [0, 0, (1 - nu) / 2]])
    rows, cols, vals = [], [], []
    for e in tri:
        (x1, y1), (x2, y2), (x3, y3) = xy[list(e)]
        area = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
        bi = [y2 - y3, y3 - y1, y1 - y2]          # shape-function
        ci = [x3 - x2, x1 - x3, x2 - x1]          # derivatives
        B = np.zeros((3, 6))
        B[0, 0::2], B[1, 1::2] = bi, ci
        B[2, 0::2], B[2, 1::2] = ci, bi
        ke = t * area * (B.T @ D @ B) / (2 * area)**2
        dof = np.ravel([[2 * k, 2 * k + 1] for k in e])
        rows += list(np.repeat(dof, 6))
        cols += list(np.tile(dof, 6))
        vals += list(ke.ravel())
    n = 2 * len(xy)
    K = coo_matrix((vals, (rows, cols)), shape=(n, n)).tocsr()
    u, f = np.zeros(n), np.zeros(n)
    f[2 * nd[:, -1] + 1] = -P / (ny + 1)       # end load, N
    free = np.ravel([[2 * k, 2 * k + 1] for k in nd[:, 1:].ravel()])
    u[free] = spsolve(K[free][:, free], f[free])
    return xy, u
