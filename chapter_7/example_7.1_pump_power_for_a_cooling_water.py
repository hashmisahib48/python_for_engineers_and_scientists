# Example 7.1  Pump power for a three-section cooling-water line
import math
import fluids
from fluids import RHO_WATER, G

q = 2.5e-3          # volume flow rate, m^3/s
rough = 0.045e-3    # roughness of commercial steel, m
dz = 6.0            # height the water is lifted, m
eta_pump = 0.70     # pump efficiency, -
# (name, inner diameter in m, length in m) of each section
sections = [('header', 0.050, 12.0), ('main', 0.040, 25.0),
            ('branch', 0.032, 8.0)]

dp_fric = 0.0
print('Section  D (mm)  V (m/s)      Re  dp (kPa)')
for name, d, length in sections:
    v = q / (math.pi * d**2 / 4)                 # mean speed, m/s
    re = fluids.reynolds(v, d)
    dp = fluids.pressure_drop(v, d, length, rough)
    dp_fric += dp
    print(f'{name:8}{d*1000:6.0f}{v:9.2f}{re:9.0f}{dp/1e3:9.2f}')

dp_lift = RHO_WATER * G * dz              # static lift, Pa
dp_pump = dp_fric + dp_lift               # rise the pump gives, Pa
power = q * dp_pump / eta_pump            # shaft power, W
print(f'Friction loss: {dp_fric / 1e3:.1f} kPa')
print(f'Static lift:   {dp_lift / 1e3:.1f} kPa')
print(f'Pump head:     {dp_pump / (RHO_WATER * G):.1f} m')
print(f'Shaft power:   {power:.0f} W')
