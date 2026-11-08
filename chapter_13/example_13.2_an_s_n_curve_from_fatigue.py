# Example 13.2  Basquin S-N curve from fully reversed fatigue tests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = pd.read_csv('fatigue_sn.csv')        # MPa, cycles to failure
s_a = df['stress_amp_MPa'].to_numpy()
log_n = np.log10(df['cycles'].to_numpy())

def log_life(s_a, sf, b):
    """log10 of cycles to failure; s_a and sf in MPa."""
    return np.log10(0.5 * (s_a / sf)**(1 / b))

p, cov = curve_fit(log_life, s_a, log_n, p0=[1000.0, -0.1])
sf, b = p
u_sf, u_b = np.sqrt(np.diag(cov))         # standard errors
print(f"sigma_f' = {sf:.0f} +/- {u_sf:.0f} MPa")
print(f"b        = {b:.4f} +/- {u_b:.4f}")
resid = log_n - log_life(s_a, sf, b)
s_log = np.sqrt(np.sum(resid**2) / (len(s_a) - 2))
print(f'scatter in log10 N: s = {s_log:.3f}')
s_des = 320.0                             # design amplitude, MPa
n_med = 10**log_life(s_des, sf, b)
n_low = n_med / 10**(2 * s_log)           # median - 2s curve
print(f'at {s_des:.0f} MPa: median life {n_med:.3e} cycles')
print(f'           design life {n_low:.3e} cycles')

n = np.logspace(3, 7, 100)
fig, ax = plt.subplots(figsize=(5.0, 3.0))
ax.loglog(df['cycles'], s_a, 'o', label='tests')
ax.loglog(n, sf * (2 * n)**b, label='Basquin fit')
n_d = n / 10**(2 * s_log)                 # design curve, cycles
ax.loglog(n_d, sf * (2 * n)**b, '--', label='design')
ax.set(xlabel='Cycles to failure N',
       ylabel='Stress amplitude (MPa)')
ax.set_yticks([250, 300, 400, 500], ['250', '300', '400', '500'])
ax.set_yticks([], minor=True)
ax.legend()
plt.show()
