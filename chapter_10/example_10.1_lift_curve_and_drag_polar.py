# Example 10.1  Lift curve and drag polar of a finite wing
import numpy as np
import matplotlib.pyplot as plt

AR, e = 8.0, 0.85          # aspect ratio, span efficiency factor
cd0 = 0.020                # zero-lift drag coefficient
alpha0 = -2.0              # zero-lift angle of attack, deg
k = np.pi * e * AR
a_deg = 2 * np.pi / (1 + 2 * np.pi / k) * np.pi / 180   # 1/deg

alpha = np.linspace(-6.0, 12.0, 100)               # deg
cl = a_deg * (alpha - alpha0)
cd = cd0 + cl**2 / k
# simulated tunnel readings, uncertainty CL +-0.02, CD +-0.002
a_m = np.array([-4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 8.0, 10.0])
cl_m = np.array([-0.186, -0.011, 0.158, 0.343, 0.505, 0.680,
                 0.860, 1.030])
cd_m = np.array([0.0216, 0.0197, 0.0209, 0.0248, 0.0318,
                 0.0414, 0.0520, 0.0661])

cl_s = np.sqrt(cd0 * k)                # C_L at the best L/D
print(f'Lift slope: {a_deg:.4f} per degree')
print(f'Best L/D = {cl_s / (2 * cd0):.2f} at CL = {cl_s:.3f}')
print(f'  angle of attack {alpha0 + cl_s / a_deg:.2f} deg')
print(f'Best measured L/D = {np.max(cl_m / cd_m):.2f}')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4, 3.0))
ax1.plot(alpha, cl, label='theory')
ax1.errorbar(a_m, cl_m, yerr=0.02, fmt='o', ms=4, capsize=2,
             label='tunnel')
ax1.set_xlabel(r'Angle of attack $\alpha$ (deg)')
ax1.set_ylabel('Lift coefficient $C_L$')
ax1.legend()
ax2.plot(cd, cl)
ax2.errorbar(cd_m, cl_m, xerr=0.002, fmt='o', ms=4, capsize=2)
ax2.plot([0.0, 2 * cd0], [0.0, cl_s], '--', color='gray')
ax2.scatter(2 * cd0, cl_s, s=70, marker='D', color='C2', zorder=3)
ax2.set_xlabel('Drag coefficient $C_D$')
fig.tight_layout()
plt.show()
