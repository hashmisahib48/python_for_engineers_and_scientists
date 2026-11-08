# Problem 14.1  Electric field in layered insulation by FEM
import numpy as np
from fem1d import bar_k, assemble, solve_fixed

EPS0 = 8.8541878128e-12               # F/m, CODATA 2018
V0 = 8.0e3                            # applied voltage, V
names = ['Mylar', 'air void', 'Pyrex']
eps_r = np.array([3.2, 1.00059, 5.6])          # rel. permittivity
t = np.array([0.5e-3, 0.1e-3, 2.0e-3])          # thickness, m
E_max = np.array([7e6, 3e6, 14e6])              # strength, V/m

n = len(t)
# eps/t plays the role of EA/L, per square meter of electrode
k_list = [bar_k(EPS0 * eps_r[e], 1.0, t[e]) for e in range(n)]
K = assemble(n + 1, [(e, e + 1) for e in range(n)], k_list)
V, q = solve_fixed(K, np.zeros(n + 1), fixed=[0, n],
                   values=[V0, 0.0])           # q: charge, C/m^2

print('Interface potentials (kV):', np.round(V / 1e3, 3))
for e in range(n):
    field = (V[e] - V[e + 1]) / t[e]           # V/m
    use = field / E_max[e]
    flag = 'BREAKDOWN' if use >= 1 else 'ok'
    print(f'{names[e]:9s}: E = {field / 1e6:6.2f} MV/m, '
          f'{use:5.0%} of strength  {flag}')
C_fem = q[0] / V0                               # F/m^2
C_series = EPS0 / np.sum(t / eps_r)
print(f'Capacitance: FEM {C_fem * 1e9:.4f} nF/m^2, '
      f'series formula {C_series * 1e9:.4f} nF/m^2')
