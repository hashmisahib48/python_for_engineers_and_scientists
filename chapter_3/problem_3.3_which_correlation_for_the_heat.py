# Problem 3.3  Which correlation for the heat transfer coefficient?
import math

# Water at a mean temperature of 40 degC
rho = 992.1               # density, kg/m^3
mu = 0.653e-3             # dynamic viscosity, Pa s
k = 0.631                 # thermal conductivity, W/(m K)
pr = 4.32                 # Prandtl number, -

d = 0.020                 # tube inner diameter, m
l_tube = 3.0              # heated length, m
v = 0.80                  # mean velocity, m/s
heating = True            # True: wall heats the water

re = rho * v * d / mu
print(f'Re = {re:.0f}, Pr = {pr}, L/D = {l_tube / d:.0f}')

valid = True
if re < 2300:
    nu = 3.66
    name = 'laminar, fully developed, constant wall temperature'
elif re >= 10000 and 0.6 <= pr <= 160 and l_tube / d >= 10:
    n = 0.4 if heating else 0.3
    nu = 0.023 * re**0.8 * pr**n
    name = f'Dittus-Boelter, n = {n}'
else:
    valid = False
    name = 'none: transitional flow or outside the validity limits'

print(f'Correlation: {name}')
if valid:
    h = nu * k / d
    print(f'Nu = {nu:.4g}, h = {h:.0f} W/(m^2 K)')
