# Write a standard-atmosphere table to a text file, then read it
from pathlib import Path

T0, P0, LAPSE = 288.15, 101325.0, 0.0065   # K, Pa, K/m
G0, R_AIR = 9.80665, 287.053               # m/s^2, J/(kg K)
path = Path('isa_table.txt')

with open(path, 'w', encoding='utf-8') as f:
    f.write('# ISA troposphere\n')
    f.write('#  h (m)    T (K)     p (Pa)  rho (kg/m^3)\n')
    for h in range(0, 11001, 1000):
        t = T0 - LAPSE * h
        p = P0 * (t / T0)**(G0 / (LAPSE * R_AIR))
        rho = p / (R_AIR * t)
        f.write(f'{h:8d} {t:8.2f} {p:10.1f} {rho:10.4f}\n')
print(f'Wrote {path.name}, exists: {path.exists()}')

rows = []
with open(path, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'):
            continue                       # skip comment lines
        h, t, p, rho = [float(x) for x in line.split()]
        rows.append((h, t, p, rho))
print(f'Read {len(rows)} rows from {path.name}')
h, t, p, rho = rows[-1]
print(f'At {h:.0f} m: T = {t:.2f} K, rho = {rho:.4f} kg/m^3')
print(f'Density ratio to sea level: {rho / rows[0][3]:.3f}')
