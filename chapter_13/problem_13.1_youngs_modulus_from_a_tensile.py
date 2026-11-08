# Problem 13.1  Young's modulus and 0.2 % offset yield of 6061-T6
import numpy as np
import pandas as pd

df = pd.read_csv('tensile_6061.csv')      # strain (-), stress MPa
el = df[(df['stress_MPa'] >= 20) & (df['stress_MPa'] <= 150)]
x = el['strain'].to_numpy()
y = el['stress_MPa'].to_numpy()

p, cov = np.polyfit(x, y, 1, cov=True)    # y = E x + c
E, u_E = p[0], np.sqrt(cov[0, 0])
ss_res = np.sum((y - np.polyval(p, x))**2)
r2 = 1 - ss_res / np.sum((y - y.mean())**2)
print(f'points in elastic fit: {len(x)}')
print(f'E = {E / 1000:.2f} +/- {u_E / 1000:.2f} GPa')
print(f'R^2 = {r2:.5f}')

# 0.2 % offset line: stress = E (strain - 0.002)
eps = df['strain'].to_numpy()
sig = df['stress_MPa'].to_numpy()
g = sig - E * (eps - 0.002)               # > 0 left of the crossing
k = np.argmax(g < 0)                      # first point past it
f = g[k - 1] / (g[k - 1] - g[k])          # linear interpolation
s_y = sig[k - 1] + f * (sig[k] - sig[k - 1])
print(f'0.2 % offset yield strength = {s_y:.1f} MPa')
