# Listing 11.6  Error of forward and central differences
import numpy as np
import matplotlib.pyplot as plt

G = 9.80665          # standard gravity, m/s^2
VT = 52.05           # terminal speed of the probe, m/s
H0 = 3000.0          # release altitude, m


def altitude(t):
    """Altitude of a probe falling from rest with drag, m."""
    return H0 - VT**2 / G * np.log(np.cosh(G * t / VT))


t0 = 3.0                                    # instant, s
v_exact = -VT * np.tanh(G * t0 / VT)        # exact velocity, m/s
h = np.logspace(-12, 0, 49)                 # step sizes, s
fwd = (altitude(t0 + h) - altitude(t0)) / h
cen = (altitude(t0 + h) - altitude(t0 - h)) / (2 * h)
err_f = np.abs(fwd - v_exact)
err_c = np.abs(cen - v_exact)

k = np.argmin(err_c)
print(f'Exact velocity at t = 3 s: {v_exact:.10f} m/s')
print(f'Best central step h = {h[k]:.1e} s, '
      f'error {err_c[k]:.1e} m/s')
j = 40                                      # h[40] = 0.01 s
print(f'At h = {h[j]:.0e} s: forward error {err_f[j]:.2e}, '
      f'central error {err_c[j]:.2e} m/s')

fig, ax = plt.subplots(figsize=(5.0, 3.0))
ax.loglog(h, err_f, 'o-', color='#F2711C', ms=3, label='forward')
ax.loglog(h, err_c, 's-', color='#0B2C5F', ms=3, label='central')
ax.set_xlabel('Step size h (s)')
ax.set_ylabel('Error in velocity (m/s)')
ax.grid(True, which='major', alpha=0.4)
ax.legend()
fig.tight_layout()
plt.show()
