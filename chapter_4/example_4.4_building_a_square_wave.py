# Example 4.4  Fourier series of a square wave and its overshoot
import math

N_POINTS = 2000      # sample points on 0 < x <= pi/2

print(' harmonics  terms   peak    x_peak (rad)   s(pi/2)')
for m in range(5):
    k_max = 3**m                         # highest harmonic: 1..81
    peak = 0.0                           # running maximum
    x_peak = 0.0
    for j in range(1, N_POINTS + 1):
        x = j * (math.pi / 2) / N_POINTS     # x = omega t, rad
        s = 0.0                              # partial sum
        for k in range(1, k_max + 1, 2):     # odd harmonics
            s += 4 / math.pi * math.sin(k * x) / k
        if s > peak:
            peak = s
            x_peak = x
    n_terms = (k_max + 1) // 2
    print(f'{k_max:10d} {n_terms:6d} {peak:7.4f} {x_peak:12.4f}'
          f' {s:10.4f}')
