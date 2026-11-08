# Power in the wind that passes through a turbine rotor
# Your first script: variables, arithmetic, print() and round()

rho_air = 1.225     # air density at sea level (ISA), kg/m^3
d_rotor = 120.0     # rotor diameter, m
v_wind = 11.0       # wind speed at hub height, m/s
c_p = 0.45          # power coefficient of the rotor, -

area = 3.14159 * d_rotor**2 / 4             # swept area, m^2
p_wind = 0.5 * rho_air * area * v_wind**3   # power in the wind, W
p_rotor = c_p * p_wind                      # rotor power, W

print('Swept area (m^2):', round(area))
print('Power in the wind (MW):', round(p_wind / 1e6, 2))
print('Rotor power (MW):', round(p_rotor / 1e6, 2))
print('Betz limit on c_p:', round(16 / 27, 3))
