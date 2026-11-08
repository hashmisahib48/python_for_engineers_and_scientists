# Problem 3.1  Does the light eject electrons?
import math

H = 6.62607015e-34        # Planck constant, J s (exact)
C = 299792458.0           # speed of light, m/s (exact)
E = 1.602176634e-19       # elementary charge, C (exact)
M_E = 9.1093837015e-31    # electron mass, kg

lam = 405e-9              # wavelength of the violet laser, m
metal = 'sodium'
phi = 2.46                # work function, eV

e_photon = H * C / lam / E                # photon energy, eV
lam_0 = H * C / (phi * E)                 # threshold wavelength, m
print(f'Photon energy: {e_photon:.3f} eV; {metal} needs {phi} eV')

if e_photon > phi:
    k_max = e_photon - phi                # eV
    v_max = math.sqrt(2 * k_max * E / M_E)
    print(f'Electrons ejected, K_max = {k_max:.3f} eV')
    print(f'Stopping voltage: {k_max:.3f} V')
    print(f'Fastest electron: {v_max / 1000:.0f} km/s')
else:
    print('No electrons ejected, however bright the light')
    print(f'Use light shorter than {lam_0 * 1e9:.1f} nm')
