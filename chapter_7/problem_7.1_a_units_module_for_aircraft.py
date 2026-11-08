# Problem 7.1  An aircraft specification converted to SI
from pathlib import Path
from units import to_si, G0

spec = {}
for line in Path('jet_spec.txt').read_text().splitlines():
    if line.startswith('#'):
        continue
    name, value, unit = line.split()
    try:
        spec[name] = to_si(float(value), unit)
    except ValueError as err:
        print(f'{name}: not converted, {err}')

for name, value in spec.items():
    print(f'{name:14} {value:12.5g}')
weight = spec['mtow'] * G0                         # N
print(f'Wing loading W/S: {weight / spec["wing_area"]:.0f} Pa')
print(f'Thrust-to-weight: {2 * spec["thrust_engine"] / weight:.3f}')
hours = spec['range'] / spec['cruise_speed'] / 3600
print(f'Time at cruise speed: {hours:.2f} h')
