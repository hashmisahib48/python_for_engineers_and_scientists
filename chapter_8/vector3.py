"""vector3.py  A 3-D vector for forces and fields (SI units)."""
import math


class Vector3:
    """A vector with Cartesian components x, y, z."""

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f'Vector3({self.x:.4g}, {self.y:.4g}, {self.z:.4g})'

    def __add__(self, other):                 # u + v
        return Vector3(self.x + other.x, self.y + other.y,
                       self.z + other.z)

    def __sub__(self, other):                 # u - v
        return Vector3(self.x - other.x, self.y - other.y,
                       self.z - other.z)

    def __mul__(self, c):                     # u * number
        return Vector3(c * self.x, c * self.y, c * self.z)

    def __rmul__(self, c):                    # number * u
        return self * c

    def __abs__(self):                        # abs(u), magnitude
        return math.sqrt(self.dot(self))

    def dot(self, other):
        return (self.x * other.x + self.y * other.y
                + self.z * other.z)

    def cross(self, other):
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)
