# Engineering Lab  Total impulse, class and specific impulse
import numpy as np
from scipy.integrate import simpson, trapezoid
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

G0 = 9.80665              # standard gravity, m/s^2
M_PROP = 0.055            # propellant mass burned, kg

t, f = np.loadtxt('thrust_test.csv', delimiter=',', skiprows=1,
                  unpack=True)                     # s, N
spl = CubicSpline(t, f)

i_trap = trapezoid(f, x=t)                         # N s
i_simp = simpson(f, x=t)
i_spl = spl.integrate(t[0], t[-1])
print(f'Total impulse: trapezoid {i_trap:.2f}, Simpson '
      f'{i_simp:.2f}, spline {i_spl:.2f} N s')

f_max = f.max()
level = 0.05 * f_max                               # 5 % of peak, N
above = np.nonzero(f > level)[0]                   # sample indices
k1, k2 = above[0], above[-1]
t_on = brentq(lambda x: spl(x) - level, t[k1 - 1], t[k1])
t_off = brentq(lambda x: spl(x) - level, t[k2], t[k2 + 1])
t_burn = t_off - t_on
print(f'Peak thrust {f_max:.1f} N; burn from {t_on:.3f} s '
      f'to {t_off:.3f} s = {t_burn:.3f} s')
print(f'Average thrust: {i_simp / t_burn:.1f} N')

letters = 'ABCDEFGHIJ'
k, top = 0, 2.5                      # class A ends at 2.5 N s
while i_simp > top:
    k += 1                           # next letter doubles the limit
    top *= 2
print(f'Motor class: {letters[k]} ({top / 2:.0f} to {top:.0f} N s)')
isp = i_simp / (M_PROP * G0)
print(f'Specific impulse: {isp:.1f} s')
