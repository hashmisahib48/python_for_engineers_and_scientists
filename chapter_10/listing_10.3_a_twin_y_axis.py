# Listing 10.3  Temperature and density of the standard atmosphere
import numpy as np
import matplotlib.pyplot as plt

g, R = 9.80665, 287.053      # m/s^2; J/(kg K) for dry air
T0, p0, L = 288.15, 101325.0, 0.0065     # K, Pa, K/m (sea level)
h = np.linspace(0.0, 20000.0, 401)        # altitude, m

T = np.where(h <= 11000.0, T0 - L * h, 216.65)          # K
p11 = p0 * (216.65 / T0) ** (g / (L * R))               # Pa
p = np.where(h <= 11000.0, p0 * (T / T0) ** (g / (L * R)),
             p11 * np.exp(-g * (h - 11000.0) / (R * 216.65)))
rho = p / (R * T)                                        # kg/m^3
print(f'At 11 km: T = {T[220]:.2f} K, rho = {rho[220]:.4f} kg/m^3')

fig, ax1 = plt.subplots(figsize=(5.6, 2.5))
ax1.plot(h / 1000, T, color='C1')
ax1.set_xlabel('Altitude $h$ (km)')
ax1.set_ylabel('Temperature $T$ (K)', color='C1')
ax1.tick_params(axis='y', labelcolor='C1')

ax2 = ax1.twinx()                     # second y axis, same x axis
ax2.plot(h / 1000, rho, color='C2')
ax2.set_ylabel(r'Density $\rho$ (kg/m$^3$)', color='C2')
ax2.tick_params(axis='y', labelcolor='C2')
plt.show()
