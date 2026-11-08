# Example 1.4  de Broglie wavelength of an accelerated electron
import math

H = 6.62607015e-34          # Planck constant, J s (exact)
E = 1.602176634e-19         # elementary charge, C (exact)
M_E = 9.1093837015e-31      # electron mass, kg
C = 299792458.0             # speed of light, m/s (exact)

v_acc = 100e3               # accelerating voltage, V

ke = E * v_acc                          # kinetic energy, J
p_classic = math.sqrt(2 * M_E * ke)     # Newtonian momentum, kg m/s
p_rel = math.sqrt(2 * M_E * ke * (1 + ke / (2 * M_E * C**2)))

lam_classic = H / p_classic             # wavelength, m
lam_rel = H / p_rel                     # wavelength, m
error = (lam_classic - lam_rel) / lam_rel * 100   # percent
agree = math.isclose(lam_classic, lam_rel, rel_tol=0.01)  # 1 %?

print('Kinetic energy (J):', ke)
print('Wavelength, Newtonian (m):', lam_classic)
print('Wavelength, relativistic (m):', lam_rel)
print('Wavelength (pm):', round(lam_rel * 1e12, 3))
print('Newtonian error (%):', round(error, 2))
print('Agree to 1 %:', agree)
