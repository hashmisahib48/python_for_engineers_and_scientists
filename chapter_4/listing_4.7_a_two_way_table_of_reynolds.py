# Listing 4.7  Reynolds numbers of water for speeds and pipe sizes
RHO = 998.21         # density of water at 20 degC, kg/m^3
MU = 1.0016e-3       # dynamic viscosity, Pa s

print('V (m/s) |    25 mm    50 mm    75 mm   100 mm')
for i in range(1, 7):
    v = 0.5 * i                          # mean velocity, m/s
    print(f'{v:7.1f} |', end='')
    for d_mm in range(25, 101, 25):      # diameter, mm
        re = RHO * v * (d_mm / 1000) / MU
        print(f'{re:9.0f}', end='')
    print()                              # end of the row
