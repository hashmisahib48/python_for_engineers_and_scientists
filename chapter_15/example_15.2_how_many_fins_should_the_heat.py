# Example 15.2: best fin count for a natural-convection heat sink
import numpy as np
import matplotlib.pyplot as plt

W, L, H, T = 0.100, 0.100, 0.040, 1.5e-3  # width, height, fin, m
K_AL = 200.0                  # extruded aluminum, W/(m K)
T_B, T_INF = 80.0, 25.0       # base and room air, degC
NU, ALPHA, K_AIR = 18.41e-6, 26.2e-6, 0.0282   # air at 325 K, SI
BETA = 1 / (273.15 + (T_B + T_INF) / 2)        # ideal gas, 1/K
dT = T_B - T_INF                               # K

n = np.arange(4, 41)                     # candidate fin counts
s = (W - n * T) / (n - 1)                # fin spacing, m
ra = 9.81 * BETA * dT * s**3 / (NU * ALPHA)        # Ra_S
nu_s = (576 / (ra * s / L)**2
        + 2.873 / (ra * s / L)**0.5)**-0.5         # Nusselt
h = nu_s * K_AIR / s                     # W/(m^2 K)
lc = H + T / 2                           # corrected fin length, m
m_fin = np.sqrt(2 * h / (K_AL * T))      # 1/m
eta = np.tanh(m_fin * lc) / (m_fin * lc)           # fin efficiency
q = h * dT * (n * eta * 2 * lc * L + (W - n * T) * L)   # W

k = np.argmax(q)
print(f'Best fin count: {n[k]}, spacing {s[k] * 1e3:.2f} mm')
print(f'h = {h[k]:.2f} W/(m^2 K), fin efficiency {eta[k]:.3f}')
print(f'Heat removed: {q[k]:.1f} W, R = {dT / q[k]:.3f} K/W')
ra_l = 9.81 * BETA * dT * L**3 / (NU * ALPHA)
print(f'Check: S_opt = 2.714 L / Ra_L^0.25 = '
      f'{2.714 * L / ra_l**0.25 * 1e3:.2f} mm')

plt.figure(figsize=(5, 2.6))
plt.plot(n, q, 'o-', ms=3)
plt.plot(n[k], q[k], 's', ms=8, mfc='none')
plt.xlabel('Number of fins')
plt.ylabel('Heat removed (W)')
plt.show()
