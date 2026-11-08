# %% Inputs: a test payload thrown by a pneumatic launcher
g = 9.80665        # standard gravity, m/s^2
vx = 40.0          # horizontal launch velocity, m/s
vy = 30.0          # vertical launch velocity, m/s

# %% Flight on level ground, air drag neglected
t_flight = 2 * vy / g              # time of flight, s
x_range = vx * t_flight            # horizontal range, m
h_max = vy**2 / (2 * g)            # peak height, m
v0 = (vx**2 + vy**2) ** 0.5        # launch speed, m/s

# %% Report
print("Launch speed:", v0, "m/s")
print("Time of flight:", round(t_flight, 3), "s")
print("Range:", round(x_range, 1), "m")
print("Peak height:", round(h_max, 1), "m")
