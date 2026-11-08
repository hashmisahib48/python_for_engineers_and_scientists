# Example 14.3  Heat loss from an aluminum pin fin by FEM
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

k, h = 237.0, 100.0              # W/(m K), W/(m^2 K)
D, L = 0.005, 0.050              # diameter, length, m
T_b, T_inf = 100.0, 25.0         # base and air temperature, C
A, P = np.pi * D**2 / 4, np.pi * D          # m^2, m
n = 8                                       # number of elements

x = np.linspace(0.0, L, n + 1)
le = L / n                                  # element length, m
ke = (k * A / le * np.array([[1, -1], [-1, 1]])
      + h * P * le / 6 * np.array([[2, 1], [1, 2]]))
fe = h * P * T_inf * le / 2                 # W at each node
e = np.arange(n)
rows = np.concatenate([e, e, e + 1, e + 1])
cols = np.concatenate([e, e + 1, e, e + 1])
vals = np.repeat([ke[0, 0], ke[0, 1], ke[1, 0], ke[1, 1]], n)
K = coo_matrix((vals, (rows, cols))).tocsr()
F = np.full(n + 1, 2 * fe)                  # nodal heat input, W
F[[0, -1]] = fe                             # end nodes: one element
T = np.zeros(n + 1)
T[0] = T_b                                  # base temperature fixed
T[1:] = spsolve(K[1:, 1:], (F - K @ T)[1:])
q_fem = (K @ T - F)[0]                      # heat into the base, W

m = np.sqrt(h * P / (k * A))                # fin parameter, 1/m
q_ex = np.sqrt(h * P * k * A) * (T_b - T_inf) * np.tanh(m * L)
T_tip = T_inf + (T_b - T_inf) / np.cosh(m * L)
print(f'Tip temperature: FEM {T[-1]:.3f} C, exact {T_tip:.3f} C')
print(f'Heat rate: FEM {q_fem:.4f} W, exact {q_ex:.4f} W')
xs = np.linspace(0.0, L, 200)
T_ex = T_inf + (T_b - T_inf) * np.cosh(m * (L - xs)) / np.cosh(m*L)
plt.plot(xs * 1e3, T_ex, 'k-', lw=1, label='exact')
plt.plot(x * 1e3, T, 'o', label=f'FEM, {n} elements')
plt.xlabel('x (mm)'); plt.ylabel('T (°C)'); plt.legend()
plt.show()
