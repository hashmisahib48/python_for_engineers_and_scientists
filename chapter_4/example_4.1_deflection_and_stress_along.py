# Example 4.1  Deflection and stress along a loaded cantilever
P = 5000.0           # tip load, N
L = 2.0              # span, m
E = 200e9            # Young's modulus of steel, Pa
B = 0.060            # section width, m
H = 0.120            # section depth, m
N = 8                # number of intervals along the beam

I = B * H**3 / 12                    # second moment of area, m^4
dx = L / N                           # station spacing, m
print('  x (m)   v (mm)   slope (mrad)   sigma (MPa)')
for k in range(N + 1):
    x = k * dx                                    # station, m
    v = P * x**2 * (3 * L - x) / (6 * E * I)      # deflection, m
    theta = P * x * (2 * L - x) / (2 * E * I)     # slope, rad
    m = P * (L - x)                               # moment, N m
    sigma = m * (H / 2) / I                       # stress, Pa
    print(f'{x:7.2f} {v * 1e3:8.3f} {theta * 1e3:12.3f}'
          f' {sigma / 1e6:13.1f}')

v_allow = L / 250                    # serviceability limit, m
print(f'Tip deflection limit L/250: {v_allow * 1e3:.3f} mm')
if v <= v_allow:
    print('Deflection check: OK')
else:
    print('Deflection check: TOO FLEXIBLE')
