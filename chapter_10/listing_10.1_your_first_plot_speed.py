# Listing 10.1  Speed of a skydiver with air drag
import numpy as np
import matplotlib.pyplot as plt

g = 9.81            # gravitational acceleration, m/s^2
v_t = 54.0          # terminal speed, belly-to-earth, m/s

t = np.linspace(0.0, 30.0, 301)      # time, s
v = v_t * np.tanh(g * t / v_t)       # speed, m/s

t_95 = v_t / g * np.arctanh(0.95)   # arctanh: inverse of tanh, s
print(f'95 % of terminal speed after {t_95:.1f} s')

plt.plot(t, v)
plt.xlabel('Time t (s)')
plt.ylabel('Speed v (m/s)')
plt.title('Free fall with quadratic drag')
plt.show()
