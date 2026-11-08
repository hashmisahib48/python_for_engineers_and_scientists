# Example 4.2  Mo-99 -> Tc-99m generator, stepped through time
import math

T_HALF_MO = 65.924   # half-life of Mo-99, h
T_HALF_TC = 6.0072   # half-life of Tc-99m, h
A_MO0 = 20.0         # Mo-99 activity at elution, GBq
DT = 0.01            # time step, h
N_STEPS = 7200       # 72 h in steps of DT
PRINT_EVERY = 1200   # print a row every 12 h

lam_mo = math.log(2) / T_HALF_MO     # decay constants, 1/h
lam_tc = math.log(2) / T_HALF_TC
n_mo = A_MO0 / lam_mo                # Mo-99 nuclei (GBq h)
n_tc = 0.0                           # column freshly eluted
a_tc_max = 0.0                       # running maximum, GBq
t_max = 0.0

print('  t (h)   A_Mo (GBq)   A_Tc (GBq)')
for step in range(N_STEPS + 1):
    t = step * DT
    a_mo = lam_mo * n_mo                 # activities, GBq
    a_tc = lam_tc * n_tc
    if step % PRINT_EVERY == 0:
        print(f'{t:7.1f} {a_mo:12.3f} {a_tc:12.3f}')
    if a_tc > a_tc_max:
        a_tc_max = a_tc
        t_max = t
    decays_mo = a_mo * DT                # decays in this step
    n_mo -= decays_mo
    n_tc += decays_mo - a_tc * DT
print(f'Peak Tc-99m activity: {a_tc_max:.3f} GBq'
      f' at t = {t_max:.2f} h')
