# Example 5.2  Node and element tables of a Warren truss
import math

nodes = [(0.0, 0.0), (4.0, 0.0), (8.0, 0.0), (12.0, 0.0),
         (2.0, 3.0), (6.0, 3.0), (10.0, 3.0)]        # (x, y), m
elements = [(0, 1), (1, 2), (2, 3), (4, 5), (5, 6),
            (0, 4), (4, 1), (1, 5), (5, 2), (2, 6), (6, 3)]
area = 9.5e-4         # cross-section area, m^2
i_min = 8.7e-7        # least second moment of area, m^4
rho = 7850.0          # density of steel, kg/m^3
e_mod = 200e9         # Young's modulus of steel, Pa

lengths = []
print(' el  nodes     L (m)       c       s')
for k in range(len(elements)):
    n1, n2 = elements[k]
    x1, y1 = nodes[n1]
    x2, y2 = nodes[n2]
    length = math.hypot(x2 - x1, y2 - y1)
    c = (x2 - x1) / length          # direction cosines
    s = (y2 - y1) / length
    lengths.append(length)
    print(f'{k:3d}   {n1}-{n2}  {length:8.3f}  {c:7.3f} {s:7.3f}')

total = sum(lengths)
l_long = max(lengths)
p_cr = math.pi ** 2 * e_mod * i_min / l_long ** 2   # N
print(f'Nodes: {len(nodes)}, elements: {len(elements)}, '
      f'2j - 3 = {2 * len(nodes) - 3}')
print(f'Total member length: {total:.3f} m')
print(f'Steel mass: {rho * area * total:.1f} kg')
print(f'Longest member: {lengths.index(l_long)}, {l_long:.3f} m')
print(f'Its Euler buckling load: {p_cr / 1e3:.1f} kN')
