# Example 11.3  Velocity, deceleration and drag from tracking data
import numpy as np

G = 9.80665              # standard gravity, m/s^2
M = 50.0                 # probe mass, kg
D = 0.8                  # probe diameter, m
RHO = 1.2                # air density, kg/m^3
AREA = np.pi * D**2 / 4  # frontal area, m^2

t, y = np.loadtxt('drop_track.csv', delimiter=',', skiprows=1,
                  unpack=True)                 # s, m
v = np.gradient(y, t)                          # velocity, m/s
a = np.gradient(v, t)                          # acceleration, m/s^2
drag = M * (G + a)                             # upward drag, N
cd = 2 * drag / (RHO * AREA * v**2)            # drag coefficient

print('  t (s)   y (m)    v (m/s)   a (m/s^2)    Cd')
for k in [2, 4, 8, 12, 16, 20, 24]:
    print(f'{t[k]:6.1f} {y[k]:8.1f} {v[k]:9.2f} {a[k]:10.3f}'
          f' {cd[k]:8.3f}')

late = t >= 4.0                                # well-developed drag
cd_mean = cd[late].mean()
print(f'Mean Cd for t >= 4 s: {cd_mean:.3f} '
      f'(std {cd[late].std():.3f}, {late.sum()} samples)')
v_term = np.sqrt(2 * M * G / (RHO * AREA * cd_mean))
print(f'Predicted terminal speed: {v_term:.2f} m/s')
