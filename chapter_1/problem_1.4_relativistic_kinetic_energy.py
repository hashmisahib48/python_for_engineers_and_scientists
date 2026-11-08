# Problem 1.4  Relativistic kinetic energy without losing digits
import math

C = 299792458.0         # speed of light, m/s (exact)
m = 1000.0              # spacecraft mass, kg

v_a = 7700.0                            # case A, m/s
b2_a = (v_a / C)**2                     # beta squared, -
g_a = 1 / math.sqrt(1 - b2_a)           # Lorentz factor, -
naive_a = (g_a - 1) * m * C**2          # Eq. (1.16), J
safe_a = b2_a * g_a**2 / (g_a + 1) * m * C**2   # Eq. (1.17), J
newton_a = 0.5 * m * v_a**2             # J

v_b = 1.0                               # case B, m/s
b2_b = (v_b / C)**2
g_b = 1 / math.sqrt(1 - b2_b)
naive_b = (g_b - 1) * m * C**2          # J
safe_b = b2_b * g_b**2 / (g_b + 1) * m * C**2   # J

print('A  gamma - 1:', g_a - 1)
print('A  naive, safe (J):', naive_a, safe_a)
print('A  relativistic part (J):', round(safe_a - newton_a, 1))
print('A  rounding error (J):', round(naive_a - safe_a))
print('B  1 - beta^2:', 1 - b2_b)
print('B  naive, safe (J):', naive_b, safe_b)
print('B  safe = mv^2/2:', math.isclose(safe_b, 0.5 * m * v_b**2))
