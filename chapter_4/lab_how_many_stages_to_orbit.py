# Lab  How many stages does a rocket need to reach orbit?
import math

DV = 9400.0          # velocity change to low Earth orbit, m/s
ISP = 300.0          # specific impulse of every stage, s
G0 = 9.80665         # standard gravity, m/s^2
EPS = 0.10           # structural ratio of every stage
M_PAY = 1000.0       # payload, kg
MIN_GAIN = 0.20      # an extra stage must add 20 % payload

c = ISP * G0                             # exhaust speed, m/s
prev = 0.0                               # last payload fraction
print('stages  mass ratio  payload frac.  launch mass (t)')
for n in range(1, 9):
    r = math.exp(DV / (n * c))           # mass ratio per stage
    if 1 / r <= EPS:
        print(f'{n:6d} {r:11.2f}   impossible: needs 1/R > eps')
        continue
    pi_s = (1 / r - EPS) / (1 - EPS)     # payload fraction/stage
    frac = pi_s**n                       # whole rocket
    print(f'{n:6d} {r:11.2f} {frac:14.4f}'
          f' {M_PAY / frac / 1000:16.1f}')
    if prev > 0 and frac < (1 + MIN_GAIN) * prev:
        print(f'Stage {n} adds under {MIN_GAIN:.0%}: use {n - 1}')
        break
    prev = frac
else:
    print('Every stage tested was still worth adding')
