# Problem 10.2  Mohr's circle for a state of plane stress
import numpy as np
import matplotlib.pyplot as plt

sx, sy, txy = 80.0, -40.0, 50.0      # stresses, MPa
c = (sx + sy) / 2                    # center of the circle, MPa
r = np.hypot((sx - sy) / 2, txy)     # radius = max shear, MPa
s1, s2 = c + r, c - r                # principal stresses, MPa
tp = 0.5 * np.degrees(np.arctan2(2 * txy, sx - sy))   # deg
print(f'sigma_1 = {s1:.2f} MPa, sigma_2 = {s2:.2f} MPa')
print(f'tau_max = {r:.2f} MPa, theta_p = {tp:.2f} deg')
ev = np.linalg.eigvalsh(np.array([[sx, txy], [txy, sy]]))
print('Eigenvalues of the stress matrix:', np.round(ev, 2))

phi = np.linspace(0.0, 2 * np.pi, 361)
fig, ax = plt.subplots(figsize=(4.6, 3.7))
ax.plot(c + r * np.cos(phi), r * np.sin(phi))
ax.plot([sx, sy], [txy, -txy], 'o-', color='C1')
ax.plot([s1, s2], [0.0, 0.0], 's', color='C3')
ax.annotate(f'X ({sx:.0f}, {txy:.0f})', (sx, txy),
            xytext=(8, 6), textcoords='offset points')
ax.annotate(f'Y ({sy:.0f}, {-txy:.0f})', (sy, -txy),
            xytext=(10, -4), textcoords='offset points')
ax.annotate(rf'$\sigma_1$ = {s1:.1f}', (s1, 0.0),
            xytext=(-62, 8), textcoords='offset points')
ax.annotate(rf'$\sigma_2$ = {s2:.1f}', (s2, 0.0),
            xytext=(4, 10), textcoords='offset points')
ax.axhline(0.0, color='gray', linewidth=0.8)
ax.set(xlabel=r'Normal stress $\sigma$ (MPa)', aspect='equal',
       ylabel=r'Shear stress $\tau$ (MPa)')
plt.show()
