# Listing 4.6  Scan an ultrasonic weld record for the first defect
# One character per 0.5 m of pipeline weld:
#   'o' sound weld   '?' no reading (probe lifted)   'X' defect
scan = 'ooooo?ooooo??oooXoooo'
SEG = 0.5            # length of weld per character, m

n_skipped = 0
for k in range(len(scan)):
    if scan[k] == '?':
        n_skipped += 1
        continue                     # nothing to judge here
    if scan[k] == 'X':
        print(f'Defect at {k * SEG:.1f} m: stop and dig up')
        break
else:
    print('No defect found in the whole record')
print(f'Segments without a reading so far: {n_skipped}')
