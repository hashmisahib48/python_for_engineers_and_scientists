# Example 5.3  Lightest material for a tension tie rod
import math

# E (Pa), rho (kg/m^3), yield strength sy (Pa)
materials = {
    'Steel 1020': {'E': 207e9, 'rho': 7850.0, 'sy': 210e6},
    'Steel 4340': {'E': 207e9, 'rho': 7850.0, 'sy': 1620e6},
    'Al 6061-T6': {'E': 69e9, 'rho': 2700.0, 'sy': 276e6},
    'Al 7075-T6': {'E': 71e9, 'rho': 2800.0, 'sy': 503e6},
    'Ti-6Al-4V': {'E': 114e9, 'rho': 4430.0, 'sy': 1103e6},
    'Mg AZ31B': {'E': 45e9, 'rho': 1770.0, 'sy': 220e6},
}
force = 50e3          # axial load, N
length = 1.2          # rod length, m
fs = 1.5              # factor of safety on yield
stretch = 1.0e-3      # allowed elongation, m

ranking = []
for name, p in materials.items():
    a_str = fs * force / p['sy']                   # m^2
    a_stiff = force * length / (p['E'] * stretch)  # m^2
    if a_str > a_stiff:
        area, rule = a_str, 'strength'
    else:
        area, rule = a_stiff, 'stiffness'
    mass = p['rho'] * area * length                # kg
    ranking.append((mass, name, area, rule))

ranking.sort()
print('Material      mass (kg)  d (mm)  governed by')
for mass, name, area, rule in ranking:
    d = 1000 * math.sqrt(4 * area / math.pi)       # mm
    print(f'{name:<12}{mass:9.3f}{d:9.1f}   {rule}')
best_mass, best_name, best_area, best_rule = ranking[0]
print(f'Lightest: {best_name}, {best_mass:.2f} kg')
