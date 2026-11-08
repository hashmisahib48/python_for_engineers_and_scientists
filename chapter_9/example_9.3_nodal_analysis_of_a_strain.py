# Example 9.3: nodal analysis of a strain-gauge Wheatstone bridge
import numpy as np
np.set_printoptions(precision=4, suppress=True)

V_S, R_S = 5.0, 0.5         # source: voltage V, resistance ohm
R0, GF = 350.0, 2.0         # gauge resistance ohm, gauge factor -
strain = 500e-6             # measured strain, m/m
r_g = R0 * (1 + GF * strain)    # strained gauge, ohm
R_M = 10e3                  # amplifier input resistance, ohm

# resistors as (node, node, ohm); node 0 is ground
res = [(1, 2, R0), (2, 0, r_g), (1, 3, R0), (3, 0, R0),
       (2, 3, R_M), (1, 0, R_S)]
n = 3                       # unknown node voltages v1, v2, v3
g = np.zeros((n, n))        # conductance matrix, S
i_in = np.zeros(n)          # currents injected into nodes, A
i_in[0] = V_S / R_S         # source as its Norton equivalent

for a, b, r in res:         # "stamp" each conductance into g
    c = 1.0 / r
    for p, q in ((a, b), (b, a)):
        if p > 0:
            g[p - 1, p - 1] += c
            if q > 0:
                g[p - 1, q - 1] -= c

v = np.linalg.solve(g, i_in)        # node voltages, V
v_out = v[1] - v[2]                 # bridge output, V
print('G (mS):')
print(g * 1e3)
print(f'Node voltages (V): {v}')
print(f'Bridge output:        {v_out * 1e3:.4f} mV')
print(f'Ideal quarter bridge: {V_S * GF * strain / 4 * 1e3:.4f} mV')
print(f'Meter current: {v_out / R_M * 1e6:.4f} uA')
print(f'Residual |G v - i|: {np.linalg.norm(g @ v - i_in):.1e} A')
