# Example 3.4  Is the water liquid, vapor or both?
import math

T_C = 647.096         # critical temperature, K
P_C = 22.064e3        # critical pressure, kPa
T_TP = 273.16         # triple-point temperature, K
A1 = -7.85951783      # Wagner-Pruss coefficients, -
A2 = 1.84408259
A3 = -11.7866497
A4 = 22.6807411
A5 = -15.9618719
A6 = 1.80122502

t_cel = 150.0         # temperature, degC
p = 1000.0            # pressure, kPa

t = t_cel + 273.15    # K
if t < T_TP:
    print('Below the triple point: outside this model')
elif t >= T_C:
    if p >= P_C:
        print('Supercritical fluid')
    else:
        print('Superheated vapor (above the critical temperature)')
else:
    tau = 1 - t / T_C
    s = (A1 * tau + A2 * tau**1.5 + A3 * tau**3 + A4 * tau**3.5
         + A5 * tau**4 + A6 * tau**7.5)
    p_sat = P_C * math.exp(T_C / t * s)
    print(f'Saturation pressure at {t_cel} degC: {p_sat:.2f} kPa')
    if math.isclose(p, p_sat, rel_tol=0.005):
        print('Saturated: liquid and vapor together')
    elif p > p_sat:
        print('Compressed (subcooled) liquid')
    else:
        print('Superheated vapor')
