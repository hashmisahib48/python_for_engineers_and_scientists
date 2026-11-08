# Problem 12.4: bound states of an electron in a GaAs quantum well
import numpy as np
from scipy.optimize import brentq

HBAR, M_E = 1.054571817e-34, 9.1093837015e-31   # J s, kg
EV = 1.602176634e-19        # J per eV (CODATA 2018)
m_eff = 0.067 * M_E         # effective mass in GaAs, kg
a, v0 = 10e-9, 0.30         # well width m, barrier height eV


def fd_levels(nw):          # bound-state energies (eV), nw points
    dx, n = a / nw, 6 * nw                         # m; domain 6a
    x = (np.arange(n) - (n - 1) / 2) * dx          # psi = 0 beyond
    v = np.where(np.abs(x) < a / 2, 0.0, v0) * EV  # potential, J
    c = HBAR**2 / (2 * m_eff * dx**2)              # J
    off = np.diag(-c * np.ones(n - 1), 1)          # above diagonal
    ham = np.diag(2 * c + v) + off + off.T
    e = np.sort(np.linalg.eigvals(ham).real) / EV
    return e[e < v0]


def mismatch(e, even):      # zero when psi joins smoothly at a/2
    k = np.sqrt(2 * m_eff * e * EV) / HBAR
    kap = np.sqrt(2 * m_eff * (v0 - e) * EV) / HBAR
    z = k * a / 2
    if even:
        return k * np.sin(z) - kap * np.cos(z)
    return k * np.cos(z) + kap * np.sin(z)


for nw in [20, 40, 80]:
    levels = [f'{1000 * e:8.3f}' for e in fd_levels(nw)]
    print(f'nw = {nw:2d}:', ' '.join(levels), 'meV')
for j, e in enumerate(fd_levels(80)):
    e_ex = brentq(mismatch, 0.95 * e, min(1.05 * e, v0 - 1e-9),
                  args=(j % 2 == 0,))
    print(f'level {j + 1}: exact {1000 * e_ex:8.3f} meV')
