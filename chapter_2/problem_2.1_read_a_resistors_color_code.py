# Problem 2.1  Decode a four-band resistor color code
COLORS = 'blk brn red orn yel grn blu vio gry wht'   # digits 0 to 9
TOLS = 'gld slv'                 # 5 % and 10 % tolerance bands
V_S = 12.0                       # supply voltage, V
P_RATED = 0.25                   # power rating of the resistor, W

bands = input('Bands, e.g. yel-vio-red-gld: ').strip().lower()

d1 = COLORS.find(bands[0:3]) // 4      # first digit
d2 = COLORS.find(bands[4:7]) // 4      # second digit
m = COLORS.find(bands[8:11]) // 4      # multiplier, power of 10
tol = 5 * (TOLS.find(bands[12:15]) // 4 + 1)    # tolerance, %

r = (10 * d1 + d2) * 10**m             # nominal resistance, ohm
r_lo = r * (1 - tol / 100)             # ohm
r_hi = r * (1 + tol / 100)             # ohm
i = V_S / r                            # current, A
p = V_S**2 / r                         # dissipated power, W

print(f'Bands {bands.upper()} : {d1} {d2} x 10^{m}  ±{tol} %')
print(f'Resistance  {r:>10,} Ω')
print(f'Range       {r_lo:>10,.0f} Ω to {r_hi:,.0f} Ω')
print(f'Current     {i * 1000:>10.3f} mA at {V_S:.0f} V')
print(f'Power       {p:>10.3g} W = {p / P_RATED:.0%} of rating')
