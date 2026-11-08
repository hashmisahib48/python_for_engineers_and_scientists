# Example 8.1  Net electric force on a charged droplet
import math
from vector3 import Vector3

EPS0 = 8.8541878128e-12               # vacuum permittivity, F/m
K_E = 1.0 / (4.0 * math.pi * EPS0)    # Coulomb constant, N m^2/C^2


class PointCharge:
    """A point charge q (C) at position pos (Vector3, m)."""

    def __init__(self, q, pos):
        self.q = q
        self.pos = pos

    def field_at(self, r):
        """Electric field (V/m) that this charge makes at r."""
        d = r - self.pos
        return K_E * self.q / abs(d)**3 * d


charges = [PointCharge(5.0e-9, Vector3(0.0, 0.0, 0.0)),
           PointCharge(-3.0e-9, Vector3(0.04, 0.0, 0.0))]
drop = PointCharge(2.0e-9, Vector3(0.0, 0.03, 0.0))

e_net = Vector3()                     # start from the zero vector
for c in charges:
    e_net = e_net + c.field_at(drop.pos)
f_net = drop.q * e_net                # F = q E, N

print('E at droplet  (V/m):', e_net)
print('F on droplet  (N):  ', f_net)
print(f'|F| = {abs(f_net):.4e} N')
angle = math.degrees(math.atan2(f_net.y, f_net.x))
print(f'Direction: {angle:.2f} deg from the +x axis')
