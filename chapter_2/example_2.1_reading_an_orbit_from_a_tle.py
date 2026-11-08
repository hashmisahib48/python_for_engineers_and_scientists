# Example 2.1  Decode line 2 of a two-line element set (TLE)
import math

MU = 3.986004418e14     # Earth's gravitational parameter, m^3/s^2
R_E = 6378.137e3        # Earth's equatorial radius, m

line2 = ('2 25544  51.6416 247.4627 0006703 130.5360 '
         '325.0288 15.72125391563537')

sat_no = int(line2[2:7])             # catalog number
incl = float(line2[8:16])            # inclination, deg
raan = float(line2[17:25])           # ascending node, deg
ecc = float('0.' + line2[26:33])     # decimal point assumed
n_rev = float(line2[52:63])          # mean motion, rev/day

n = n_rev * 2 * math.pi / 86400      # mean motion, rad/s
a = (MU / n**2) ** (1 / 3)           # semi-major axis, m
period = 1440 / n_rev                # orbital period, min
h_peri = (a * (1 - ecc) - R_E) / 1000    # perigee altitude, km
h_apo = (a * (1 + ecc) - R_E) / 1000     # apogee altitude, km

print('Characters in line 2:', len(line2))
print('Catalog number:', sat_no)
print('Inclination (deg):', incl)
print('RAAN (deg):', raan)
print('Eccentricity:', ecc)
print('Mean motion (rev/day):', n_rev)
print('Period (min):', round(period, 2))
print('Semi-major axis (km):', round(a / 1000, 1))
print('Perigee altitude (km):', round(h_peri, 1))
print('Apogee altitude (km):', round(h_apo, 1))
