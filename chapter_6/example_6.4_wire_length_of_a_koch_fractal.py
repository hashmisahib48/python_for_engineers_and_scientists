# Example 6.4  Wire length of a Koch fractal monopole antenna
import cmath

TURN = cmath.exp(1j * cmath.pi / 3)     # rotation by +60 degrees


def koch(a, b, n):
    """Points of a Koch curve of order n from a to b (complex).

    Returns a list that starts at a and stops just before b.
    """
    if n == 0:
        return [a]
    step = (b - a) / 3
    p1 = a + step                       # one third of the way
    p3 = a + 2 * step                   # two thirds of the way
    p2 = p1 + step * TURN               # tip of the new bump
    return (koch(a, p1, n - 1) + koch(p1, p2, n - 1)
            + koch(p2, p3, n - 1) + koch(p3, b, n - 1))


def wire_length(points):
    """Total length of the polyline through the points."""
    return sum([abs(q - p) for p, q in zip(points, points[1:])])


HEIGHT = 0.060                          # monopole height, m
base, top = 0j, 1j * HEIGHT             # wire runs up the y axis
print(' n  segments  wire (mm)  wire/height  (4/3)^n')
for n in range(6):
    pts = koch(base, top, n) + [top]
    length = wire_length(pts)
    print(f'{n:2d} {len(pts) - 1:9d} {length * 1000:10.2f} '
          f'{length / HEIGHT:12.4f} {(4 / 3)**n:8.4f}')
