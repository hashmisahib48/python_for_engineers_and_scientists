# Example 10.3  Electric field lines of a dipole
import numpy as np
import matplotlib.pyplot as plt

eps0 = 8.8541878128e-12        # vacuum permittivity, F/m
k = 1 / (4 * np.pi * eps0)     # Coulomb constant, N m^2/C^2
q, d = 1e-9, 0.020             # charge, C; separation, m
charges = [(q, -d / 2), (-q, d / 2)]      # (charge, x position)

def field(x, y):
    """E components (V/m) and potential (V) at points x, y (m)."""
    ex, ey, pot = 0.0, 0.0, 0.0
    for qi, xi in charges:
        r = np.hypot(x - xi, y)
        ex = ex + k * qi * (x - xi) / r**3
        ey = ey + k * qi * y / r**3
        pot = pot + k * qi / r
    return ex, ey, pot

ex, ey, pot = field(0.0, 0.030)
print(f'E at (0, 30 mm): Ex = {ex:.1f} V/m, Ey = {ey:.1f} V/m')
print(f'Point-dipole estimate: {k * q * d / 0.030**3:.1f} V/m')

x = np.linspace(-0.05, 0.05, 200)              # m, misses charges
X, Y = np.meshgrid(x, x)
Ex, Ey, V = field(X, Y)
E = np.hypot(Ex, Ey)

fig, ax = plt.subplots(figsize=(5.2, 4.2))
ax.contour(X * 1e3, Y * 1e3, V, levels=np.linspace(-300, 300, 13),
           cmap='RdBu_r', linewidths=0.8)
sp = ax.streamplot(X * 1e3, Y * 1e3, Ex, Ey, color=np.log10(E),
                   cmap='viridis', density=1.4, linewidth=0.8)
fig.colorbar(sp.lines, ax=ax, label=r'$\log_{10}|E|$ (V/m)')
ax.plot(-10, 0, 'o', color='red', ms=9)
ax.plot(10, 0, 'o', color='blue', ms=9)
ax.set_aspect('equal')
ax.set_xlabel('$x$ (mm)')
ax.set_ylabel('$y$ (mm)')
plt.show()
