# Engineering Lab  Go or no-go for launch?
# %% Readings at T-10 minutes
wind = 11.2               # peak ground wind at the pad, m/s
t_air = 6.5               # air temperature, degC
d_light = 24.0            # distance to latest lightning, km
t_light = 41.0            # minutes since that strike
p_tank = 3.34             # oxidizer tank pressure, bar
fts_armed = True          # flight termination system ready
range_clear = True        # no ships or aircraft in the hazard area

# %% Launch rules
wind_ok = wind <= 15.0
temp_ok = t_air >= 4.0
light_ok = not (d_light < 18.5 and t_light < 30.0)
tank_ok = 2.90 <= p_tank <= 3.30
safety_ok = fts_armed and range_clear

# %% Decision
n_fail = ((not wind_ok) + (not temp_ok) + (not light_ok)
          + (not tank_ok) + (not safety_ok))
if not safety_ok:
    reason = 'range safety'
elif not light_ok:
    reason = 'lightning'
elif not wind_ok:
    reason = 'ground wind'
elif not temp_ok:
    reason = 'low temperature'
elif not tank_ok:
    reason = f'tank pressure {p_tank} bar outside 2.90 to 3.30 bar'
else:
    reason = ''

print(f'Rules violated: {n_fail}')
if n_fail == 0:
    print('GO for launch')
else:
    print(f'NO-GO: {reason}')
