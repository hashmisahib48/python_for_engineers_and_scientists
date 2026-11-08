# Problem 4.4  How long is the uniform-field zone of a solenoid?
import math

MU0 = 1.25663706212e-6   # vacuum permeability, N/A^2 (CODATA 2018)
I = 2.0              # current, A
R = 0.050            # coil radius, m
L = 0.500            # coil length, m
N_TURNS = 500        # number of turns
DZ = 0.001           # step along the axis, m
LIMIT = 0.99         # uniform means B >= 99 % of the center value

b_center = 0.0
print(' z (mm)   B (mT)   B/B_center')
for step in range(1000):                 # z from 0 to 1 m
    z = step * DZ                        # point on the axis, m
    b = 0.0                              # field accumulator, T
    for k in range(N_TURNS):
        z_k = -L / 2 + (k + 0.5) * L / N_TURNS   # turn k, m
        d = z - z_k
        b += MU0 * I * R**2 / (2 * (R**2 + d**2)**1.5)
    if step == 0:
        b_center = b
    if step % 25 == 0:
        print(f'{z * 1e3:7.0f} {b * 1e3:8.4f} {b / b_center:11.4f}')
    if b < LIMIT * b_center:
        print(f'B falls below {LIMIT:.0%} at z = {z * 1e3:.0f} mm')
        print(f'Uniform zone: {2 * (z - DZ) * 1e3:.0f} mm long, '
              f'{2 * (z - DZ) / L:.0%} of the coil')
        break
else:
    print('B stayed uniform over the whole range tested')
n = N_TURNS / L                          # turns per meter
b_long = MU0 * n * I                     # ideal long solenoid, T
b_finite = b_long * (L / 2) / math.sqrt(R**2 + (L / 2)**2)
print(f'Center, sum of loops:  {b_center * 1e3:.5f} mT')
print(f'Center, finite coil:   {b_finite * 1e3:.5f} mT')
print(f'Ideal long solenoid:   {b_long * 1e3:.5f} mT')
