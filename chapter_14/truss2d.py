"""truss2d.py  Plane truss elements (Chapter 14)."""
import numpy as np


def truss_k(E, A, xy_i, xy_j):
    """4 x 4 global stiffness matrix of one truss member, N/m."""
    dx, dy = xy_j - xy_i
    L = np.hypot(dx, dy)
    c, s = dx / L, dy / L
    t = np.array([-c, -s, c, s])
    return E * A / L * np.outer(t, t)


def assemble(nodes, members, E, A):
    """Global K; node n owns DOFs 2n (x) and 2n+1 (y).
    A holds the cross-section area of every member, m^2."""
    n_dof = 2 * len(nodes)
    K = np.zeros((n_dof, n_dof))
    for m, (i, j) in enumerate(members):
        dofs = [2 * i, 2 * i + 1, 2 * j, 2 * j + 1]
        ke = truss_k(E, A[m], nodes[i], nodes[j])
        K[np.ix_(dofs, dofs)] += ke
    return K


def member_forces(nodes, members, E, A, u):
    """Axial force in every member, N (tension > 0)."""
    N = np.zeros(len(members))
    for m, (i, j) in enumerate(members):
        dx, dy = nodes[j] - nodes[i]
        L = np.hypot(dx, dy)
        c, s = dx / L, dy / L
        du = u[2 * j:2 * j + 2] - u[2 * i:2 * i + 2]
        N[m] = E * A[m] / L * (c * du[0] + s * du[1])
    return N
