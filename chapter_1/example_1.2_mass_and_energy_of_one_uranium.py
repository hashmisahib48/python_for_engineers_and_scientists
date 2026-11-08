# Example 1.2  Mass-energy of one U-235 fission
# Constants: CODATA 2018.  Atomic mass of U-235: NIST.
C = 299792458.0             # speed of light, m/s (exact)
EV = 1.602176634e-19        # one electronvolt, J (exact)
N_A = 6.02214076e23         # Avogadro constant, 1/mol (exact)
AMU = 1.66053906660e-27     # atomic mass constant, kg
M_U235 = 235.0439301        # molar mass of U-235, g/mol

e_mev = 200.0               # mean energy per fission, MeV
e_fis = e_mev * 1e6 * EV    # energy per fission, J
dm = e_fis / C**2           # mass that disappears, kg
dm_u = dm / AMU             # the same mass in atomic mass units

atoms = 1000 / M_U235 * N_A     # atoms in 1 kg of U-235
e_kg = atoms * e_fis            # energy from 1 kg, J/kg
coal = e_kg / 29.3e6            # kg of coal equivalent (29.3 MJ/kg)

print('Energy per fission (J):', e_fis)
print('Mass converted (kg):', dm)
print('Mass converted (u):', round(dm_u, 4))
print('Fraction of the atom:', round(dm_u / M_U235, 6))
print('Atoms in 1 kg:', atoms)
print('Energy from 1 kg (TJ):', round(e_kg / 1e12, 1))
print('Coal equivalent (tonnes):', round(coal / 1000))
