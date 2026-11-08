"""sections.py  Beam cross-sections bent about a horizontal axis."""
import math


class Section:
    """Base class: subclasses set h, area() and inertia()."""
    kind = 'section'

    def modulus(self):                    # Z = I / c, m^3
        return self.inertia() / (self.h / 2)

    def __str__(self):
        return f'{self.kind:10} A = {self.area() * 1e6:6.0f} mm^2'


class Rectangle(Section):
    kind = 'rectangle'

    def __init__(self, b, h):
        self.b, self.h = b, h             # width, height, m

    def area(self):
        return self.b * self.h

    def inertia(self):
        return self.b * self.h**3 / 12


class Circle(Section):
    kind = 'round bar'

    def __init__(self, d):
        self.h = d                        # diameter = height, m

    def area(self):
        return math.pi * self.h**2 / 4

    def inertia(self):
        return math.pi * self.h**4 / 64
