# Problem 3.4  Is this triangle fit for a finite element mesh?
import math

x1 = 0.0                  # node 1, mm
y1 = 0.0
x2 = 40.0                 # node 2, mm
y2 = 30.0
x3 = 50.0                 # node 3, mm
y3 = 0.0
area = 0.5 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
if math.isclose(area, 0.0, abs_tol=1e-9):
    print('Degenerate element: the nodes lie on one line. Reject.')
else:
    if area < 0:
        area = -area
        print('Nodes are clockwise: swap nodes 2 and 3')
    l12 = math.hypot(x2 - x1, y2 - y1)
    l23 = math.hypot(x3 - x2, y3 - y2)
    l31 = math.hypot(x1 - x3, y1 - y3)
    q = 4 * math.sqrt(3) * area / (l12**2 + l23**2 + l31**2)
    # angle at each node from the law of cosines, rad
    a1 = math.acos((l12**2 + l31**2 - l23**2) / (2 * l12 * l31))
    a2 = math.acos((l12**2 + l23**2 - l31**2) / (2 * l12 * l23))
    a3 = math.pi - a1 - a2
    if a1 <= a2 and a1 <= a3:     # pick the smallest angle
        a_min = a1
    elif a2 <= a3:
        a_min = a2
    else:
        a_min = a3
    if q >= 0.6:
        grade = 'good'
    elif q >= 0.3:
        grade = 'acceptable'
    else:
        grade = 'poor: remesh this region'
    print(f'Area: {area:.1f} mm^2')
    print(f'Quality q = {q:.3f}, smallest angle '
          f'{math.degrees(a_min):.1f} deg')
    print(f'Grade: {grade}')
