# Thermal shock of a thick steel wall: explicit FTCS scheme
import math
import numpy as np
import matplotlib.pyplot as plt

k, rho, cp = 60.5, 7854.0, 434.0   # plain carbon steel, SI units
alpha = k / (rho * cp)             # thermal diffusivity, m^2/s
L = 0.20                           # wall thickness, m
t_hot, t_cold = 290.0, 50.0        # initial and inner-face temp, C
nx = 81                            # number of nodes
dx = L / (nx - 1)                  # node spacing, m
r = 0.4                            # r = alpha dt / dx^2
dt = r * dx**2 / alpha             # time step, s
n_steps = round(120.0 / dt)        # march for two minutes

x = np.linspace(0.0, L, nx)
temp = np.full(nx, t_hot)
temp[0] = t_cold                   # cold water on the inner face
for n in range(n_steps):
    new = temp.copy()
    new[1:-1] = temp[1:-1] + r * (temp[2:] - 2 * temp[1:-1]
                                  + temp[:-2])
    new[-1] = temp[-1] + 2 * r * (temp[-2] - temp[-1])  # insulated
    temp = new

t_end = n_steps * dt
print(f'alpha = {alpha:.3e} m^2/s, dt = {dt:.3f} s, r = {r}')
print(f'Temperatures (deg C) after {t_end:.1f} s:')
for xi in [0.005, 0.01, 0.02, 0.05, 0.10, 0.20]:
    i = round(xi / dx)
    semi = t_cold + (t_hot - t_cold) * math.erf(
        xi / (2 * math.sqrt(alpha * t_end)))
    print(f'  x = {xi:5.3f} m: {temp[i]:9.5g}  semi-inf {semi:.2f}')
plt.plot(100 * x, temp)
plt.xlabel('Depth below the inner face x (cm)')
plt.ylabel('Temperature T (°C)')
plt.show()
