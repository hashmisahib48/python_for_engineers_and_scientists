# Listing 5.4  Check several thermocouple channels at once
names = ['TC1', 'TC2', 'TC3', 'TC4']
temps = [64.8, 71.2, 58.9, 69.7]          # degC
limits = [70.0, 70.0, 60.0, 65.0]         # degC

for k, (name, t, lim) in enumerate(zip(names, temps, limits)):
    status = 'OVER' if t > lim else 'ok'
    print(f'{k}  {name}  {t:5.1f} / {lim:4.1f} degC  {status}')

over = [name for name, t, lim in zip(names, temps, limits)
        if t > lim]
print('Channels over their limit:', over)
