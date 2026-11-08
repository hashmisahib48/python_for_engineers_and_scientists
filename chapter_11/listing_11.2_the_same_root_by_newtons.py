# Listing 11.2  The same root by Newton's method
import math


def newton(f, dfdx, x, tol=1e-12, max_iter=50):
    """Root of f near x by Newton's method; prints each step."""
    for n in range(1, max_iter + 1):
        dx = f(x) / dfdx(x)
        x = x - dx
        print(f'{n:3d}  x = {x:.15f}  |dx| = {abs(dx):.1e}')
        if abs(dx) < tol:
            return x
    raise RuntimeError('Newton did not converge')


def mode_eq(x):
    return math.cos(x) * math.cosh(x) + 1.0


def d_mode_eq(x):
    return -math.sin(x) * math.cosh(x) + math.cos(x) * math.sinh(x)


root = newton(mode_eq, d_mode_eq, 2.0)
print(f'beta*L = {root:.10f}')
