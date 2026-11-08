"""fem1d.py  Two-node elements for 1-D problems (Chapter 14)."""
import numpy as np


def bar_k(E, A, L):
    """Stiffness matrix of a two-node bar, N/m."""
    k = E * A / L
    return k * np.array([[1.0, -1.0], [-1.0, 1.0]])


def assemble(n_nodes, elements, k_list):
    """Add every element matrix into the global matrix K."""
    K = np.zeros((n_nodes, n_nodes))
    for (i, j), ke in zip(elements, k_list):
        dofs = [i, j]
        K[np.ix_(dofs, dofs)] += ke
    return K


def solve_fixed(K, F, fixed, values):
    """Solve K u = F with u[fixed] = values prescribed.
    Return the full solution u and the reactions R = K u - F."""
    n = len(F)
    u = np.zeros(n)
    u[fixed] = values
    free = np.setdiff1d(np.arange(n), fixed)
    rhs = F[free] - K[np.ix_(free, fixed)] @ u[fixed]
    u[free] = np.linalg.solve(K[np.ix_(free, free)], rhs)
    R = K @ u - F
    return u, R
