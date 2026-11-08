# Listing 8.2  Methods, __repr__ and __str__ for the spring
class Spring:
    """A linear elastic spring that obeys F = k x."""

    def __init__(self, k, name='spring'):
        self.k = k                # stiffness, N/m
        self.name = name

    def force(self, x):
        """Spring force in N for a deflection x in m."""
        return self.k * x

    def energy(self, x):
        """Stored strain energy in J, U = k x**2 / 2."""
        return 0.5 * self.k * x**2

    def __repr__(self):
        return f"Spring({self.k}, '{self.name}')"

    def __str__(self):
        return f'{self.name} (k = {self.k / 1e3:.1f} kN/m)'


front = Spring(2.5e4, 'front coil')
x = 0.060                         # deflection under the car, m
print(front)
print(repr(front))
print(f'F = {front.force(x):.0f} N, U = {front.energy(x):.1f} J')
