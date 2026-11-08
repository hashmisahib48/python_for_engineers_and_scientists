# Example 1.1  Reynolds number of water in a pipe
# Water at 20 degC and 1 atm (NIST Chemistry WebBook)
rho = 998.21        # density, kg/m^3
mu = 1.0016e-3      # dynamic viscosity, Pa s

d_pipe = 0.050      # inner diameter, m
v_mean = 1.5        # mean velocity, m/s

re = rho * v_mean * d_pipe / mu         # Reynolds number, -
nu = mu / rho                           # kinematic viscosity, m^2/s

re_crit = 2300                          # end of laminar flow, -
v_crit = re_crit * mu / (rho * d_pipe)  # velocity at re_crit, m/s
q_crit = v_crit * 3.14159 * d_pipe**2 / 4   # flow rate, m^3/s

print('Kinematic viscosity (m^2/s):', nu)
print('Reynolds number:', round(re))
print('Re / Re_crit:', round(re / re_crit, 1))
print('Laminar limit velocity (m/s):', round(v_crit, 4))
print('Laminar limit flow (L/min):', round(q_crit * 1000 * 60, 2))
