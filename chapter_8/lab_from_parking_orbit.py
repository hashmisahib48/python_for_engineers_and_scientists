# Engineering Lab  From parking orbit to geostationary orbit
import math

MU = 3.986004418e14                   # Earth's GM, m^3/s^2
R_E = 6378.137e3                      # equatorial radius, m
T_SID = 86164.0905                    # sidereal day, s


class Orbit:
    """An elliptic orbit with periapsis rp and apoapsis ra (m)."""

    def __init__(self, rp, ra):
        self.rp, self.ra = rp, ra
        self.a = (rp + ra) / 2        # semi-major axis, m

    @property
    def period(self):                 # s
        return 2 * math.pi * math.sqrt(self.a**3 / MU)

    def speed_at(self, r):            # vis-viva equation, m/s
        return math.sqrt(MU * (2 / r - 1 / self.a))


class CircularOrbit(Orbit):
    """A circle is an ellipse with rp = ra = r."""

    def __init__(self, r):
        super().__init__(r, r)


leo = CircularOrbit(R_E + 300e3)
geo = CircularOrbit((MU * T_SID**2 / (4 * math.pi**2))**(1 / 3))
gto = Orbit(leo.rp, geo.rp)           # the Hohmann transfer ellipse
dv1 = gto.speed_at(leo.rp) - leo.speed_at(leo.rp)
dv2 = geo.speed_at(geo.rp) - gto.speed_at(geo.rp)
print(f'GEO radius {geo.rp / 1e3:.1f} km')
print(f'Speeds: LEO {leo.speed_at(leo.rp):.1f} m/s, '
      f'GEO {geo.speed_at(geo.rp):.1f} m/s')
print(f'Burn 1 {dv1:.1f} m/s, burn 2 {dv2:.1f} m/s')
print(f'Total {dv1 + dv2:.1f} m/s, coast {gto.period / 7200:.2f} h')
