# Example 3.2  Will a cracked wing panel fracture or yield first?
import math

K_IC = 28.0           # fracture toughness, MPa m^0.5
S_Y = 500.0           # yield strength, MPa
w = 0.200             # panel width, m
b = 0.006             # panel thickness, m
a = 0.010             # half-length of the central crack, m
s = 150.0             # remote tensile stress, MPa

k_i = s * math.sqrt(math.pi * a)          # MPa m^0.5
s_net = s * w / (w - 2 * a)               # net-section stress, MPa
fs_frac = K_IC / k_i
fs_yield = S_Y / s_net
a_crit = (K_IC / s)**2 / math.pi          # critical half-length, m

if fs_frac < fs_yield:
    mode = 'fracture'
    fs = fs_frac
else:
    mode = 'net-section yielding'
    fs = fs_yield

if fs < 1.0:
    verdict = 'FAILS: remove the panel from service'
elif fs < 1.5:
    verdict = 'MARGINAL: repair before next flight'
else:
    verdict = 'SAFE: continue routine inspections'

print(f'K_I = {k_i:.2f} MPa m^0.5, net stress = {s_net:.1f} MPa')
print(f'Safety factors: fracture {fs_frac:.2f}, '
      f'yield {fs_yield:.2f}')
print(f'Governing mode: {mode}')
print(f'Critical crack length 2a: {2 * a_crit * 1000:.1f} mm')
print(verdict)
if b < 2.5 * (K_IC / S_Y)**2:
    print('Note: thinner than plane strain; K_IC is conservative')
