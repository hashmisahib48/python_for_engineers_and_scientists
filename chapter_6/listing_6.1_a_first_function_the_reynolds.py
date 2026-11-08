# Listing 6.1  A first function: the Reynolds number of a flow


def reynolds(rho, v, d, mu):
    re = rho * v * d / mu       # Reynolds number, -
    return re


# water at 20 degC in a 25 mm pipe
re_water = reynolds(998.21, 1.2, 0.025, 1.0016e-3)
# air at 20 degC over a 0.30 m model wing chord
re_air = reynolds(1.2041, 30.0, 0.30, 1.8205e-5)
# engine oil at 40 degC in a 10 mm gallery
re_oil = reynolds(876.0, 2.0, 0.010, 0.2177)

print(f'Water pipe: Re = {re_water:,.0f}')
print(f'Model wing: Re = {re_air:,.0f}')
print(f'Oil gallery: Re = {re_oil:,.1f}')
