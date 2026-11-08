# Problem 6.1  Heat loss through a composite wall, per m^2


def r_cond(thickness, k, area=1.0):
    return thickness / (k * area)       # conduction, K/W


def r_conv(h, area=1.0):
    return 1.0 / (h * area)             # convection, K/W


def r_series(*resistances):
    return sum(resistances)             # K/W


def report(label, t_in, t_out, *layers):
    """Print heat flux and the temperature after each layer."""
    q = (t_in - t_out) / r_series(*layers)      # W per m^2
    temps = [t_in]
    for r in layers:
        temps.append(temps[-1] - q * r)     # T after each layer
    print(f'{label}: q = {q:.1f} W/m2, T =',
          [round(t, 1) for t in temps])        # degC
    return q


inside, outside = r_conv(10.0), r_conv(25.0)
brick = r_cond(0.10, 0.72)              # common brick
board = r_cond(0.013, 0.17)             # plasterboard
glass = r_cond(0.050, 0.046)            # glass fiber blanket

q1 = report('Bare wall', 20.0, -10.0, inside, board, brick, outside)
q2 = report('Insulated', 20.0, -10.0,       # air in, out, degC
            inside, board, glass, brick, outside)
print(f'Insulation cuts the loss by {1 - q2 / q1:.1%}')
