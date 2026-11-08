# Problem 2.3  Nuclear binding energy from the liquid-drop model
A_V = 15.5     # volume coefficient, MeV
A_S = 16.8     # surface coefficient, MeV
A_C = 0.72     # Coulomb coefficient, MeV
A_A = 23.0     # asymmetry coefficient, MeV
QE = 1.602176634e-19   # J per eV (CODATA 2018)
C = 299792458.0        # speed of light, m/s
U = 1.66053906660e-27  # atomic mass unit, kg (CODATA 2018)

label = input('Nuclide, e.g. Fe-56: ').strip()
z = int(input('Atomic number Z: '))

dash = label.find('-')
symbol = label[:dash].capitalize()
a = int(label[dash + 1:])              # mass number
n = a - z                              # neutron number

b = (A_V * a - A_S * a**(2 / 3) - A_C * z * (z - 1) / a**(1 / 3)
     - A_A * (a - 2 * z)**2 / a)       # binding energy, MeV
dm = b * 1e6 * QE / C**2               # mass defect, kg

e_g = b * 1e6 * QE / (a * U) / 1000   # J to split 1 g of nuclei

print(f'{symbol}-{a}:  Z = {z},  N = {n},  A = {a}')
print(f'{"Binding energy B":<24}{b:>11.1f} MeV')
print(f'{"Per nucleon B/A":<24}{b / a:>11.3f} MeV')
print(f'{"Mass defect":<24}{dm:>11.3e} kg')
print(f'{"":<24}{dm / U:>11.4f} u')
print(f'{"Energy to split 1 g":<24}{e_g:>11.3e} J')
