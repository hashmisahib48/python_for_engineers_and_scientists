# Example 2.3  Photon energies across the electromagnetic spectrum
H = 6.62607015e-34      # Planck constant, J s (CODATA 2018)
C = 299792458.0         # speed of light in vacuum, m/s
QE = 1.602176634e-19    # elementary charge, C (J per eV)

lam1 = 3.0              # FM radio, 100 MHz band, m
lam2 = 0.1224           # microwave oven, 2.45 GHz, m
lam3 = 632.8e-9         # helium-neon laser, red, m
lam4 = 0.15406e-9       # copper K-alpha X-ray, m
lam5 = 0.9305e-12       # cobalt-60 gamma ray, 1.33 MeV, m

e1 = H * C / lam1 / QE  # photon energies, eV
e2 = H * C / lam2 / QE
e3 = H * C / lam3 / QE
e4 = H * C / lam4 / QE
e5 = H * C / lam5 / QE

head = f'{"Source":<16}{"λ (m)":>10}{"f (Hz)":>10}{"E (eV)":>10}'
print(head)
print('=' * len(head))
print(f'{"FM radio":<16}{lam1:10.3e}{C / lam1:10.3e}{e1:10.3g}')
print(f'{"Microwave":<16}{lam2:10.3e}{C / lam2:10.3e}{e2:10.3g}')
print(f'{"He-Ne laser":<16}{lam3:10.3e}{C / lam3:10.3e}{e3:10.3g}')
print(f'{"Cu K-alpha":<16}{lam4:10.3e}{C / lam4:10.3e}{e4:10.3g}')
print(f'{"Co-60 gamma":<16}{lam5:10.3e}{C / lam5:10.3e}{e5:10.3g}')
print('=' * len(head))
print(f'Gamma/radio energy ratio: {e5 / e1:,.0f}')
