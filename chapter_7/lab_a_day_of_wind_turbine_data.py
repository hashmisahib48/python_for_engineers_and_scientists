# Engineering Lab  One day of turbine records: energy and health
import csv
from pathlib import Path
from windturbine import power_curve, P_RATED

DT = 600.0                      # logging interval, s
e_meas = e_curve = 0.0          # energy logged and expected, J
n_good, bad = 0, []

with open(Path('scada_day.csv'), newline='') as f:
    for row in csv.DictReader(f):
        try:
            v = float(row['wind_ms'])                  # m/s
            p = float(row['power_kw']) * 1e3           # W
            if v < 0 or p > 1.1 * P_RATED:
                raise ValueError('reading out of range')
        except (ValueError, TypeError) as err:
            bad.append(f"{row['time']} ({type(err).__name__})")
            continue
        e_meas += p * DT
        e_curve += power_curve(v) * DT
        n_good += 1

cf = e_meas / (P_RATED * n_good * DT)       # capacity factor, -
ratio = e_meas / e_curve                    # performance ratio, -
assert 0 <= cf <= 1, 'capacity factor out of range'
hours = n_good * DT / 3600                  # good data, h
report = [f'Good records:      {n_good} ({hours:.1f} h)',
          f'Rejected records:  {len(bad)}',
          f'Energy delivered:  {e_meas / 3.6e9:.2f} MWh',
          f'Power-curve value: {e_curve / 3.6e9:.2f} MWh',
          f'Capacity factor:   {cf:.1%}',
          f'Performance ratio: {ratio:.3f}']
report += ['  rejected ' + x for x in bad]
with open('turbine_report.txt', 'w', encoding='utf-8') as f:
    for line in report:
        f.write(line + '\n')
        if not line.startswith('  '):
            print(line)                  # summary lines only
