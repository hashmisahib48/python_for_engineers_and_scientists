# Engineering Lab  How high can the drogue parachute open?
import math
G0, R_AIR, GAMMA = 9.80665, 287.053, 1.4   # SI units


# %% Reused tools: isa() from Example 6.1, bisect() from 6.3
def isa(h):
    if h <= 11000.0:
        t = 288.15 - 0.0065 * h
        p = 101325.0 * (t / 288.15)**(G0 / (0.0065 * R_AIR))
    else:                                   # 11 to 20 km only
        t = 216.65
        p = 22632.06 * math.exp(-G0 * (h - 11000.0) / (R_AIR * t))
    return t, p, p / (R_AIR * t)


def bisect(f, a, b, tol=1e-10):
    while b - a > tol:
        mid = 0.5 * (a + b)
        if f(a) * f(mid) <= 0.0:
            b = mid
        else:
            a = mid
    return 0.5 * (a + b)


# %% New tool: Mach number of the capsule at its terminal speed
def terminal_mach(h, mass=5000.0, cd=1.2, diameter=3.9):
    t, p, rho = isa(h)
    area = math.pi * diameter**2 / 4                    # m^2
    v_t = math.sqrt(2 * mass * G0 / (rho * cd * area))  # m/s
    return v_t / math.sqrt(GAMMA * R_AIR * t)


# %% Answer the Mission
M_LIMIT = 0.8           # highest Mach number for drogue opening
for h_km in [20, 16, 12, 8]:
    print(f'{h_km:2d} km: M = {terminal_mach(h_km * 1e3):.3f}')
h_open = bisect(lambda h: terminal_mach(h) - M_LIMIT, 0.0, 20000.0)
print(f'Open the drogue below {h_open:,.0f} m altitude')
