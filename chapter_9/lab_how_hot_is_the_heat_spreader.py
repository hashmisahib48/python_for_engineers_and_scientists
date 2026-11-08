# Lab: steady temperature field of an aluminum heat-spreader plate
import numpy as np

L, TH = 0.100, 0.002       # plate side and thickness, m
K = 167.0                  # 6061-T6 aluminum, W/(m K)
P, A = 30.0, 0.020         # chip power W, chip side m
T_EDGE, T_LIM = 25.0, 85.0 # frame and limit temperature, deg C
N = 41                     # grid points per side

h = L / (N - 1)                         # grid spacing, m
c, m = N // 2, round(A / 2 / h)         # center index, half-width
src = np.zeros((N, N))                  # q h^2 / k per node, K
chip = src[c - m:c + m + 1, c - m:c + m + 1]    # a view
chip[:] = P / (chip.size * TH * K)      # q = P / (n h^2 TH)

t = np.full((N, N), T_EDGE)             # first guess, deg C
change, n_it = 1.0, 0
while change > 1e-6:                    # Jacobi sweeps
    t_new = t.copy()
    t_new[1:-1, 1:-1] = 0.25 * (t[2:, 1:-1] + t[:-2, 1:-1]
                                + t[1:-1, 2:] + t[1:-1, :-2]
                                + src[1:-1, 1:-1])
    change = np.abs(t_new - t).max()
    t = t_new
    n_it += 1

# heat leaving through the four edges, W (Fourier's law)
rim = (t[1, 1:-1].sum() + t[-2, 1:-1].sum()
       + t[1:-1, 1].sum() + t[1:-1, -2].sum())
q_out = K * TH * (rim - 4 * (N - 2) * T_EDGE)
np.save('plate_T.npy', t)
np.savetxt('plate_T.csv', t, fmt='%.3f', delimiter=',')
i, j = np.unravel_index(t.argmax(), t.shape)
print(f'Grid {t.shape}, h = {h * 1e3:.1f} mm, chip nodes '
      f'{chip.size}, {n_it} sweeps')
print(f'Hottest point: {t[i, j]:.2f} deg C at node ({i}, {j})')
print(f'Mean plate temperature: {t.mean():.2f} deg C')
print(f'Heat out through edges: {q_out:.3f} W (chip {P} W)')
p_lim = P * (T_LIM - T_EDGE) / (t[i, j] - T_EDGE)   # linear
print(f'Power that gives {T_LIM} deg C: {p_lim:.1f} W')
