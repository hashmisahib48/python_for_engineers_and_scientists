# Problem 1.1  The red and blue-green lines of hydrogen
R_INF = 10973731.568160     # Rydberg constant, 1/m (CODATA 2018)
M_E = 9.1093837015e-31      # electron mass, kg (CODATA 2018)
M_P = 1.67262192369e-27     # proton mass, kg (CODATA 2018)
H = 6.62607015e-34          # Planck constant, J s (exact)
C = 299792458.0             # speed of light, m/s (exact)
E = 1.602176634e-19         # elementary charge, C (exact)

r_h = R_INF / (1 + M_E / M_P)     # Rydberg constant for H, 1/m

lam_alpha = 1 / (r_h * (1 / 2**2 - 1 / 3**2))   # H-alpha, m
lam_beta = 1 / (r_h * (1 / 2**2 - 1 / 4**2))    # H-beta, m
e_alpha = H * C / lam_alpha / E                 # photon, eV
e_beta = H * C / lam_beta / E                   # photon, eV

# H-alpha again, for an infinitely heavy nucleus, m
lam_inf = 1 / (R_INF * (1 / 2**2 - 1 / 3**2))

print('R_H (1/m):', round(r_h, 1))
print('H-alpha (nm):', round(lam_alpha * 1e9, 3))
print('H-alpha photon (eV):', round(e_alpha, 4))
print('H-beta (nm):', round(lam_beta * 1e9, 3))
print('H-beta photon (eV):', round(e_beta, 4))
print('Ratio beta/alpha energy:', round(e_beta / e_alpha, 6))
print('H-alpha shift (pm):', round((lam_alpha - lam_inf) * 1e12, 1))
