# Engineering Lab  Choosing a ceramic you can trust
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from weibull_tools import rank_prob, weibull_fit, p_fail

S_DESIGN = 400.0          # peak stress in the rotor, MPa
PF_MAX = 1e-4             # allowed probability of fracture

df = pd.read_csv('bend_tests.csv')
df['strength'] = 30 * df['load_N'] / (df['b_mm'] * df['d_mm']**2)
summary = df.groupby('supplier')['strength'].agg(['mean', 'std'])
print(summary.round(1))

stress = np.linspace(300, 1000, 300)      # MPa, for the curves
fig, ax = plt.subplots(figsize=(5.0, 3.1))
for name, grp in df.groupby('supplier'):
    s = np.sort(grp['strength'].to_numpy())
    m, s0 = weibull_fit(s)
    pf = p_fail(S_DESIGN, m, s0)
    verdict = 'PASS' if pf <= PF_MAX else 'FAIL'
    print(f'{name}: m = {m:5.2f}  s0 = {s0:.0f} MPa  '
          f'P_f = {pf:.1e}  {verdict}')
    ax.semilogy(s, rank_prob(len(s)), 'o', ms=3.5,
                label=f'supplier {name}, m = {m:.1f}')
    ax.semilogy(stress, p_fail(stress, m, s0), lw=1.2,
                color=ax.lines[-1].get_color())  # same color

ax.axhline(PF_MAX, color='red', ls='--', lw=0.9)
ax.axvline(S_DESIGN, color='grey', ls=':', lw=0.9)
ax.set_ylim(1e-7, 1)
ax.set_xlabel('Stress (MPa)')
ax.set_ylabel('Probability of fracture')
ax.legend(loc='lower right')
plt.show()
