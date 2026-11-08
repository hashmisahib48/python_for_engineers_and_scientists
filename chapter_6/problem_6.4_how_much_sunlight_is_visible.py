# Problem 6.4  Fraction of sunlight in a band, by adaptive Simpson
import math

H, C, K_B = 6.62607015e-34, 299792458.0, 1.380649e-23  # SI
T_SUN = 5772.0                      # solar effective temperature, K


def planck_x(x):
    """Integrand x^3 / (e^x - 1) of the blackbody fraction."""
    return x**3 / math.expm1(x) if x > 0.0 else 0.0


def simpson(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f(0.5 * (a + b)) + f(b))


def adapt(f, a, b, whole, tol, depth=0):
    """Integral of f on [a, b] by recursive Simpson halving."""
    mid = 0.5 * (a + b)
    left, right = simpson(f, a, mid), simpson(f, mid, b)
    if abs(left + right - whole) <= 15 * tol or depth >= 40:
        return left + right + (left + right - whole) / 15
    return (adapt(f, a, mid, left, tol / 2, depth + 1)
            + adapt(f, mid, b, right, tol / 2, depth + 1))


def band_fraction(lam1, lam2, temp, tol=1e-9):
    """Share of blackbody power between wavelengths lam1 < lam2."""
    x1 = H * C / (K_B * temp * lam2)
    x2 = min(H * C / (K_B * temp * lam1), 60.0)   # e^-60: nothing
    whole = simpson(planck_x, x1, x2)
    return 15 / math.pi**4 * adapt(planck_x, x1, x2, whole, tol)


print(f'Check, all x: {band_fraction(1e-9, 1e3, T_SUN):.6f}')
for lo, hi, name in [(1e-9, 400e-9, 'ultraviolet'),
                     (400e-9, 700e-9, 'visible'),
                     (700e-9, 1e3, 'infrared')]:
    print(f'{name:>11}: {band_fraction(lo, hi, T_SUN):.4f}')
