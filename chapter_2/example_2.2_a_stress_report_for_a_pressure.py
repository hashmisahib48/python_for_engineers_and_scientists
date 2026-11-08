# Example 2.2  Hoop and axial stress in a thin-walled vessel
S_YIELD = 260.0       # minimum yield strength, MPa (A516 Grade 70)

tag = input('Vessel tag: ')
p = float(input('Design pressure (MPa): '))
d_in = float(input('Inner diameter (mm): '))
t = float(input('Wall thickness (mm): '))

r = d_in / 2                   # inner radius, mm
sigma_h = p * r / t            # hoop stress, MPa
sigma_a = p * r / (2 * t)      # axial stress, MPa
fs = S_YIELD / sigma_h         # safety factor against yield

print()
print(f'Stress report for vessel {tag.strip().upper()}')
print('-' * 38)
print(f'Design pressure     {p:8.2f} MPa')
print(f'Radius / thickness  {r / t:8.1f}')
print(f'Hoop stress         {sigma_h:8.1f} MPa')
print(f'Axial stress        {sigma_a:8.1f} MPa')
print(f'Safety factor       {fs:8.2f}')
print('-' * 38)
print(f'Hoop stress = {sigma_h / S_YIELD:.1%} of yield strength')
