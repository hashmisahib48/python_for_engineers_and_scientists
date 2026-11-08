# Example 13.1  Steinhart-Hart calibration of an NTC thermistor
import numpy as np
import pandas as pd

cal = pd.read_csv('thermistor_cal.csv')  # T_C in degC, R_ohm in ohm
t_k = cal['T_C'].to_numpy() + 273.15     # bath temperature, K
ln_r = np.log(cal['R_ohm'].to_numpy())

# model 1/T = A + B ln R + C (ln R)^3 is linear in A, B, C
X = np.column_stack([np.ones(len(ln_r)), ln_r, ln_r**3])
coef = np.linalg.lstsq(X, 1 / t_k, rcond=None)[0]
a, b, c = coef
print(f'A = {a:.6e} 1/K')
print(f'B = {b:.6e} 1/K')
print(f'C = {c:.6e} 1/K')

res_mk = (t_k - 1 / (X @ coef)) * 1000   # residuals, mK
print(f'rms residual = {np.sqrt(np.mean(res_mk**2)):.1f} mK')
print(f'max residual = {np.max(np.abs(res_mk)):.1f} mK')

# simpler beta model, 1/T = A + B ln R (drop the cubic column)
coef2 = np.linalg.lstsq(X[:, :2], 1 / t_k, rcond=None)[0]
res2 = (t_k - 1 / (X[:, :2] @ coef2)) * 1000
print(f'beta model: beta = {1 / coef2[1]:.0f} K, '
      f'max residual = {np.max(np.abs(res2)):.0f} mK')

r_read = 7500.0                          # a reading, ohm
lr = np.log(r_read)
t_read = 1 / (a + b * lr + c * lr**3) - 273.15
print(f'R = {r_read:.0f} ohm  ->  T = {t_read:.3f} degC')
