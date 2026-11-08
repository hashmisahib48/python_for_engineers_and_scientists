# Example 11.2  Saturation pressure of water between table rows
import numpy as np
from scipy.interpolate import CubicSpline

# steam table: temperature (degC) and saturation pressure (kPa)
t_tab = np.arange(25.0, 301.0, 25.0)
p_tab = np.array([3.1698, 12.352, 38.597, 101.42, 232.23, 476.16,
                  892.60, 1554.9, 2549.7, 3976.2, 5946.4, 8587.9])
A = [-7.85951783, 1.84408259, -11.7866497, 22.6807411,
     -15.9618719, 1.80122502]                # Wagner-Pruss
B = [1.0, 1.5, 3.0, 3.5, 4.0, 7.5]


def p_exact(t):
    """Saturation pressure, kPa, from the Wagner-Pruss equation."""
    tk = t + 273.15
    tau = 1 - tk / 647.096
    s = sum(ai * tau**bi for ai, bi in zip(A, B))
    return 22064.0 * np.exp(647.096 / tk * s)


lnp = CubicSpline(t_tab, np.log(p_tab))    # spline through ln p
print('  T (degC)   linear  linear ln p  spline ln p    exact')
for t in [37.0, 137.0, 263.0]:
    p_lin = np.interp(t, t_tab, p_tab)
    p_log = np.exp(np.interp(t, t_tab, np.log(p_tab)))
    p_spl = np.exp(lnp(t))
    print(f'{t:9.1f} {p_lin:9.2f} {p_log:11.2f} {p_spl:12.2f}'
          f' {p_exact(t):9.2f}')

# inverse problem: boiling temperature at 1000 kPa
t_lin = np.interp(1000.0, p_tab, t_tab)
t_spl = CubicSpline(np.log(p_tab), t_tab)(np.log(1000.0))
print(f'Boiling point at 1 MPa: linear {t_lin:.2f} degC, '
      f'spline {t_spl:.2f} degC')
