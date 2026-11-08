# Problem 3.2  How fast does the reactor power change?
import math

BETA = 0.0065             # delayed neutron fraction of U-235, -
LAM = 0.08                # one-group precursor decay, 1/s
k_eff = 1.0010            # effective multiplication factor, -

rho = (k_eff - 1) / k_eff                 # reactivity, -
print(f'Reactivity: {rho * 1e5:.1f} pcm = {rho / BETA:.3f} dollars')

if math.isclose(rho, 0.0, abs_tol=1e-6):
    print('Critical: power is steady')
elif rho < 0:
    print('Subcritical: power falls')
elif rho < BETA:
    period = (BETA - rho) / (LAM * rho)   # stable period, s
    print('Delayed supercritical: power rises under control')
    print(f'Period: {period:.1f} s')
    print(f'Power doubles in {period * math.log(2):.1f} s')
else:
    print('PROMPT CRITICAL: SCRAM the reactor')
