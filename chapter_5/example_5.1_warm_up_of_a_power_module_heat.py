# Example 5.1  Warm-up of a power-module heat sink
import math

dt = 15.0                          # sampling interval, s
temps = [24.7, 36.4, 44.7, 50.2, 54.1, 57.4, 59.7, 61.4,
         61.9, 62.7, 63.7, 64.1, 64.7, 64.7, 64.6, 64.7,
         65.4, 64.8, 64.7, 64.6, 65.0]   # thermocouple, degC
t_limit = 70.0                     # allowed temperature, degC

n = len(temps)
t_peak = max(temps)
k_peak = temps.index(t_peak)

# steady state: mean and standard deviation of the last 8
tail = temps[-8:]
t_ss = sum(tail) / len(tail)
squares = 0.0
for t in tail:
    squares = squares + (t - t_ss) ** 2
s_ss = math.sqrt(squares / (len(tail) - 1))

# time constant: where the rise first passes 63.2 %
t_63 = temps[0] + 0.632 * (t_ss - temps[0])
k = 0
while temps[k] < t_63:
    k = k + 1
frac = (t_63 - temps[k - 1]) / (temps[k] - temps[k - 1])
tau = (k - 1 + frac) * dt

# fastest heating rate between neighboring samples
rates = []
for j in range(1, n):
    rates.append((temps[j] - temps[j - 1]) / dt)

print(f'Samples: {n} over {(n - 1) * dt:.0f} s')
print(f'Peak: {t_peak:.1f} degC at t = {k_peak * dt:.0f} s')
print(f'Steady: {t_ss:.2f} +/- {s_ss:.2f} degC')
print(f'Time constant: {tau:.1f} s')
print(f'Fastest rise: {max(rates):.3f} K/s')
print(f'Margin to limit: {t_limit - t_peak:.1f} K')
