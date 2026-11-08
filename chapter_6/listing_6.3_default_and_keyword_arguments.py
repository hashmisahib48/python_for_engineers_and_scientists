# Listing 6.3  Default and keyword arguments: thin-walled vessels


def hoop_stress(p, r, t, eff=1.0):
    sigma = p * r / (eff * t)   # hoop stress, Pa
    return sigma


p_air = 1.0e6       # gauge pressure in an air receiver, Pa
r_tank = 0.30       # mean radius, m
t_wall = 0.006      # wall thickness, m

s1 = hoop_stress(p_air, r_tank, t_wall)             # eff = 1.0
s2 = hoop_stress(p_air, r_tank, t_wall, 0.85)       # positional
s3 = hoop_stress(p_air, r_tank, t_wall, eff=0.70)   # keyword
s4 = hoop_stress(t=t_wall, eff=0.85, p=p_air, r=r_tank)

print(f'Seamless shell:       {s1 / 1e6:5.1f} MPa')
print(f'Welded, eff = 0.85:   {s2 / 1e6:5.1f} MPa')
print(f'Welded, eff = 0.70:   {s3 / 1e6:5.1f} MPa')
print(f'All by keyword:       {s4 / 1e6:5.1f} MPa')
