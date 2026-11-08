# Listing 4.3  Mass of a tapered wind-turbine tower, slice by slice
import math

H = 80.0             # tower height, m
D_BASE = 4.0         # outer diameter at the base, m
D_TOP = 2.5          # outer diameter at the top, m
T_WALL = 0.020       # wall thickness, m
RHO = 7850.0         # density of steel, kg/m^3
N_SLICES = 8         # number of slices

dz = H / N_SLICES                    # slice height, m
mass = 0.0                           # accumulator, kg
for k in range(N_SLICES):
    z_mid = (k + 0.5) * dz           # height of slice center, m
    d = D_BASE + (D_TOP - D_BASE) * z_mid / H
    area = math.pi * T_WALL * (d - T_WALL)   # wall area, m^2
    mass += RHO * area * dz
print(f'Slices: {N_SLICES}, each {dz:.1f} m high')
print(f'Tower shell mass: {mass / 1000:.2f} t')
