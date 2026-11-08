# Euler's method: a steel ball cooling in an air blast
import math

rho = 7832.0        # density of AISI 1010 steel, kg/m^3
cp = 434.0          # specific heat capacity, J/(kg K)
d = 0.020           # ball diameter, m
h_conv = 150.0      # convection coefficient, W/(m^2 K)
t_air = 25.0        # air temperature, deg C
t_init = 300.0      # ball temperature at t = 0, deg C
tau = rho * cp * d / (6.0 * h_conv)     # time constant, s


def f(t, temp):
    """Rate of change of the ball temperature, K/s."""
    return -(temp - t_air) / tau


h = 10.0            # time step, s
n_steps = 30        # 30 steps of 10 s = 300 s
t = 0.0
temp = t_init
print(f'Time constant tau = {tau:.1f} s')
print('  t (s)   T Euler   T exact   error (K)')
for n in range(n_steps + 1):
    if n % 5 == 0:
        exact = t_air + (t_init - t_air) * math.exp(-t / tau)
        err = temp - exact
        print(f'{t:7.0f} {temp:9.2f} {exact:9.2f} {err:9.3f}')
    temp = temp + h * f(t, temp)      # one Euler step
    t = t + h
