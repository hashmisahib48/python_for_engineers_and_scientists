# Listing 10.2  Two body positions, object-oriented style
import numpy as np
import matplotlib.pyplot as plt

g = 9.81                        # gravitational acceleration, m/s^2
t = np.linspace(0.0, 30.0, 301)            # time, s

fig, ax = plt.subplots(figsize=(6.0, 3.4))
for v_t, pose in [(54.0, 'belly-to-earth'), (80.0, 'head-down')]:
    v = v_t * np.tanh(g * t / v_t)         # speed, m/s
    ax.plot(t, v, label=f'{pose}, $v_t$ = {v_t:.0f} m/s')
    ax.axhline(v_t, color='gray', linestyle='--', linewidth=0.8)

ax.set_xlabel('Time $t$ (s)')
ax.set_ylabel('Speed $v$ (m/s)')
ax.set_title('Skydiver speed with quadratic drag')
ax.set_xlim(0.0, 30.0)
ax.set_ylim(0.0, 90.0)
ax.grid(True, alpha=0.3)
ax.legend(loc='lower right')
plt.show()
