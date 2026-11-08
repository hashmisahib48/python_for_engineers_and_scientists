# Engineering Lab  U-235 fissioned per day by a 1000 MW plant
# Constants: CODATA 2018.  Atomic mass of U-235: NIST.
C = 299792458.0             # speed of light, m/s (exact)
EV = 1.602176634e-19        # one electronvolt, J (exact)
N_A = 6.02214076e23         # Avogadro constant, 1/mol (exact)
M_U235 = 235.0439301        # molar mass of U-235, g/mol

# %% Step 1: the plant
p_elec = 1000e6             # electrical output, W
eta = 0.33                  # thermal efficiency, -
day = 24 * 3600             # seconds in one day, s

# %% Step 2: heat needed in one day
p_heat = p_elec / eta               # reactor heat output, W
q_day = p_heat * day                # heat per day, J

# %% Step 3: fissions and uranium mass
e_fis = 200e6 * EV                  # energy per fission, J
n_fis = q_day / e_fis               # fissions per day
m_u235 = n_fis / N_A * M_U235 / 1000    # U-235 fissioned, kg

# %% Step 4: comparisons
m_coal = q_day / 29.3e6             # coal equivalent, kg
dm = q_day / C**2                   # mass turned into energy, kg

# %% Step 5: results
print('Reactor heat output (MW):', round(p_heat / 1e6))
print('Heat per day (TJ):', round(q_day / 1e12, 1))
print('Fissions per day:', n_fis)
print('U-235 fissioned per day (kg):', round(m_u235, 2))
print('Coal equivalent per day (tonnes):', round(m_coal / 1000))
print('Mass converted to energy (g):', round(dm * 1000, 2))
print('Coal / uranium mass ratio:', round(m_coal / m_u235))
