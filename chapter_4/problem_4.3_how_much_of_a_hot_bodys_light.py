# Problem 4.3  Fraction of blackbody emission in the visible band
import math

C2 = 14387.769       # second radiation constant, um K (CODATA 2018)
TOL = 1e-12          # stop when a series term is this small
print(' T (K)   F(0-0.4um)  F(0-0.7um)  visible')
best_t = 0
best_f = 0.0
for t in range(1000, 12001, 100):            # temperature, K
    f_400 = 0.0
    f_700 = 0.0
    for lam_nm in range(400, 701, 300):      # 400 and 700 nm
        z = C2 / (lam_nm / 1000 * t)          # zeta = C2/(lam T)
        total = 0.0
        n = 1
        term = 1.0
        while term > TOL:
            term = (math.exp(-n * z) / n * (z**3 + 3 * z**2 / n
                    + 6 * z / n**2 + 6 / n**3))
            total += term
            n += 1
        if lam_nm == 400:
            f_400 = 15 / math.pi**4 * total
        else:
            f_700 = 15 / math.pi**4 * total
    f_vis = f_700 - f_400
    if t % 4000 == 0 or t == 2800 or t == 5800:
        print(f'{t:6d} {f_400:11.5f} {f_700:11.5f} {f_vis:9.4f}')
    if f_vis > best_f:
        best_f = f_vis
        best_t = t
print(f'Largest visible fraction {best_f:.4f} at T = {best_t} K')
