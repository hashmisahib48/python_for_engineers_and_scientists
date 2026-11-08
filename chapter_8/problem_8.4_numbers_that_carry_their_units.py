# Problem 8.4  Numbers that carry their SI units
from dataclasses import dataclass

NAMES = ('kg', 'm', 's')                  # base units tracked


@dataclass(frozen=True)
class Q:
    value: float
    dims: tuple = (0, 0, 0)               # powers of kg, m, s

    def __mul__(self, o):
        return Q(self.value * o.value,
                 tuple([a + b for a, b in zip(self.dims, o.dims)]))

    def __truediv__(self, o):
        return Q(self.value / o.value,
                 tuple([a - b for a, b in zip(self.dims, o.dims)]))

    def __add__(self, o):
        if self.dims != o.dims:
            raise ValueError(f'{self.units()} + {o.units()}')
        return Q(self.value + o.value, self.dims)

    def units(self):
        parts = [f'{n}^{p}' for n, p in zip(NAMES, self.dims) if p]
        return ' '.join(parts) if parts else '1'


rho = Q(998.21, (1, -3, 0))               # water at 20 degC, kg/m^3
mu = Q(1.0016e-3, (1, -1, -1))            # viscosity, Pa s
v, d = Q(1.2, (0, 1, -1)), Q(0.025, (0, 1, 0))   # m/s, m
re = rho * v * d / mu
p_dyn = Q(0.5) * rho * v * v              # dynamic pressure
print(f'Re = {re.value:.0f}  [{re.units()}]')
print(f'q = {p_dyn.value:.1f}  [{p_dyn.units()}]')
try:
    print(p_dyn + v)
except ValueError as err:
    print('Caught:', err)
