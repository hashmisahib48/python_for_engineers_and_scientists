# Example 13.3  Weibull modulus of silicon nitride, supplier A
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from weibull_tools import rank_prob, weibull_fit, p_fail

df = pd.read_csv('bend_tests.csv')
# four-point bend strength, MPa (spans 40 and 20 mm)
df['strength'] = 30 * df['load_N'] / (df['b_mm'] * df['d_mm']**2)
s = np.sort(df.loc[df['supplier'] == 'A', 'strength'].to_numpy())

m, s0 = weibull_fit(s)
print(f'n = {len(s)}, mean strength = {s.mean():.0f} MPa')
print(f'Weibull modulus m = {m:.2f}')
print(f'characteristic strength s0 = {s0:.0f} MPa')
c_ml, loc, s0_ml = stats.weibull_min.fit(s, floc=0)
print(f'max. likelihood: m = {c_ml:.2f}, s0 = {s0_ml:.0f} MPa')
for stress in (400.0, 600.0, 800.0):      # MPa
    print(f'P_f at {stress:.0f} MPa = {p_fail(stress, m, s0):.4f}')

x = np.log(s)
y = np.log(-np.log(1 - rank_prob(len(s))))
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.plot(x, y, 'o', label='30 bars, supplier A')
ax.plot(x, m * (x - np.log(s0)), label=f'fit, m = {m:.1f}')
ax.set_xlabel('ln(strength / MPa)')
ax.set_ylabel('ln ln(1/(1 - F))')
ax.legend()
plt.show()
