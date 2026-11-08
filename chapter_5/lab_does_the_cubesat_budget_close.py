# Engineering Lab  Mass and power budget of a 3U CubeSat
import math

# part: (function, mass in kg, power in W, duty cycle)
parts = {'structure': ('structure', 0.62, 0.0, 0.0),
         'harness': ('wiring', 0.20, 0.0, 0.0),
         'solar cells': ('generation', 0.30, 0.0, 0.0),
         'battery': ('storage', 0.27, 0.0, 0.0),
         'EPS board': ('regulation', 0.09, 0.3, 1.0),
         'computer': ('command', 0.07, 0.4, 1.0),
         'UHF radio': ('downlink', 0.09, 4.0, 0.10),
         'S-band radio': ('downlink', 0.25, 8.0, 0.08),
         'antennas': ('antenna', 0.10, 0.0, 0.0),
         'ADCS unit': ('pointing', 0.70, 2.0, 1.0),
         'camera': ('payload', 1.10, 3.5, 0.25),
         'heater': ('thermal', 0.05, 2.0, 0.20)}
m_limit, m_margin, p_margin = 4.00, 0.10, 0.20

# orbit-average power from the cells (500 km, Sun in orbit plane)
r_e, h = 6371.0, 500.0                     # km
f_sun = 1 - math.asin(r_e / (r_e + h)) / math.pi
p_gen = 1361.0 * 0.28 * 0.030 * f_sun      # S * eta * A, W

needed = {f for f, m, p, d in parts.values()}
m_tot = sum([m for f, m, p, d in parts.values()])
p_avg = sum([p * d for f, m, p, d in parts.values()])
print(f'{len(parts)} parts, {len(needed)} functions')
print(f'Sunlit fraction {f_sun:.3f}, cells give {p_gen:.2f} W')
print(f'Mass  {m_tot:.2f} kg x 1.10 = {m_tot * (1 + m_margin):.2f}'
      f' kg (limit {m_limit:.2f})')
print(f'Power {p_avg:.2f} W x 1.20 = {p_avg * (1 + p_margin):.2f}'
      f' W (available {p_gen:.2f})')

# which single part can go and still leave every function?
for name, (f, m, p, d) in parts.items():
    left = {g for k, (g, mm, pp, dd) in parts.items() if k != name}
    m_new = (m_tot - m) * (1 + m_margin)
    if left == needed and m_new <= m_limit:
        print(f'Remove {name}: {m_new:.2f} kg, '
              f'{(p_avg - p * d) * (1 + p_margin):.2f} W')
