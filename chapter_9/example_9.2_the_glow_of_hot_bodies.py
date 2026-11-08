# Example 9.2: blackbody spectra of four bodies by broadcasting
import numpy as np

H = 6.62607015e-34      # Planck constant, J s
C = 299792458.0         # speed of light, m/s
K_B = 1.380649e-23      # Boltzmann constant, J/K
SIGMA = 5.670374419e-8  # Stefan-Boltzmann constant, W/(m^2 K^4)

names = ['Sun surface', 'lamp filament', 'red-hot steel',
         'room wall']
t = np.array([5772.0, 3000.0, 1000.0, 300.0])   # temperature, K
lam = np.linspace(0.1e-6, 200e-6, 400_000)      # wavelength, m
d_lam = lam[1] - lam[0]                         # step, m

# column (4, 1) against row (400000,) gives a (4, 400000) table
x = H * C / (lam * K_B * t[:, np.newaxis])
b = 2 * H * C**2 / lam**5 / np.expm1(x)     # W/(m^2 sr m)

lam_pk = lam[b.argmax(axis=1)]              # peak wavelength, m
e_tot = np.pi * b.sum(axis=1) * d_lam       # emissive power, W/m^2
vis = (lam >= 380e-9) & (lam <= 750e-9)     # visible band mask
f_vis = np.pi * b[:, vis].sum(axis=1) * d_lam / e_tot

print(f'b: shape {b.shape}, {b.nbytes / 1e6:.1f} MB')
print(f"{'body':14}{'T, K':>6}{'peak, um':>10}{'E, W/m2':>11}"
      f"{'E/sT^4':>8}{'visible':>9}")
for k in range(len(t)):
    ratio = e_tot[k] / (SIGMA * t[k]**4)
    print(f'{names[k]:14}{t[k]:6.0f}{lam_pk[k] * 1e6:10.3f}'
          f'{e_tot[k]:11.3e}{ratio:8.4f}{f_vis[k]:9.3%}')
print(f"Wien: lam_pk * T = {np.round(lam_pk * t * 1e3, 3)} mm K")
