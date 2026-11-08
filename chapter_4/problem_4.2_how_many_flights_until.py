# Problem 4.2  Fatigue crack growth in a wing panel (Paris law)
import math

S_MAX = 150.0        # peak stress of each flight cycle, MPa
K_IC = 28.0          # fracture toughness, MPa m^0.5
C = 1e-11            # Paris coefficient, m/cycle (MPa m^0.5)^-m
M = 3.0              # Paris exponent
A0 = 1.0e-3          # initial half crack length, m
DN = 100             # cycles per block
REPORT = 50000       # print a row every REPORT cycles
a = A0                               # half crack length, m
n = 0                                # cycles so far
k_max = S_MAX * math.sqrt(math.pi * a)
print(' cycles    2a (mm)   K_max (MPa m^0.5)')
while k_max < K_IC:
    if n % REPORT == 0:
        print(f'{n:7d} {2 * a * 1e3:9.2f} {k_max:14.2f}')
    a += C * k_max**M * DN           # Delta K = K_max for R = 0
    n += DN
    k_max = S_MAX * math.sqrt(math.pi * a)
print(f'Fracture after {n} cycles at 2a = {2 * a * 1e3:.2f} mm')
print(f'Inspection interval (half the life): {n // 2} flights')
