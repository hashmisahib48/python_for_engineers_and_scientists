# Problem 11.1  Colebrook friction factor with brentq
import math
from scipy.optimize import brentq

EPS = 0.045e-3        # roughness of commercial steel, m
D = 0.025             # inner diameter, m
RHO = 998.21          # density of water at 20 degC, kg/m^3
MU = 1.0016e-3        # viscosity of water at 20 degC, Pa s


def colebrook(re):
    """Friction factor from the Colebrook equation."""
    def g(x):                                  # x = 1 / sqrt(f)
        return x + 2 * math.log10(EPS / (3.7 * D) + 2.51 * x / re)
    return 1 / brentq(g, 1.0, 20.0)**2


def swamee_jain(re):
    return 0.25 / math.log10(EPS / (3.7 * D) + 5.74 / re**0.9)**2


re_pipe = RHO * 1.2 * D / MU                   # V = 1.2 m/s
print('        Re   Colebrook  Swamee-Jain  diff (%)')
for re in [4000.0, re_pipe, 1e5, 1e6, 1e8]:
    fc, fs = colebrook(re), swamee_jain(re)
    print(f'{re:10.4g} {fc:11.5f} {fs:12.5f} '
          f'{100 * (fs - fc) / fc:9.2f}')
