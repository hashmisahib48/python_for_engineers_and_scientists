# Example 10.2  Blackbody spectra on logarithmic axes
import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015e-34          # Planck constant, J s
c = 299792458.0             # speed of light, m/s
k_B = 1.380649e-23          # Boltzmann constant, J/K
b = 2.897771955e-3          # Wien displacement constant, m K

def planck(lam, T):
    """Spectral radiance, W/(m^2 sr m), at wavelength lam (m)."""
    x = h * c / (lam * k_B * T)
    return 2 * h * c**2 / lam**5 / np.expm1(x)

lam = np.logspace(-7, -4, 2000)        # 0.1 to 100 micrometers, m
fig, ax = plt.subplots(figsize=(6.0, 3.6))
for T in [300.0, 1000.0, 3000.0, 5772.0]:
    B = planck(lam, T)
    ax.loglog(lam * 1e6, B * 1e-6, label=f'{T:.0f} K')
    j = np.argmax(B)
    print(f'{T:5.0f} K: peak {lam[j] * 1e6:6.3f} um,'
          f' Wien {b / T * 1e6:6.3f} um')

T_all = np.linspace(200.0, 6000.0, 50)       # locus of the peaks
ax.loglog(b / T_all * 1e6, planck(b / T_all, T_all) * 1e-6,
          'k--', linewidth=0.8, label="Wien's law")
ax.axvspan(0.38, 0.75, color='gold', alpha=0.25)   # visible band
ax.set_ylim(1e-2, 1e8)
ax.set_xlabel(r'Wavelength $\lambda$ ($\mu$m)')
ax.set_ylabel(r'$B_\lambda$ (W m$^{-2}$ sr$^{-1}$ $\mu$m$^{-1}$)')
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, which='major', alpha=0.3)
plt.show()
