# Problem 6.2  Lead or iron? Shield thickness for Co-60 gammas
import math


def bisect(f, a, b, tol=1e-8):
    while b - a > tol:
        mid = 0.5 * (a + b)
        if f(a) * f(mid) <= 0.0:
            b = mid
        else:
            a = mid
    return 0.5 * (a + b)


def transmission(x, mu, buildup=True):
    """Fraction of dose passing a slab x cm thick (mu in 1/cm)."""
    b = 1.0 + mu * x if buildup else 1.0     # linear buildup
    return b * math.exp(-mu * x)


def thickness(mu, target, buildup=True):
    """Slab thickness in cm that gives the target transmission."""
    return bisect(lambda x: transmission(x, mu, buildup) - target,
                  0.0, 100.0)


# mass attenuation at 1.25 MeV (cm^2/g) and density (g/cm^3)
shields = {'lead': (5.876e-2, 11.35), 'iron': (5.350e-2, 7.874)}
TARGET = 1.0e-3                     # reduce the dose rate 1000-fold
for name, (mass_mu, rho) in shields.items():
    mu = mass_mu * rho              # linear attenuation, 1/cm
    x_nb = thickness(mu, TARGET, buildup=False)
    x_b = thickness(mu, TARGET)
    print(f'{name}: mu = {mu:.4f} 1/cm')
    print(f'   no buildup {x_nb:.2f} cm, with buildup {x_b:.2f} cm'
          f' = {x_b * rho:.0f} g/cm2')
