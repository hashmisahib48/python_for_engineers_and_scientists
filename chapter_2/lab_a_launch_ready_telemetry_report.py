# Lab  A launch-ready telemetry report from one raw downlink frame
import math

GAMMA = 1.4             # ratio of specific heats of air
R_AIR = 287.053         # specific gas constant of air, J/(kg K)
G0 = 9.80665            # standard gravity, m/s^2

frame = ('SR-7  T+0042.50 ALT 012345.6 VEL +0412.3 ACC -0011.8 '
         'PRS 019.40 TMP -056.5 BAT 27.6')
status = '  Guidance=nominal  Recovery=armed \n'

vehicle = frame[0:4]
t = float(frame[8:15])            # time since liftoff, s
alt = float(frame[20:28])         # altitude, m
vel = float(frame[33:40])         # vertical velocity, m/s
acc = float(frame[45:52])         # acceleration, m/s^2
p = float(frame[57:63]) * 1000    # static pressure, Pa
t_air = float(frame[68:74])       # air temperature, deg C
v_bat = float(frame[79:83])       # battery voltage, V

a_snd = math.sqrt(GAMMA * R_AIR * (t_air + 273.15))   # m/s
mach = vel / a_snd
q = 0.5 * GAMMA * p * mach**2     # dynamic pressure, Pa
s = status.strip().lower()
k = s.find('recovery=') + len('recovery=')

title = f'{vehicle} TELEMETRY   T+{t:.2f} s'
print('=' * 44)
print(f'{title:^44}')
print('=' * 44)
print(f'{"Altitude":<24}{alt:>12,.1f}  m')
print(f'{"":<24}{alt / 0.3048:>12,.0f}  ft')
print(f'{"Vertical velocity":<24}{vel:>12.1f}  m/s')
print(f'{"Mach number":<24}{mach:>12.3f}')
print(f'{"Acceleration":<24}{acc / G0:>+12.2f}  g')
print(f'{"Dynamic pressure":<24}{q / 1000:>12.1f}  kPa')
print(f'{"Air temperature":<24}{t_air:>+12.1f}  °C')
print(f'{"Battery":<24}{v_bat:>12.1f}  V')
print('Recovery system', s[k:].upper(), sep=' ..... ')
print('=' * 44)
