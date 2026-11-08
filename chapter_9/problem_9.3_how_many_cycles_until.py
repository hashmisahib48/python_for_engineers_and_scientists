# Problem 9.3: fatigue crack growth life by the Paris law
import numpy as np

C_P, M_P = 6.9e-12, 3.0     # Paris constants, m/cycle, (MPa m^0.5)
S_MAX, S_MIN = 120.0, 20.0  # cyclic stress limits, MPa
Y = 1.12                    # geometry factor, edge crack, -
K_IC = 50.0                 # fracture toughness, MPa m^0.5
A0 = 0.001                  # initial crack depth, m
A_INSP = 0.005              # crack an inspection must find, m

a_c = (K_IC / (Y * S_MAX))**2 / np.pi      # critical depth, m
a = np.linspace(A0, a_c, 20_001)           # crack depths, m
da = a[1] - a[0]
a_mid = (a[:-1] + a[1:]) / 2               # middle of each step
dk = Y * (S_MAX - S_MIN) * np.sqrt(np.pi * a_mid)   # MPa m^0.5
n_step = da / (C_P * dk**M_P)              # cycles for each step
n_cum = np.concatenate(([0.0], np.cumsum(n_step)))  # at each a
n_insp = n_cum[a <= A_INSP].max()          # cycles to reach A_INSP
half = a[n_cum <= n_cum[-1] / 2].max()     # depth at half life
e = 1 - M_P / 2                            # closed-form check
n_exact = (a_c**e - A0**e) / (
    C_P * (Y * (S_MAX - S_MIN) * np.sqrt(np.pi))**M_P * e)
print(f'Critical crack depth: {a_c * 1e3:.2f} mm')
print(f'Life to fracture: {n_cum[-1]:,.0f} cycles')
print(f'Closed form:      {n_exact:,.0f} cycles')
print(f'Cycles to reach {A_INSP * 1e3:.0f} mm: {n_insp:,.0f}')
print(f'Depth at half life: {half * 1e3:.2f} mm')
print(f'Share of life spent below 2 mm: '
      f'{n_cum[a <= 0.002].max() / n_cum[-1]:.1%}')
