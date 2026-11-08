# Listing 10.8  A Gaussian laser beam as an image and a surface
import numpy as np
import matplotlib.pyplot as plt

P = 5e-3                      # beam power, W
w = 1.0e-3                    # beam radius (1/e^2 intensity), m
I0 = 2 * P / (np.pi * w**2)   # peak intensity, W/m^2

x = np.linspace(-2.5e-3, 2.5e-3, 151)            # m
X, Y = np.meshgrid(x, x)
I = I0 * np.exp(-2 * (X**2 + Y**2) / w**2)       # W/m^2
dA = (x[1] - x[0])**2                            # cell area, m^2
print(f'Peak intensity: {I0:.0f} W/m^2')
print(f'Power summed over the grid: {I.sum() * dA * 1e3:.3f} mW')

fig = plt.figure(figsize=(6.6, 3.0))
ax1 = fig.add_subplot(1, 2, 1)
im = ax1.imshow(I, extent=[-2.5, 2.5, -2.5, 2.5], origin='lower',
                cmap='inferno')
fig.colorbar(im, ax=ax1, label='$I$ (W/m$^2$)')
ax1.set_xlabel('$x$ (mm)')
ax1.set_ylabel('$y$ (mm)')

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot_surface(X * 1e3, Y * 1e3, I, cmap='inferno',
                 rstride=5, cstride=5, linewidth=0)
ax2.set_xlabel('$x$ (mm)')
ax2.set_ylabel('$y$ (mm)')
ax2.set_zlabel('$I$ (W/m$^2$)')
ax2.view_init(elev=30, azim=-60)
plt.show()
