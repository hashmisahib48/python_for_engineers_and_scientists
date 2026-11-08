# Listing 6.6  A recursive function: Legendre polynomials


def legendre(n, x):
    """Legendre polynomial P_n(x) by Bonnet's recursion."""
    if n == 0:                      # base case 1
        return 1.0
    if n == 1:                      # base case 2
        return x
    return ((2 * n - 1) * x * legendre(n - 1, x)
            - (n - 1) * legendre(n - 2, x)) / n


def n_calls(n):
    """Number of calls that legendre(n, x) makes in total."""
    if n <= 1:
        return 1
    return 1 + n_calls(n - 1) + n_calls(n - 2)


x = 0.5                             # cos(60 deg)
print(f'P2(0.5) = {legendre(2, x)}, formula: {(3 * x**2 - 1) / 2}')
for n in [5, 10, 20, 25]:
    print(f'P{n}(0.5) = {legendre(n, x):+.6f}   '
          f'calls: {n_calls(n):,}')
