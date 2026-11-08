# Problem 2.4  Where did the payload land? Decode a GPS GGA sentence
import math
R_EARTH = 6371000.0          # mean Earth radius, m
LAT_PAD = 44.0500            # launch rail latitude, deg (north +)
LON_PAD = -121.3500          # launch rail longitude, deg (east +)

gga = ('$GNGGA,001043.00,4404.14036,N,12118.85961,W,1,12,0.98,'
       '1113.0,M,-21.3,M*47')
c1 = gga.find(',')                  # positions of the commas
c2 = gga.find(',', c1 + 1)
c3 = gga.find(',', c2 + 1)
c4 = gga.find(',', c3 + 1)
c5 = gga.find(',', c4 + 1)
c6 = gga.find(',', c5 + 1)
c7 = gga.find(',', c6 + 1)
c8 = gga.find(',', c7 + 1)
c9 = gga.find(',', c8 + 1)
c10 = gga.find(',', c9 + 1)
c11 = gga.find(',', c10 + 1)

utc = gga[c1 + 1:c2]                          # hhmmss.ss
ns = gga[c3 + 1:c4]                           # 'N' or 'S'
ew = gga[c5 + 1:c6]                           # 'E' or 'W'
lat = float(gga[c2 + 1:c2 + 3]) + float(gga[c2 + 3:c3]) / 60
lat = lat * (1 - 2 * 'NS'.find(ns))           # south negative
lon = float(gga[c4 + 1:c4 + 4]) + float(gga[c4 + 4:c5]) / 60
lon = lon * (1 - 2 * 'EW'.find(ew))           # west negative
n_sat = int(gga[c7 + 1:c8])
h_msl = float(gga[c9 + 1:c10])                # above sea level, m
geoid = float(gga[c11 + 1:gga.find(',', c11 + 1)])   # separation, m

s = (math.sin(math.radians(lat - LAT_PAD) / 2)**2
     + math.cos(math.radians(LAT_PAD)) * math.cos(math.radians(lat))
     * math.sin(math.radians(lon - LON_PAD) / 2)**2)
d = 2 * R_EARTH * math.asin(math.sqrt(s))     # distance, m

print(f'Fix {utc[:2]}:{utc[2:4]}:{utc[4:]} UTC, {n_sat} satellites')
print(f'Position  {abs(lat):.5f}° {ns}   {abs(lon):.5f}° {ew}')
print(f'Altitude  {h_msl:.1f} m MSL, {h_msl + geoid:.1f} m WGS 84')
print(f'Distance from the launch rail: {d / 1000:.3f} km')
