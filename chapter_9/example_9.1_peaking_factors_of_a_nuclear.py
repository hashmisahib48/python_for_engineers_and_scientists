# Example 9.1: peaking factors of a 17 x 17 PWR fuel assembly
import numpy as np

P_ASSY = 17.67e6     # thermal power of one assembly, W
L_ACT = 3.66         # active fuel length, m

rel = np.loadtxt('rod_power.txt')    # relative rod powers, -
fuel = rel > 0.0                     # guide tubes hold no fuel
n_rods = fuel.sum()
rel = rel / rel[fuel].mean()         # fuel average is now 1

f_pin = rel.max()                    # pin peaking factor, -
i, j = np.unravel_index(rel.argmax(), rel.shape)
q_avg = P_ASSY / (n_rods * L_ACT)    # mean linear heat rate, W/m
col_avg = rel.sum(axis=0) / fuel.sum(axis=0)    # fuel only
n_hot = (rel > 1.05).sum()

print(f'Map {rel.shape}: {n_rods} fuel rods, '
      f'{rel.size - n_rods} guide tubes')
print(f'Pin peaking factor: {f_pin:.3f} at row {i}, col {j}')
print(f'Coolest rod: {rel[fuel].min():.3f}, '
      f'rods above 1.05: {n_hot}')
print(f'Linear heat rate, average rod: {q_avg / 1e3:.2f} kW/m')
print(f'Linear heat rate, hot rod:     '
      f'{f_pin * q_avg / 1e3:.2f} kW/m')
print('Column averages, columns 0 to 16:')
print(np.round(col_avg, 3))
