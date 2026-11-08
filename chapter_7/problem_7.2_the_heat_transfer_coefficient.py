# Problem 7.2  Heat transfer coefficient from a quench log
import csv
import math

RHO, C, K = 7900.0, 470.0, 47.0   # steel: kg/m^3, J/(kg K), W/(m K)
D = 0.020                         # ball diameter, m
T_OIL, T_I = 40.0, 850.0          # oil, initial temperature, degC
LC = D / 6                        # V/A of a sphere, m

h_values = []
with open('quench_log.csv', newline='') as fin:
    with open('quench_h.csv', 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(['time_s', 'h_W_m2K'])
        for row in csv.DictReader(fin):
            try:
                t = float(row['time_s'])
                temp = float(row['temp_C'])                # degC
                theta = (temp - T_OIL) / (T_I - T_OIL)
                h = -RHO * C * LC / t * math.log(theta)
            except ValueError as err:
                print(f"t = {row['time_s']} s skipped: {err}")
            except ZeroDivisionError:
                print(f"t = {row['time_s']} s skipped: start")
            else:
                h_values.append(h)
                writer.writerow([t, round(h, 1)])

h_mean = sum(h_values) / len(h_values)
bi = h_mean * LC / K
print(f'{len(h_values)} values of h written to quench_h.csv')
print(f'h: {min(h_values):.0f} to {max(h_values):.0f} W/(m^2 K)')
print(f'Mean h = {h_mean:.0f} W/(m^2 K), Biot number = {bi:.4f}')
print('Lumped model valid' if bi < 0.1 else 'Lumped NOT valid')
