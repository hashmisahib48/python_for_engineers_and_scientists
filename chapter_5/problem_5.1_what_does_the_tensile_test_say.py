# Problem 5.1  Properties from a tensile test of 6061-T6
strain = [0.0, 0.058, 0.116, 0.174, 0.232, 0.290, 0.337,
          0.385, 0.443, 0.515, 0.600, 0.730, 0.928, 1.170,
          1.434, 1.687, 2.5, 4.0, 6.0, 8.0, 10.0, 11.5,
          12.2]                                  # percent
stress = [0.0, 40.0, 80.0, 120.0, 160.0, 200.0, 230.0,
          250.0, 262.0, 270.0, 276.0, 282.0, 288.0, 293.0,
          297.0, 300.0, 304.0, 309.0, 312.0, 313.0, 306.0,
          290.0, 262.0]                          # MPa
eps = [e / 100 for e in strain]                  # strain, m/m

# (a) modulus: mean of stress/strain for 0 < stress <= 200 MPa
ratios = [s / e for e, s in zip(eps, stress) if 0 < s <= 200]
e_mod = sum(ratios) / len(ratios)                # MPa

# (b) 0.2 % offset yield: g = stress - E (eps - 0.002) turns < 0
g = [s - e_mod * (e - 0.002) for e, s in zip(eps, stress)]
for k in range(1, len(g)):
    if g[k] < 0:
        w = g[k - 1] / (g[k - 1] - g[k])         # 0 ... 1
        s_y = stress[k - 1] + w * (stress[k] - stress[k - 1])
        break

# (c) ultimate strength and (d) elongation after fracture
s_u = max(stress)
k_u = stress.index(s_u)
elong = eps[-1] - stress[-1] / e_mod             # elastic part off

print(f'Points: {len(stress)}, used for E: {len(ratios)}')
print(f'Young\'s modulus  E    = {e_mod / 1e3:.1f} GPa')
print(f'0.2 % yield      s_y  = {s_y:.1f} MPa')
print(f'Ultimate         s_u  = {s_u:.1f} MPa at {strain[k_u]} %')
print(f'Elongation at fracture = {elong:.1%}')
print(f'Yield ratio s_y/s_u   = {s_y / s_u:.3f}')
