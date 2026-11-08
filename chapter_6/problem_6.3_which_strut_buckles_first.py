# Problem 6.3  Euler or Johnson? Ranking four tubular struts
import math


def tube_props(d_out, wall):
    """Area (m^2) and radius of gyration (m) of a round tube."""
    d_in = d_out - 2 * wall
    area = math.pi * (d_out**2 - d_in**2) / 4
    i_sec = math.pi * (d_out**4 - d_in**4) / 64
    return area, math.sqrt(i_sec / area)


def critical_load(length, d_out, wall, e, s_y, k_end=1.0):
    """Buckling load (N) and the formula that applies."""
    area, r_g = tube_props(d_out, wall)
    slender = k_end * length / r_g
    c_c = math.sqrt(2 * math.pi**2 * e / s_y)   # transition
    if slender >= c_c:
        s_cr, rule = math.pi**2 * e / slender**2, 'Euler'
    else:
        s_cr = s_y - (s_y * slender / (2 * math.pi))**2 / e
        rule = 'Johnson'
    return s_cr * area, rule


STEEL = (200e9, 250e6)              # A36: E, yield strength, Pa
ALUM = (68.9e9, 276e6)              # 6061-T6: E, yield strength, Pa
struts = [('A steel', 2.0, 0.060, 0.004, STEEL, 1.0),
          ('B steel', 0.8, 0.060, 0.004, STEEL, 1.0),
          ('C alum.', 2.0, 0.080, 0.005, ALUM, 1.0),
          ('D alum.', 2.0, 0.080, 0.005, ALUM, 0.5)]
results = []
for name, length, d, w, (e, s_y), k_end in struts:
    p_cr, rule = critical_load(length, d, w, e, s_y, k_end=k_end)
    results.append((name, p_cr, rule))
for name, p_cr, rule in sorted(results, key=lambda s: s[1]):
    print(f'{name}: P_cr = {p_cr / 1000:7.1f} kN  ({rule})')
