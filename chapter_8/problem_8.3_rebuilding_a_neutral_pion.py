# Problem 8.3  Rebuilding a neutral pion from its two photons
import math


class FourMomentum:
    """Energy E and momentum (px, py, pz), all in MeV (c = 1)."""

    def __init__(self, e, px, py, pz):
        self.e, self.px, self.py, self.pz = e, px, py, pz

    def __add__(self, other):
        return FourMomentum(self.e + other.e, self.px + other.px,
                            self.py + other.py, self.pz + other.pz)

    @property
    def p(self):                          # momentum magnitude, MeV
        return math.sqrt(self.px**2 + self.py**2 + self.pz**2)

    @property
    def mass(self):                       # invariant mass, MeV
        return math.sqrt(max(self.e**2 - self.p**2, 0.0))


def photon(e, theta_deg):
    th = math.radians(theta_deg)
    return FourMomentum(e, e * math.cos(th), e * math.sin(th), 0.0)


g1, g2 = photon(600.0, 6.24), photon(400.0, -9.6)   # simulated
pion = g1 + g2
print(f'Photon masses: {g1.mass:.3f} and {g2.mass:.3f} MeV')
print(f'Pair: E = {pion.e:.1f} MeV, p = {pion.p:.1f} MeV')
print(f'Invariant mass m = {pion.mass:.2f} MeV')
print(f'beta = {pion.p / pion.e:.4f}, '      # speed / c
      f'gamma = {pion.e / pion.mass:.3f}')
