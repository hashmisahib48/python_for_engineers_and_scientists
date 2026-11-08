# Listing 10.6  Velocity field of a Rankine vortex (tornado model)
import numpy as np
import matplotlib.pyplot as plt

a = 50.0                         # core radius, m
v_max = 60.0                     # peak speed at r = a, m/s
gamma = 2 * np.pi * a * v_max    # circulation, m^2/s

x = np.linspace(-200.0, 200.0, 81)            # m
X, Y = np.meshgrid(x, x)                      # 81 x 81 grid
r = np.hypot(X, Y) + 1e-9                     # radius, m (never 0)
v_th = np.where(r < a, gamma * r / (2 * np.pi * a**2),
                gamma / (2 * np.pi * r))      # swirl speed, m/s
u = -v_th * Y / r                             # x component, m/s
v = v_th * X / r                              # y component, m/s
print(f'Circulation {gamma:.0f} m^2/s')
print(f'Speed 150 m from the axis: {gamma / (2*np.pi*150):.1f} m/s')

fig, ax = plt.subplots(figsize=(4.6, 3.6))
cf = ax.contourf(X, Y, v_th, levels=12, cmap='viridis')
fig.colorbar(cf, ax=ax, label='Speed (m/s)')
s = slice(None, None, 6)                      # every sixth point
ax.quiver(X[s, s], Y[s, s], u[s, s], v[s, s], color='white')
ax.set_aspect('equal')
ax.set_xlabel('$x$ (m)')
ax.set_ylabel('$y$ (m)')
plt.show()
