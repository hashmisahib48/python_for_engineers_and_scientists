# Problem 4.1  Where is the Molniya satellite 3 h after perigee?
import math

MU = 3.986004418e14  # Earth's gravitational parameter, m^3/s^2
R_E = 6378.137e3     # Earth's equatorial radius, m
A = 26600e3          # semi-major axis, m
E_ORB = 0.74         # eccentricity
T_SINCE = 3 * 3600.0 # time since perigee, s
TOL = 1e-12          # convergence tolerance on E, rad

period = 2 * math.pi * math.sqrt(A**3 / MU)      # s
m_anom = 2 * math.pi * T_SINCE / period           # rad

# Fixed-point iteration  E = M + e sin E
e_fp = m_anom                       # first guess, rad
n_fp = 0
change = 1.0
while change > TOL and n_fp < 500:
    e_next = m_anom + E_ORB * math.sin(e_fp)
    change = abs(e_next - e_fp)
    e_fp = e_next
    n_fp += 1
# Newton's method on g(E) = E - e sin E - M
e_nw = m_anom
n_nw = 0
change = 1.0
while change > TOL and n_nw < 50:
    g = e_nw - E_ORB * math.sin(e_nw) - m_anom
    step = g / (1 - E_ORB * math.cos(e_nw))
    e_nw -= step
    change = abs(step)
    n_nw += 1
nu = 2 * math.atan(math.sqrt((1 + E_ORB) / (1 - E_ORB))
                   * math.tan(e_nw / 2))        # true anomaly, rad
r = A * (1 - E_ORB * math.cos(e_nw))            # radius, m
print(f'Period: {period / 3600:.3f} h, M = {m_anom:.6f} rad')
print(f'Fixed point: E = {e_fp:.10f} rad in {n_fp} passes')
print(f'Newton:      E = {e_nw:.10f} rad in {n_nw} passes')
print(f'True anomaly: {math.degrees(nu):.2f} deg')
print(f'Altitude: {(r - R_E) / 1000:.0f} km')
