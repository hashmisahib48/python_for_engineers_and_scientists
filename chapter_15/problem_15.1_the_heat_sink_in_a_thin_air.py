# Problem 15.1: the Example 15.2 heat sink at reduced air pressure
import numpy as np

W, L, H, T = 0.100, 0.100, 0.040, 1.5e-3  # width, height, fin, m
K_AL, K_AIR = 200.0, 0.0282   # aluminum, air, W/(m K)
NU0, ALPHA0 = 18.41e-6, 26.2e-6   # air at 325 K, 101.325 kPa
dT, BETA = 55.0, 1 / 325.65       # K, 1/K
Q_NEED = 30.0                     # amplifier heat, W


def heat(p_kpa, n):
    """Heat removed (W) by n fins (int or array) at p_kpa."""
    nu = NU0 * 101.325 / p_kpa        # nu and alpha go as 1/rho
    alpha = ALPHA0 * 101.325 / p_kpa
    s = (W - n * T) / (n - 1)                       # spacing, m
    x = 9.81 * BETA * dT * s**3 / (nu * alpha) * s / L
    h = (576 / x**2 + 2.873 / x**0.5)**-0.5 * K_AIR / s
    m = np.sqrt(2 * h / (K_AL * T))
    eta = np.tanh(m * (H + T / 2)) / (m * (H + T / 2))
    area = 2 * n * eta * (H + T / 2) * L + (W - n * T) * L   # eff.
    return h * dT * area


fins = np.arange(4, 41)
print(' p (kPa)  best n  S (mm)  Q_max (W)  13 fins (W)  30 W?')
for p in [101.325, 80.0, 60.0, 40.0]:
    q = heat(p, fins)
    k = np.argmax(q)
    s = (W - fins[k] * T) / (fins[k] - 1) * 1e3     # mm
    ok = 'yes' if q[k] >= Q_NEED else 'NO'
    print(f'{p:8.1f}  {fins[k]:6d}  {s:6.2f}  {q[k]:9.1f}  '
          f'{heat(p, 13):11.1f}  {ok:>5}')
