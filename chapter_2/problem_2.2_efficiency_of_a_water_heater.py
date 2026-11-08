# Problem 2.2  Efficiency of a water heater from one log line
RHO = 993.0        # density of water near 38 deg C, kg/m^3
CP = 4178.0        # specific heat of water near 38 deg C, J/(kg K)

log = ' WH-12;T_in=18.4C;T_out=57.9C;flow=4.20L/min;P_el=12.00kW\n'
log = log.strip()

tag = log[:log.find(';')]
k = log.find('T_in=') + 5
t_in = float(log[k:log.find('C', k)])          # deg C
k = log.find('T_out=') + 6
t_out = float(log[k:log.find('C', k)])         # deg C
k = log.find('flow=') + 5
flow = float(log[k:log.find('L', k)])          # L/min
k = log.find('P_el=') + 5
p_el = float(log[k:log.find('kW', k)]) * 1000  # W

m_dot = RHO * flow / 1000 / 60                 # mass flow, kg/s
q = m_dot * CP * (t_out - t_in)                # heat to water, W
eta = q / p_el                                 # efficiency

print(f'Log line has {log.count(";") + 1} fields; heater {tag}')
print('-' * 40)
print(f'{"Inlet temperature":<22}{t_in:>10.1f} °C')
print(f'{"Outlet temperature":<22}{t_out:>10.1f} °C')
print(f'{"Mass flow rate":<22}{m_dot:>10.4f} kg/s')
print(f'{"Heat to the water":<22}{q / 1000:>10.2f} kW')
print(f'{"Electrical power":<22}{p_el / 1000:>10.2f} kW')
print(f'{"Efficiency":<22}{eta:>10.1%}')
print(f'{"Losses":<22}{(p_el - q) / 1000:>10.2f} kW')
