# Example 6.3  One bisection function, any equation f(x) = 0
import math


def bisect(f, a, b, tol=1e-10):
    """Bisection root of f in [a, b]; returns (root, halvings)."""
    fa = f(a)
    n = 0
    while b - a > tol:
        mid = 0.5 * (a + b)
        fm = f(mid)
        if fa * fm <= 0.0:      # sign change in the left half
            b = mid
        else:                   # sign change in the right half
            a, fa = mid, fm
        n = n + 1
    return 0.5 * (a + b), n


def freq_eq(x):
    return math.cos(x) * math.cosh(x) + 1.0   # cantilever modes


E, RHO = 200e9, 7850.0      # steel: modulus Pa, density kg/m^3
L, T = 0.30, 0.003          # strip length and thickness, m
scale = T / L**2 * math.sqrt(E / (12 * RHO))   # sqrt(EI/rho A L^4)

for k, (a, b) in enumerate([(1, 3), (4, 6), (7, 9)], start=1):
    beta_l, n = bisect(freq_eq, a, b)
    f_hz = beta_l**2 * scale / (2 * math.pi)
    print(f'Mode {k}: beta*L = {beta_l:.6f} ({n} halvings), '
          f'f = {f_hz:6.1f} Hz')

# Wien's law: the same function, handed an equation on the spot
x, n = bisect(lambda x: 5 * (1 - math.exp(-x)) - x, 4.0, 6.0)
b_wien = 6.62607015e-34 * 299792458.0 / (1.380649e-23 * x)   # m K
print(f'Wien: x = {x:.6f}, b = {b_wien * 1e3:.6f} mm K')
