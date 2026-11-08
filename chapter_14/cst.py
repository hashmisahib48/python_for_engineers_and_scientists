"""cst.py  Constant-strain triangles, plane stress (Chapter 14)."""
import numpy as np
from scipy.sparse import coo_matrix


def d_matrix(E, nu):
    """Plane-stress elasticity matrix, Pa."""
    return E / (1 - nu**2) * np.array([[1, nu, 0], [nu, 1, 0],
                                       [0, 0, (1 - nu) / 2]])


def b_matrix(xy):
    """Strain-displacement matrix B (1/m) and area (m^2)."""
    x, y = xy[:, 0], xy[:, 1]
    b = np.array([y[1] - y[2], y[2] - y[0], y[0] - y[1]])
    c = np.array([x[2] - x[1], x[0] - x[2], x[1] - x[0]])
    area = 0.5 * (b[0] * c[1] - b[1] * c[0])
    B = np.zeros((3, 6))
    B[0, 0::2], B[1, 1::2] = b, c
    B[2, 0::2], B[2, 1::2] = c, b
    return B / (2 * area), area


def assemble(nodes, tris, D, t):
    """Sparse global stiffness matrix of a CST mesh, N/m."""
    rows, cols, vals = [], [], []
    for tri in tris:
        B, area = b_matrix(nodes[tri])
        ke = t * area * B.T @ D @ B
        dofs = np.column_stack([2 * tri, 2 * tri + 1]).ravel()
        rows.append(np.repeat(dofs, 6))
        cols.append(np.tile(dofs, 6))
        vals.append(ke.ravel())
    n = 2 * len(nodes)
    rows, cols = np.concatenate(rows), np.concatenate(cols)
    vals = np.concatenate(vals)
    return coo_matrix((vals, (rows, cols)), shape=(n, n)).tocsr()
