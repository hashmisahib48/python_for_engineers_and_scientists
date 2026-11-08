# Listing 4.1  Thermal expansion of a 25 m steel rail
ALPHA = 12e-6        # expansion coefficient of steel, 1/K
L_REF = 25.0         # rail length at the laying temperature, m
T_REF = 20.0         # laying temperature, degC

print(' T (degC)   dL (mm)')
for t in range(-20, 51, 10):
    dl = ALPHA * L_REF * (t - T_REF)          # change in length, m
    print(f'{t:8d}  {dl * 1000:+8.2f}')
print('Table complete')
