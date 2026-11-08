# Example 14.1  Stepped bar between two rigid walls
import numpy as np
from fem1d import bar_k, assemble, solve_fixed

E = np.array([69e9, 69e9, 207e9])         # Young's modulus, Pa
A = np.array([900e-6, 600e-6, 300e-6])    # area, m^2
L = np.array([0.25, 0.20, 0.30])          # length, m
elements = [(0, 1), (1, 2), (2, 3)]       # node pairs
F = np.array([0.0, 60e3, -20e3, 0.0])     # nodal loads, N

k_list = [bar_k(E[e], A[e], L[e]) for e in range(3)]
K = assemble(4, elements, k_list)
u, R = solve_fixed(K, F, fixed=[0, 3], values=[0.0, 0.0])

# element results: strain from the end displacements
for e, (i, j) in enumerate(elements):
    strain = (u[j] - u[i]) / L[e]
    stress = E[e] * strain                 # Pa
    force = stress * A[e]                  # N, tension > 0
    print(f'Element {e}: N = {force / 1e3:7.2f} kN, '
          f'stress = {stress / 1e6:7.2f} MPa')
print('Displacements (mm):', np.round(u * 1e3, 4))
print(f'Reactions: left {R[0] / 1e3:.2f} kN, '
      f'right {R[3] / 1e3:.2f} kN')
