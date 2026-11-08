# Problem 1.2  From a parking orbit to geostationary orbit
import math

MU = 3.986004418e14     # Earth's GM, m^3/s^2 (WGS 84)
R_EQ = 6378137.0        # equatorial radius, m (WGS 84)
T_SID = 86164.0905      # sidereal day, s
C = 299792458.0         # speed of light, m/s (exact)
r_leo = R_EQ + 300e3    # parking-orbit radius, m

r_geo = (MU * T_SID**2 / (4 * math.pi**2)) ** (1 / 3)   # m
v_geo = 2 * math.pi * r_geo / T_SID                      # m/s
delay = 2 * (r_geo - R_EQ) / C          # up and down, s

a_t = (r_leo + r_geo) / 2               # transfer ellipse, m
v_leo = math.sqrt(MU / r_leo)           # m/s
v_per = math.sqrt(MU * (2 / r_leo - 1 / a_t))   # perigee, m/s
v_apo = math.sqrt(MU * (2 / r_geo - 1 / a_t))   # apogee, m/s
dv1 = v_per - v_leo                     # first burn, m/s
dv2 = v_geo - v_apo                     # second burn, m/s
t_trans = math.pi * math.sqrt(a_t**3 / MU)      # s

print('GEO radius (km):', round(r_geo / 1e3, 1))
print('GEO altitude (km):', round((r_geo - R_EQ) / 1e3, 1))
print('GEO speed (m/s):', round(v_geo, 1))
print('Delay up and down (ms):', round(delay * 1e3, 1))
print('LEO speed (m/s):', round(v_leo, 1))
print('Burns (m/s):', round(dv1, 1), round(dv2, 1))
print('Total delta-v (m/s):', round(dv1 + dv2, 1))
print('Transfer time (h):', round(t_trans / 3600, 2))
