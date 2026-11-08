"""Exact conversion factors to SI units (NIST SP 811)."""
FT = 0.3048                # foot, m
LB = 0.45359237            # pound (mass), kg
G0 = 9.80665               # standard gravity, m/s^2
LBF = LB * G0              # pound-force, N
KT = 1852 / 3600           # knot, m/s
NMI = 1852.0               # nautical mile, m
FACTORS = {'ft': FT, 'ft2': FT**2, 'lb': LB, 'lbf': LBF,
           'kt': KT, 'nmi': NMI}


def to_si(value, unit):
    """Convert value given in unit (a key of FACTORS) to SI."""
    if unit not in FACTORS:
        raise ValueError(f"unknown unit '{unit}'")
    return value * FACTORS[unit]


if __name__ == '__main__':
    assert abs(LBF - 4.4482216152605) < 1e-12, 'lbf is wrong'
    assert to_si(1.0, 'nmi') == 1852.0, 'nmi is wrong'
    print('units.py: self-test passed')
