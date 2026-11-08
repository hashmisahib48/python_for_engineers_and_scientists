# Listing 11.1  First bending mode of a blade by bisection
import math


def bisect(f, a, b, tol=1e-10):
    """Root of f in [a, b] by bisection; returns (root, steps)."""
    if f(a) * f(b) > 0:
        raise ValueError('f(a) and f(b) must differ in sign')
    n = 0
    while b - a > tol:
        m = 0.5 * (a + b)
        if f(a) * f(m) <= 0:
            b = m                 # root lies in the left half
        else:
            a = m                 # root lies in the right half
        n += 1
    return 0.5 * (a + b), n


def mode_eq(x):
    """Cantilever frequency equation, x = beta*L."""
    return math.cos(x) * math.cosh(x) + 1.0


E = 200e9           # Young's modulus of steel, Pa
RHO = 7850.0        # density of steel, kg/m^3
L = 0.25            # blade length, m
t = 0.006           # blade thickness, m

bl, steps = bisect(mode_eq, 1.0, 3.0)
f1 = bl**2 / (2 * math.pi) * math.sqrt(E * t**2
                                       / (12 * RHO * L**4))
print(f'beta*L = {bl:.10f} after {steps} halvings')
print(f'Residual f(root) = {mode_eq(bl):.1e}')
print(f'First natural frequency: {f1:.1f} Hz')
