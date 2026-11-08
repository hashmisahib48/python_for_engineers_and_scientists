# Example 6.2  Heat flow from a pin fin with an insulated tip
import math


def pin_fin(d, length, h, k=237.0, t_base=100.0, t_inf=25.0):
    """Heat rate and efficiency of a pin fin, insulated tip.

    d, length : fin diameter and length, m
    h         : convection coefficient, W/(m^2 K)
    k         : thermal conductivity, W/(m K) (pure Al)
    t_base, t_inf : base and air temperatures, degC
    Returns (q, eta): heat rate in W, fin efficiency.
    """
    perim = math.pi * d                     # perimeter, m
    area_c = math.pi * d**2 / 4             # cross-section, m^2
    m = math.sqrt(h * perim / (k * area_c))  # fin parameter, 1/m
    theta_b = t_base - t_inf                # excess temp., K
    q = (math.sqrt(h * perim * k * area_c) * theta_b
         * math.tanh(m * length))
    q_max = h * perim * length * theta_b    # whole fin at T_b
    return q, q / q_max


metals = {'copper': 401.0, 'aluminum': 237.0, 'AISI 304': 14.9}
print('Pin fin 5 mm x 50 mm, h = 25 W/(m2 K), 100 -> 25 degC')
for name, k_metal in metals.items():
    q, eta = pin_fin(0.005, 0.050, 25.0, k=k_metal)
    print(f'{name:>9}: q = {q:5.3f} W, efficiency = {eta:5.1%}')

q_fan, eta_fan = pin_fin(0.005, 0.050, h=100.0)
print(f'aluminum, fan on (h = 100): q = {q_fan:.3f} W, '
      f'efficiency = {eta_fan:.1%}')
