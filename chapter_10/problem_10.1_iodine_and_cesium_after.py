# Problem 10.1  Decay of I-131 and Cs-137 on linear and log axes
import numpy as np
import matplotlib.pyplot as plt

T_I = 8.0252                   # half-life of I-131, days
T_Cs = 30.08 * 365.25          # half-life of Cs-137, days
A_I0, A_Cs0 = 10.0, 1.0        # initial activities, relative
lam_I, lam_Cs = np.log(2) / T_I, np.log(2) / T_Cs   # 1/day

t = np.linspace(0.0, 200.0, 401)                  # time, days
A_I = A_I0 * np.exp(-lam_I * t)
A_Cs = A_Cs0 * np.exp(-lam_Cs * t)
t_x = np.log(A_I0 / A_Cs0) / (lam_I - lam_Cs)     # crossover, days
print(f'Equal activities after {t_x:.1f} days')
print(f'I-131 down by 1000 after {np.log(1000) / lam_I:.1f} days')
print(f'Cs-137 left after 200 days: {A_Cs[-1] / A_Cs0:.4f}')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4, 2.8))
for ax in (ax1, ax2):
    ax.plot(t, A_I, label='I-131')
    ax.plot(t, A_Cs, label='Cs-137')
    ax.plot(t, A_I + A_Cs, 'k:', label='total')
    ax.axvline(t_x, color='gray', linewidth=0.8)
    ax.set_xlabel('Time (days)')
ax1.set(ylabel='Activity (relative)', title='Linear axes')
ax2.set(yscale='log', title='Logarithmic $y$ axis')
ax2.legend()
fig.tight_layout()
plt.show()
