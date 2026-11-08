# Example 9.4: principal stresses from a 3-D stress tensor
import numpy as np
np.set_printoptions(precision=4, suppress=True)

SIG_Y = 250.0                          # yield strength, MPa
s = np.array([[ 80.0,  30.0, -20.0],   # stress tensor, MPa
              [ 30.0, -40.0,  10.0],
              [-20.0,  10.0,  25.0]])
vals, vecs = np.linalg.eigh(s)   # ascending eigenvalues
sig = vals[::-1]                 # sigma_1 >= sigma_2 >= sigma_3
n = vecs[:, ::-1]                # matching directions (columns)
tau_max = (sig[0] - sig[2]) / 2                         # MPa
d = np.array([sig[0] - sig[1], sig[1] - sig[2], sig[2] - sig[0]])
vm = np.sqrt((d**2).sum() / 2)                          # MPa

print(f'Principal stresses (MPa): {sig}')
print('Principal directions (columns n1, n2, n3):')
print(n)
print(f'Maximum shear stress: {tau_max:.2f} MPa')
print(f'Von Mises stress: {vm:.2f} MPa, '
      f'safety factor {SIG_Y / vm:.2f}')
print(f'Trace: {np.trace(s):.2f} = sum {sig.sum():.2f}')
print(f'Det:   {np.linalg.det(s):.1f} = product {sig.prod():.1f}')
print('Rotated to principal axes, n.T @ s @ n:')
print(n.T @ s @ n)
