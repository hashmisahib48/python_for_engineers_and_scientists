# Listing 3.1  Does the relief valve on an air receiver open?
p_set = 8.0           # valve set pressure, bar (gauge)
p_gauge = 8.6         # pressure read on the gauge, bar
vented = False

if p_gauge > p_set:
    print('Relief valve opens')
    vented = True

print('Check complete')
print('Vented:', vented)
