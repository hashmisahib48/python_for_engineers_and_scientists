"""Power curve of a 2 MW wind turbine (illustrative data, SI)."""
import math

RHO_AIR = 1.225          # sea-level air density, kg/m^3
D_ROTOR = 90.0           # rotor diameter, m
CP = 0.45                # power coefficient below rated, -
P_RATED = 2.0e6          # rated electrical power, W
V_IN, V_OUT = 3.5, 25.0  # cut-in and cut-out wind speeds, m/s
BETZ = 16 / 27           # Betz limit on CP, -


def power_curve(v):
    """Expected power (W) at hub-height wind speed v (m/s)."""
    if v < V_IN or v > V_OUT:
        return 0.0
    area = math.pi * D_ROTOR**2 / 4                # swept area, m^2
    return min(0.5 * RHO_AIR * area * CP * v**3, P_RATED)


assert CP < BETZ, 'power coefficient above the Betz limit'

if __name__ == '__main__':
    for v in (3.0, 6.0, 9.0, 12.0, 26.0):
        print(f'{v:5.1f} m/s: {power_curve(v) / 1e3:7.1f} kW')
