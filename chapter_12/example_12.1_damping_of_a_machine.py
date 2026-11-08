# Free vibration of a damped machine mount, RK4 by hand
import numpy as np
import matplotlib.pyplot as plt
from odesteps import rk4_step

m = 250.0           # machine mass, kg
k = 4.0e5           # stiffness of the mounts, N/m
c = 1000.0          # damping coefficient, N s/m
x0 = 0.005          # initial displacement, m


def f(t, y):
    """State y = [x, v]; returns [dx/dt, dv/dt]."""
    x, v = y
    return np.array([v, -(c * v + k * x) / m])


h = 0.002                              # time step, s
t = np.arange(751) * h                 # 0 to 1.5 s
y = np.zeros((len(t), 2))              # one row [x, v] per time
y[0] = [x0, 0.0]
for n in range(len(t) - 1):
    y[n + 1] = rk4_step(f, t[n], y[n], h)
x = y[:, 0]
wn = np.sqrt(k / m)                    # natural frequency, rad/s
zeta = c / (2 * np.sqrt(k * m))        # damping ratio
wd = wn * np.sqrt(1 - zeta**2)         # damped frequency, rad/s
exact = x0 * np.exp(-zeta * wn * t) * (np.cos(wd * t)
        + zeta / np.sqrt(1 - zeta**2) * np.sin(wd * t))
err = np.max(np.abs(x - exact))        # largest error, m
pk = [n for n in range(1, len(t) - 1) if x[n - 1] < x[n] > x[n + 1]]
delta = np.log(x[pk[0]] / x[pk[1]])    # logarithmic decrement
print(f'Natural frequency: {wn / (2 * np.pi):.4f} Hz')
print(f'Log decrement: {delta:.4f}')
print(f'Damping ratio: {delta / np.hypot(2 * np.pi, delta):.4f}')
print(f'Largest error against exact: {err:.2e} m')
plt.plot(t, 1000 * x)
plt.xlabel('Time t (s)')
plt.ylabel('Displacement x (mm)')
plt.show()
