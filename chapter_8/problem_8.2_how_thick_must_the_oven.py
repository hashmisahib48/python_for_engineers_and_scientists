# Problem 8.2  Heat loss through an insulated oven wall (per m^2)
class Layer:
    """One thermal resistance in series; subclasses define r()."""
    def __str__(self):
        return f'{self.name:14} R = {self.r():.3e} m^2 K/W'


class Conduction(Layer):
    def __init__(self, name, thick, k):
        self.name, self.thick, self.k = name, thick, k  # m, W/(m K)

    def r(self):
        return self.thick / self.k


class Convection(Layer):
    def __init__(self, name, h):
        self.name, self.h = name, h               # W/(m^2 K)

    def r(self):
        return 1.0 / self.h


T_IN, T_OUT = 220.0, 25.0                         # air temps, degC
for t_ins in [0.025, 0.050, 0.075, 0.100]:        # insulation, m
    wall = [Convection('oven air', 25.0),
            Conduction('steel liner', 0.0015, 60.5),
            Conduction('glass fiber', t_ins, 0.040),
            Conduction('steel skin', 0.0010, 60.5),
            Convection('room air', 8.0)]
    r_total = sum([layer.r() for layer in wall])
    q = (T_IN - T_OUT) / r_total                  # heat flux, W/m^2
    t_skin = T_OUT + q * wall[-1].r()             # skin temp, degC
    print(f'{t_ins * 1e3:5.0f} mm: q = {q:6.1f} W/m^2, '
          f'skin {t_skin:5.1f} degC')
    if t_skin <= 45.0:
        break
print('Wall of the accepted design:')
for layer in wall:
    print(' ', layer)
