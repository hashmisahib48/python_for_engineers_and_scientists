# Example 7.3  Dead-time correction of a damaged Geiger counter log
import math
from pathlib import Path

TAU = 100e-6       # dead time of the GM tube, s
DT = 10.0          # counting interval, s


def true_rate(m, tau=TAU):
    """True count rate (1/s) from a measured rate m (1/s)."""
    if m * tau >= 1:
        raise ValueError(f'm*tau = {m * tau:.2f}, rate impossible')
    return m / (1 - m * tau)


counts, rates = [], []
lines = Path('gm_counts.txt').read_text().splitlines()
for k, line in enumerate(lines, start=1):
    if line.startswith('#') or line.strip() == '':
        continue                                # comment or blank
    try:
        start, text = line.split()
        c = int(text)
        n = true_rate(c / DT)
    except ValueError as err:
        print(f'line {k} skipped: {err}')
    else:
        counts.append(c)
        rates.append(n)

c_mean = sum(counts) / len(counts)
dev2 = [(c - c_mean)**2 for c in counts]
s = math.sqrt(sum(dev2) / (len(counts) - 1))        # std deviation
print(f'{len(counts)} good intervals')
print(f'Measured rate: {c_mean / DT:.1f} 1/s')
print(f'True rate:     {sum(rates) / len(rates):.1f} 1/s')
print(f'Count scatter: {s:.0f}, Poisson: {math.sqrt(c_mean):.0f}')
