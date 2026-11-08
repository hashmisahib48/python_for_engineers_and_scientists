# Engineering Lab  Wind flowing past a cylindrical mast
import numpy as np
import matplotlib.pyplot as plt

U, R = 20.0, 0.15            # wind speed, m/s; mast radius, m
rho = 1.225                  # air density (ISA sea level), kg/m^3
q = 0.5 * rho * U**2         # dynamic pressure, Pa

x = np.linspace(-0.6, 0.6, 240)              # m (never 0)
y = np.linspace(-0.35, 0.35, 140)            # m
X, Y = np.meshgrid(x, y)
r2 = X**2 + Y**2
u = U * (1 - R**2 * (X**2 - Y**2) / r2**2)   # m/s
v = -2 * U * R**2 * X * Y / r2**2            # m/s
inside = r2 < R**2
u[inside], v[inside] = 0.0, 0.0              # no flow in the mast
cp = 1 - (u**2 + v**2) / U**2                # pressure coefficient

theta = np.linspace(0.0, 180.0, 361)         # surface angle, deg
v_s = 2 * U * np.sin(np.radians(theta))      # surface speed, m/s
cp_s = 1 - (v_s / U)**2
j = np.argmin(cp_s)
print(f'Top speed {v_s[j]:.1f} m/s at {theta[j]:.0f} deg')
print(f'Cp min = {cp_s[j]:.2f}, p - p_inf = {cp_s[j] * q:.0f} Pa')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5.6, 4.7),
                               height_ratios=[1.3, 1])
cf = ax1.contourf(X, Y, cp, levels=np.linspace(-3, 1, 17),
                  cmap='RdBu_r', vmin=-3.0, vmax=3.0)
fig.colorbar(cf, ax=ax1, label='$C_p$')
ax1.streamplot(X, Y, u, v, color='k', density=1.2, linewidth=0.6)
ax1.add_patch(plt.Circle((0, 0), R, color='gray'))
ax1.set(xlabel='$x$ (m)', ylabel='$y$ (m)', aspect='equal')
ax2.plot(theta, cp_s)
ax2.set(xlabel=r'Angle from the front $\theta$ (deg)',
        ylabel='Surface $C_p$', xticks=np.arange(0, 181, 30))
fig.tight_layout()
fig.savefig('mast_flow.png', dpi=300)
fig.savefig('mast_flow.pdf')
plt.show()
