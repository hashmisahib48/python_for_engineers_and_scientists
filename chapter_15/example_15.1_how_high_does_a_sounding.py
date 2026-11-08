# Example 15.1: fly the rocket, check it, plot the flight
import numpy as np
import matplotlib.pyplot as plt
from rocket import fly, G0, ISP, T_BURN, M_DRY

M_PROP = 1.2                              # propellant, kg
burn, coast = fly(M_PROP)
t = np.concatenate([burn.t, coast.t])     # s
h, v, m = np.hstack([burn.y, coast.y])    # m, m/s, kg
mach = v / np.sqrt(1.4 * 287.053 * (288.15 - 0.0065 * h))
print(f'Burnout: h = {burn.y[0, -1]:.1f} m, '
      f'v = {burn.y[1, -1]:.1f} m/s')
print(f'Apogee:  h = {h[-1]:.1f} m at t = {t[-1]:.2f} s')
print(f'Peak Mach number: {mach.max():.3f}')

# check: without drag the ascent has an exact solution
m0, mf = M_DRY + M_PROP, M_DRY
v_bo = G0 * ISP * np.log(m0 / mf) - G0 * T_BURN
h_bo = (G0 * ISP * (T_BURN - mf * T_BURN / (m0 - mf)
                    * np.log(m0 / mf)) - G0 * T_BURN**2 / 2)
exact = h_bo + v_bo**2 / (2 * G0)
num = fly(M_PROP, cd=0.0)[1].y[0, -1]
print(f'No drag: exact {exact:.2f} m, solve_ivp {num:.2f} m')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2.8))
ax1.plot(t, h / 1000)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Altitude (km)')
ax2.plot(t, v)
ax2.axvline(T_BURN, ls='--', color='gray')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (m/s)')
fig.tight_layout()
plt.show()
