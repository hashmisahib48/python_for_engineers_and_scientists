# Example 7.4  Ideal Brayton cycle of a gas turbine (has a bug)
T1 = 288.15        # compressor inlet temperature, K
T3 = 1500.0        # turbine inlet temperature, K
R_P = 15.0         # pressure ratio p2/p1, -
GAMMA = 1.4        # ratio of specific heats of air, -
CP = 1005.0        # specific heat of air, J/(kg K)
M_DOT = 50.0       # air mass flow rate, kg/s

tau = R_P**(GAMMA - 1 / GAMMA)       # temperature ratio T2/T1, -
t2 = T1 * tau                        # compressor exit, K
t4 = T3 / tau                        # turbine exit, K
w_comp = CP * (t2 - T1)              # compressor work, J/kg
w_turb = CP * (T3 - t4)              # turbine work, J/kg
w_net = w_turb - w_comp              # net work, J/kg
q_in = CP * (T3 - t2)                # heat added, J/kg
eta = w_net / q_in                   # thermal efficiency, -
eta_carnot = 1 - T1 / T3             # Carnot limit, -

print(f'T2 = {t2:.1f} K, T4 = {t4:.1f} K')
print(f'Net power: {M_DOT * w_net / 1e6:.1f} MW')
print(f'Efficiency: {eta:.3f} (Carnot {eta_carnot:.3f})')
assert t2 < T3, 'compressor exit hotter than turbine inlet'
assert 0 < eta < eta_carnot, 'efficiency breaks the second law'
