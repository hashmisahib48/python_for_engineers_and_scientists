# Listing 8.1  A first class: a linear spring
class Spring:
    """A linear elastic spring that obeys F = k x."""

    def __init__(self, k, name='spring'):
        self.k = k                # stiffness, N/m
        self.name = name          # a label for printing


front = Spring(2.5e4, 'front coil')
valve = Spring(5.0e4, name='valve spring')
print(type(front))
print(front.name, front.k)
print(valve.name, valve.k)
valve.k = 5.4e4                   # a stiffer replacement, N/m
print(valve.name, valve.k)
print(isinstance(front, Spring))
