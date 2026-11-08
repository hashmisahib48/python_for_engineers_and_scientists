# Problem 12.3: how deep does the frost reach? FTCS in soil
import math
import numpy as np
from scipy.optimize import brentq

alpha = 0.52 / (2050.0 * 1840.0)   # soil: k/(rho cp), m^2/s
t_soil, t_surf = 10.0, -15.0       # initial and surface temp, C
depth, nx = 4.0, 81                # domain depth m, nodes
dx = depth / (nx - 1)              # node spacing, m
r = 0.45                           # stability needs r <= 1/2
dt = r * dx**2 / alpha             # time step, s
day = 86400.0                      # s

x = np.linspace(0.0, depth, nx)
temp = np.full(nx, t_soil)
temp[0] = t_surf                   # sudden cold snap at t = 0
t = 0.0
print(f'dt = {dt / 3600:.2f} h')
print(' days   frost depth (m)   erf solution (m)')
for days in [15, 30, 60, 90]:
    while t < days * day - dt / 2:
        temp[1:-1] = temp[1:-1] + r * (temp[2:] - 2 * temp[1:-1]
                                       + temp[:-2])
        t = t + dt
    i = np.argmax(temp > 0.0)                 # first node above 0 C
    x0 = np.interp(0.0, temp[i - 1:i + 1], x[i - 1:i + 1])
    eta = brentq(lambda z: math.erf(z) - (0 - t_surf)
                 / (t_soil - t_surf), 0.0, 3.0)
    x_ex = 2 * eta * math.sqrt(alpha * t)
    print(f'{t / day:5.1f} {x0:13.3f} {x_ex:17.3f}')
