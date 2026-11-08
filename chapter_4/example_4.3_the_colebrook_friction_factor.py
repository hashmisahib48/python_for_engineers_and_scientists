# Example 4.3  Colebrook friction factor by fixed-point iteration
import math

RHO = 998.21         # density of water at 20 degC, kg/m^3
MU = 1.0016e-3       # dynamic viscosity, Pa s
D = 0.025            # inner diameter, m
EPS = 0.045e-3       # roughness of commercial steel, m
V = 1.2              # mean velocity, m/s
TOL = 1e-10          # relative change that counts as converged
MAX_ITER = 50        # safety limit on the number of passes

re = RHO * V * D / MU
x = 1 / math.sqrt(0.02)              # first guess for 1/sqrt(f)
change = 1.0
n = 0
print(' n    f            relative change')
while change > TOL and n < MAX_ITER:
    x_new = -2 * math.log10(EPS / (3.7 * D) + 2.51 * x / re)
    change = abs(x_new - x) / abs(x_new)
    x = x_new
    n += 1
    print(f'{n:2d}   {1 / x**2:.8f}   {change:.2e}')

if change <= TOL:
    print(f'Re = {re:.0f}: f = {1 / x**2:.5f} after {n} passes')
else:
    print(f'No convergence after {MAX_ITER} passes')
