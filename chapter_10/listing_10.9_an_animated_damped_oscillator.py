# Listing 10.9  Animation of a damped mass-spring oscillator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m, k_s, c = 1.0, 40.0, 0.8        # kg, N/m, N s/m
x0 = 50.0                         # initial displacement, mm
wn = np.sqrt(k_s / m)             # natural frequency, rad/s
zeta = c / (2 * np.sqrt(k_s * m))           # damping ratio
wd = wn * np.sqrt(1 - zeta**2)              # damped freq., rad/s
t = np.linspace(0.0, 10.0, 201)             # s
x = x0 * np.exp(-zeta * wn * t) * (np.cos(wd * t)
     + zeta / np.sqrt(1 - zeta**2) * np.sin(wd * t))   # mm
print(f'zeta = {zeta:.4f}, period = {2 * np.pi / wd:.3f} s')

fig, ax = plt.subplots(figsize=(6.0, 2.6))
ax.plot(t, x, color='lightgray')              # whole history
line, = ax.plot([], [], color='C0')           # grows frame by frame
dot, = ax.plot([], [], 'o', color='C1', ms=8)
ax.set_xlabel('Time $t$ (s)')
ax.set_ylabel('Displacement $x$ (mm)')

def update(n):
    """Draw frame n: the trace up to t[n] and the mass at t[n]."""
    line.set_data(t[:n + 1], x[:n + 1])
    dot.set_data([t[n]], [x[n]])
    return line, dot

ani = FuncAnimation(fig, update, frames=len(t), interval=50,
                    blit=True)
ani.save('oscillator.gif', writer='pillow', fps=20)
print('Saved oscillator.gif with', len(t), 'frames')
plt.show()
