# Problem 5.3  Delta-v of a three-stage launcher
import math

g0 = 9.80665                 # standard gravity, m/s^2
# stage: (propellant mass kg, dry mass kg, specific impulse s)
stages = [(40000.0, 4500.0, 275.0),
          (9000.0, 1400.0, 310.0),
          (1800.0, 450.0, 315.0)]
dv_need = 9400.0             # to low Earth orbit with losses, m/s
payload = 500.0              # kg

masses = [mp + md for mp, md, isp in stages]     # kg
dv_total = 0.0
for k, (mp, md, isp) in enumerate(stages):
    m0 = payload + sum(masses[k:])          # ignition mass, kg
    mf = m0 - mp                            # burnout mass, kg
    dv = isp * g0 * math.log(m0 / mf)       # m/s
    dv_total += dv
    print(f'Stage {k + 1}: m0 = {m0:6.0f} kg, mass ratio '
          f'{m0 / mf:5.3f}, dv = {dv:5.0f} m/s')
print(f'Total dv = {dv_total:.0f} m/s (need {dv_need:.0f})')

# largest payload, in 10 kg steps, that still reaches orbit
payload = 0.0
dv_total = dv_need
while dv_total >= dv_need:
    payload += 10.0
    dv_total = 0.0
    for k, (mp, md, isp) in enumerate(stages):
        m0 = payload + sum(masses[k:])
        dv_total += isp * g0 * math.log(m0 / (m0 - mp))
best = payload - 10.0
print(f'Largest payload: {best:.0f} kg, '
      f'{best / (best + sum(masses)):.2%} of lift-off mass')
