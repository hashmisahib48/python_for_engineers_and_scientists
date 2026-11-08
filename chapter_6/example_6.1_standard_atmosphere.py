# Example 6.1  Standard atmosphere and the drag of an airliner
import math

G0 = 9.80665        # standard gravity, m/s^2
R_AIR = 287.053     # gas constant of air, J/(kg K)


def isa(h):
    if h <= 11000.0:                        # troposphere
        t = 288.15 - 0.0065 * h
        p = 101325.0 * (t / 288.15)**(G0 / (0.0065 * R_AIR))
    else:                                   # 11 to 20 km
        t = 216.65
        p = 22632.06 * math.exp(-G0 * (h - 11000.0)
                                / (R_AIR * t))
    rho = p / (R_AIR * t)                   # ideal gas, kg/m^3
    return t, p, rho


def drag(h, v, cd_a):
    t, p, rho = isa(h)
    return 0.5 * rho * v**2 * cd_a          # drag force, N


V = 230.0           # true airspeed, m/s
CD_A = 3.1          # drag area C_D*A of the airliner, m^2
print(' h (km)   T (K)   p (kPa)  rho (kg/m3)  D (kN)  P (MW)')
for h_km in [0, 3, 6, 9, 11, 13]:
    t, p, rho = isa(h_km * 1000.0)
    d = drag(h_km * 1000.0, V, CD_A)
    print(f'{h_km:5d} {t:9.2f} {p / 1000:9.3f} {rho:11.4f}'
          f' {d / 1000:8.1f} {d * V / 1e6:7.2f}')
