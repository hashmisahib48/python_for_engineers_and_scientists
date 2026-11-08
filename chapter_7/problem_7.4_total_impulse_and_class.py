# Problem 7.4  Total impulse, Isp and class of a solid motor
import csv

G0 = 9.80665          # standard gravity, m/s^2
M_PROP = 0.072        # propellant mass, kg
CLASSES = 'ABCDEFGHIJKLMNO'


def read_thrust(fname):
    """Time (s) and thrust (N) lists; skip rows out of order."""
    times, forces = [], []
    with open(fname, newline='') as f:
        for k, row in enumerate(csv.DictReader(f), start=2):
            try:
                t, F = float(row['time_s']), float(row['thrust_N'])
                if times and t <= times[-1]:
                    raise ValueError(f'time {t} s is not later')
            except ValueError as err:
                print(f'line {k} skipped: {err}')
                continue
            times.append(t)
            forces.append(max(F, 0.0))
    return times, forces


t, F = read_thrust('thrust_test.csv')
impulse = 0.0
for k in range(len(t) - 1):                    # trapezoid rule
    impulse += (F[k] + F[k + 1]) / 2 * (t[k + 1] - t[k])    # N s
assert impulse > 0, 'no thrust recorded'
on = [tk for tk, Fk in zip(t, F) if Fk >= 0.05 * max(F)]
t_burn = on[-1] - on[0]                         # burn time, s
k, limit = 0, 2.5                     # class A: up to 2.5 N s
while impulse > limit:
    k, limit = k + 1, 2 * limit
print(f'Total impulse: {impulse:.1f} N s  (class {CLASSES[k]}, '
      f'up to {limit:g} N s)')
print(f'Peak thrust: {max(F):.1f} N, burn time: {t_burn:.2f} s')
print(f'Average thrust: {impulse / t_burn:.1f} N')
print(f'Specific impulse: {impulse / (M_PROP * G0):.0f} s')
