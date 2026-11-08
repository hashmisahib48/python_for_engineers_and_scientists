# Escape velocity from the surfaces of Earth and Mars
# Data: NASA planetary fact sheets; G is the CODATA 2018 value
G = 6.67430e-11          # gravitational constant, m^3/(kg s^2)

M_earth = 5.9722e24      # mass of Earth, kg
R_earth = 6.3710e6       # mean radius of Earth, m
M_mars = 0.64169e24      # mass of Mars, kg
R_mars = 3.3895e6        # mean radius of Mars, m

# v = sqrt(2 G M / R); raising to the power 0.5 takes the square root
v_earth = (2 * G * M_earth / R_earth) ** 0.5    # m/s
v_mars = (2 * G * M_mars / R_mars) ** 0.5       # m/s

print("Escape velocity from Earth:", round(v_earth / 1000, 2), "km/s")
print("Escape velocity from Mars: ", round(v_mars / 1000, 2), "km/s")
print("Ratio Earth/Mars:", round(v_earth / v_mars, 2))
