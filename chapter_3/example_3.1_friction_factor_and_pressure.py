# Example 3.1  Friction factor and pressure drop in a water pipe
import math

rho = 998.21          # density of water at 20 degC, kg/m^3
mu = 1.0016e-3        # dynamic viscosity, Pa s
d_pipe = 0.025        # inner diameter, m
eps = 0.045e-3        # roughness of commercial steel, m
l_pipe = 30.0         # pipe length, m
v_mean = 1.2          # mean velocity, m/s

re = rho * v_mean * d_pipe / mu
rr = eps / d_pipe     # relative roughness, -

if re < 2300:
    regime = 'laminar'
    f = 64 / re
elif re < 4000:
    regime = 'transitional'
    f = 0.25 / math.log10(rr / 3.7 + 5.74 / 4000**0.9)**2
else:
    regime = 'turbulent'
    f = 0.25 / math.log10(rr / 3.7 + 5.74 / re**0.9)**2

dp = f * (l_pipe / d_pipe) * rho * v_mean**2 / 2     # Pa
print(f'Reynolds number: {re:.0f}')
print(f'Flow regime: {regime}')
print(f'Friction factor: {f:.4f}')
print(f'Pressure drop: {dp / 1000:.2f} kPa')
if regime == 'transitional':
    print('Warning: regime uncertain; f taken at Re = 4000')
