"""odesteps.py: one step of Euler's method and of classical RK4.

f(t, y) returns dy/dt. y may be a float or a NumPy array."""


def euler_step(f, t, y, h):
    """Advance y from t to t + h with Euler's method."""
    return y + h * f(t, y)


def rk4_step(f, t, y, h):
    """Advance y from t to t + h with the classical RK4 method."""
    k1 = f(t, y)
    k2 = f(t + h / 2, y + h / 2 * k1)
    k3 = f(t + h / 2, y + h / 2 * k2)
    k4 = f(t + h, y + h * k3)
    return y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
