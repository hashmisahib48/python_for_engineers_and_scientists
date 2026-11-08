# Problem 10.3  Steady temperature field in a square plate
import numpy as np
import matplotlib.pyplot as plt

L = 0.40                        # side of the square plate, m
T1, T2 = 20.0, 120.0            # cold edges and hot top edge, degC
x = np.linspace(0.0, L, 81)     # m
X, Y = np.meshgrid(x, x)

theta = np.zeros_like(X)        # dimensionless temperature
for n in range(1, 100, 2):      # only odd n contribute
    theta += (4 / (np.pi * n) * np.sin(n * np.pi * X / L)
              * np.sinh(n * np.pi * Y / L) / np.sinh(n * np.pi))
T = T1 + (T2 - T1) * theta      # degC
T[-1, :] = T2                   # impose the hot edge exactly
print(f'Center: {T[40, 40]:.2f} degC')
print(f'Quarter height, mid-width: {T[20, 40]:.2f} degC')

fig = plt.figure(figsize=(6.6, 3.0))
ax1 = fig.add_subplot(1, 2, 1)
levels = np.linspace(20.0, 120.0, 11)
cf = ax1.contourf(X * 100, Y * 100, T, levels, cmap='inferno')
cs = ax1.contour(X * 100, Y * 100, T, levels=levels[1:-1],
                 colors='white', linewidths=0.6)
ax1.clabel(cs, fmt='%.0f', fontsize=9)
ax1.set(xlabel='$x$ (cm)', ylabel='$y$ (cm)', aspect='equal')

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot_surface(X * 100, Y * 100, T, cmap='inferno', vmin=20,
                 vmax=120, rstride=2, cstride=2, linewidth=0)
ax2.set(xlabel='$x$ (cm)', ylabel='$y$ (cm)', zlim=(20.0, 120.0))
ax2.view_init(elev=25, azim=-125)
fig.colorbar(cf, ax=[ax1, ax2], label='$T$ (°C)', shrink=0.8)
plt.show()
