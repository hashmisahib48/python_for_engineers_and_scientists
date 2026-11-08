# Listing 3.2  Switch the cooling fan of a battery pack
t_cell = 41.5         # hottest cell temperature, degC
T_ON = 40.0           # fan switches on above this, degC

if t_cell > T_ON:
    fan = 'ON'
    print(f'Cell at {t_cell} degC: fan on')
else:
    fan = 'OFF'
    print(f'Cell at {t_cell} degC: fan off')
print(f'Fan state: {fan}')
