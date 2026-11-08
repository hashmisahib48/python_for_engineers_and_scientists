# Example 3.3  Speed of sound and flight regime (ISA)
import math

GAMMA = 1.4           # ratio of specific heats of air, -
R_AIR = 287.053       # gas constant of air, J/(kg K)
h = 10668.0           # geopotential altitude, m (35 000 ft)
v = 250.0             # true airspeed, m/s

if h < 0 or h > 20000:
    print('Altitude outside the model (0 to 20 km)')
else:
    if h <= 11000:
        t_air = 288.15 - 0.0065 * h       # troposphere, K
    else:
        t_air = 216.65                    # lower stratosphere, K
    a = math.sqrt(GAMMA * R_AIR * t_air)  # speed of sound, m/s
    mach = v / a
    if mach < 0.8:
        regime = 'subsonic'
    elif mach < 1.2:
        regime = 'transonic'
    elif mach < 5.0:
        regime = 'supersonic'
    else:
        regime = 'hypersonic'
    print(f'Air temperature: {t_air:.2f} K '
          f'({t_air - 273.15:.2f} degC)')
    print(f'Speed of sound: {a:.1f} m/s')
    print(f'Mach number: {mach:.3f}')
    print(f'Flight regime: {regime}')
