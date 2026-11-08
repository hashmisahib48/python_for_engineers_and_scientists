# Example 7.2  Principal stresses from a strain-rosette log
import csv
import math

E = 200e9          # Young's modulus of steel, Pa
NU = 0.30          # Poisson's ratio, -
SY = 355e6         # yield strength of S355 steel, Pa


def principal(ea, eb, ec):
    """Principal stresses (Pa) from a 0/45/90 rosette."""
    mid = (ea + ec) / 2
    rad = math.sqrt((ea - eb)**2 + (eb - ec)**2) / math.sqrt(2)
    k = E / (1 - NU**2)
    e1, e2 = mid + rad, mid - rad
    return k * (e1 + NU * e2), k * (e2 + NU * e1)


peak, t_peak, n = 0.0, 0.0, 0
with open('rosette_log.csv', newline='') as fin:
    with open('rosette_stress.csv', 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(['time_s', 's1_MPa', 's2_MPa', 'svm_MPa'])
        for row in csv.DictReader(fin):
            t = float(row['time_s'])
            ea, eb, ec = [float(row[k]) * 1e-6
                          for k in ('eps_a', 'eps_b', 'eps_c')]
            s1, s2 = principal(ea, eb, ec)
            svm = math.sqrt(s1**2 - s1 * s2 + s2**2)    # Pa
            mpa = [round(s / 1e6, 1) for s in (s1, s2, svm)]
            writer.writerow([t] + mpa)
            n += 1
            if svm > peak:
                peak, t_peak, s_at_peak = svm, t, (s1, s2)
print(f'{n} rows read, results in rosette_stress.csv')
print(f'Peak von Mises stress: {peak / 1e6:.1f} MPa at {t_peak} s')
print(f'  sigma_1 = {s_at_peak[0] / 1e6:.1f} MPa, '
      f'sigma_2 = {s_at_peak[1] / 1e6:.1f} MPa')
print(f'Safety factor on yield: {SY / peak:.2f}')
