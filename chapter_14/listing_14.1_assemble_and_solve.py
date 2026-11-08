# Section 14.1  Three springs hold two masses between two walls
import numpy as np

k1, k2, k3 = 40.0e3, 25.0e3, 50.0e3   # spring rates, N/m
P1, P2 = 600.0, -200.0                # loads on nodes 1 and 2, N

# global stiffness matrix, built one spring at a time
one = np.array([[1.0, -1.0], [-1.0, 1.0]])
K = np.zeros((4, 4))
K[0:2, 0:2] += k1 * one             # spring 1 joins nodes 0, 1
K[1:3, 1:3] += k2 * one             # spring 2 joins nodes 1, 2
K[2:4, 2:4] += k3 * one             # spring 3 joins nodes 2, 3
print('K (kN/m) =')
print(K / 1000)

F = np.array([0.0, P1, P2, 0.0])    # nodal forces, N
# nodes 0 and 3 are fixed: solve for the free nodes 1 and 2
u = np.zeros(4)                     # nodal displacements, m
u[1:3] = np.linalg.solve(K[1:3, 1:3], F[1:3])
R = K @ u - F                       # reactions at the walls, N
print(f'u = {u * 1000} mm')
print(f'Reactions = {R} N')
print(f'Sum of reactions and loads = {R.sum() + P1 + P2:.1e} N')
