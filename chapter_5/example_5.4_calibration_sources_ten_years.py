# Example 5.4  A set of calibration sources, ten years on
half_life = {'Co-60': 5.2711, 'Cs-137': 30.08, 'Am-241': 432.6,
             'Na-22': 2.6029, 'Ba-133': 10.551,
             'H-3': 12.32}                    # years, NuDat 3
a_cert = {'Co-60': 37e3, 'Cs-137': 37e3,      # certified
          'Na-22': 37e3, 'Am-241': 37e3}      # activity, Bq
years = 10.0                 # time since certification, y
keep = 0.10                  # replace below 10 % of a_cert

# activity today, A = A0 * 2**(-t / T_half)
a_now = {iso: a0 * 0.5 ** (years / half_life[iso])
         for iso, a0 in a_cert.items()}
for a, iso in sorted([(a, iso) for iso, a in a_now.items()],
                     reverse=True):
    print(f'{iso:<7}{a / 1e3:7.2f} kBq  {a / a_cert[iso]:6.1%}')
print(f'Total: {sum(a_now.values()) / 1e3:.2f} kBq')

replace = [iso for iso in a_now if a_now[iso] < keep * a_cert[iso]]
print('Replace:', replace)

# isotopes identified in today's gamma spectrum
seen = {'Cs-137', 'Co-60', 'Am-241', 'Ba-133'}
print('Seen, not listed:', seen - set(a_cert))
print('Listed, not seen:', set(a_cert) - seen)
print('Unknown to library:', seen - set(half_life))
