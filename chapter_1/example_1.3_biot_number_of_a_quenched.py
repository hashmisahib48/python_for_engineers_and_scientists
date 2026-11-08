# Example 1.3  Oil quench of a steel ball: Biot number, cooling time
import math

k = 47.0            # thermal conductivity of AISI 1010, W/(m K)
rho = 7900.0        # density, kg/m^3
c = 470.0           # specific heat, J/(kg K)       (MakeItFrom.com)

d = 0.020           # ball diameter, m
h = 400.0           # heat transfer coefficient in oil, W/(m^2 K)
t_i = 850.0         # initial temperature, degC
t_oil = 40.0        # oil temperature, degC
t_end = 100.0       # target temperature, degC

r = d / 2
vol = 4 / 3 * math.pi * r**3        # volume, m^3
area = 4 * math.pi * r**2           # surface area, m^2
l_c = vol / area                    # characteristic length, m
bi = h * l_c / k                    # Biot number, -

tau = rho * c * vol / (h * area)    # time constant, s
t_cool = tau * math.log((t_i - t_oil) / (t_end - t_oil))
t_60 = t_oil + (t_i - t_oil) * math.exp(-60 / tau)

print('Characteristic length (mm):', round(l_c * 1000, 3))
print('Biot number:', round(bi, 4))
print('Time constant (s):', round(tau, 1))
print('Time to reach 100 degC (s):', round(t_cool, 1))
print('Temperature after 60 s (degC):', round(t_60, 1))
