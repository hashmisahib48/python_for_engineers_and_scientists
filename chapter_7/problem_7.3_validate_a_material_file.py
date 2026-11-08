# Problem 7.3  Validate a material file, then size critical cracks
import csv
import math

Y = 1.12            # geometry factor of a small edge crack, -
LOAD = 0.6          # design stress as a fraction of yield, -
A_NDT = 1.0         # smallest crack inspection can find, mm


def check_material(row):
    """Return (E, sy, KIc) in GPa, MPa, MPa m^0.5 or raise."""
    e, sy, kic = [float(row[k]) for k in
                  ('E_GPa', 'sy_MPa', 'KIc_MPa_m')]
    if min(e, sy, kic) <= 0:
        raise ValueError('values must be positive')
    if sy >= e * 1000:
        raise ValueError('yield strength above modulus')
    return e, sy, kic


print('Material         sigma (MPa)  a_c (mm)  a_c/a_NDT')
with open('materials.csv', newline='') as f:
    for line_no, row in enumerate(csv.DictReader(f), start=2):
        try:
            e, sy, kic = check_material(row)
        except ValueError as err:
            print(f'line {line_no} ({row["name"]}) rejected: {err}')
            continue
        sigma = LOAD * sy                                   # MPa
        a_c = (kic / (Y * sigma))**2 / math.pi * 1000       # mm
        print(f'{row["name"]:16}{sigma:9.0f}{a_c:12.2f}'
              f'{a_c / A_NDT:10.1f}')
