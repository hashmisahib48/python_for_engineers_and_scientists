# Example 8.2  Which section makes the best cantilever?
from sections import Section, Rectangle, Circle


class Tube(Circle):
    kind = 'tube'

    def __init__(self, d, t):
        super().__init__(d)               # sets self.h = d
        self.bore = Circle(d - 2 * t)     # the missing core, m

    def area(self):
        return super().area() - self.bore.area()

    def inertia(self):
        return super().inertia() - self.bore.inertia()


class IBeam(Section):
    kind = 'I-beam'

    def __init__(self, b, h, tf, tw):
        self.b, self.h, self.bw, self.hw = b, h, b - tw, h - 2*tf

    def area(self):
        return self.b * self.h - self.bw * self.hw

    def inertia(self):
        return (self.b * self.h**3 - self.bw * self.hw**3) / 12


P, L, E = 2.0e3, 2.0, 200e9               # load N, length m, Pa
beams = [Rectangle(0.040, 0.060), Circle(0.055),
         Tube(0.100, 0.008), IBeam(0.100, 0.150, 0.008, 0.006)]
for s in beams:
    stress = P * L / s.modulus()          # sigma = M / Z, Pa
    defl = P * L**3 / (3 * E * s.inertia())           # m
    ok = stress <= 183e6 and defl <= L / 250          # limits
    print(f'{s}  sigma = {stress / 1e6:5.1f} MPa  delta = '
          f'{defl * 1e3:5.2f} mm ', 'OK' if ok else 'fails')
