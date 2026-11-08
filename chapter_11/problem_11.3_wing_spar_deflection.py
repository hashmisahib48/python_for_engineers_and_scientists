# Problem 11.3  Wing-spar deflection from strain-gauge readings
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import CubicSpline

E = 71.7e9            # Young's modulus of 7075-T6 aluminum, Pa
I_A = 2.0e-5          # second moment of area of the spar, m^4
C = 0.06              # gauge distance from the neutral axis, m
W = 1500.0            # test load, N/m
L = 4.0               # semi-span, m

x = np.linspace(0.0, L, 9)                       # gauge stations, m
strain = np.array([502, 384, 282, 196, 126, 71, 31, 8, 0]) * 1e-6
kappa = strain / C                               # curvature, 1/m

# method 1: trapezoid twice; slope and deflection start at zero
slope = cumulative_trapezoid(kappa, x, initial=0.0)
defl_t = cumulative_trapezoid(slope, x, initial=0.0)

# method 2: cubic spline of the curvature, integrated twice
spl = CubicSpline(x, kappa)
defl_s = spl.antiderivative(2)                   # zero at x = 0

tip_exact = W * L**4 / (8 * E * I_A)             # beam theory, m
print(f'Tip deflection, trapezoid: {1e3 * defl_t[-1]:.2f} mm')
print(f'Tip deflection, spline:    {1e3 * defl_s(L):.2f} mm')
print(f'Tip deflection, exact:     {1e3 * tip_exact:.2f} mm')
print(f'Mid-span deflection, spline: {1e3 * defl_s(2.0):.2f} mm')
tip_slope = spl.antiderivative()(L)              # rad
print(f'Tip slope, spline: {np.degrees(tip_slope):.3f} deg')
