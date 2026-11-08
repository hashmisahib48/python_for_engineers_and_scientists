# Problem 13.2  Half-life of Ba-137m from Geiger counts
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

df = pd.read_csv('ba137m_counts.csv')     # counts per 10 s interval
t = df['t_s'].to_numpy() + 5.0            # mid-interval time, s
c = df['counts'].to_numpy()

def model(t, c0, lam, bkg):
    """Expected counts per interval: decay plus background."""
    return c0 * np.exp(-lam * t) + bkg

p, cov = curve_fit(model, t, c, p0=[c[0], 0.005, 1.0],
                   sigma=np.sqrt(np.maximum(c, 1)),
                   absolute_sigma=True)
c0, lam, bkg = p
u_lam = np.sqrt(cov[1, 1])
t_half = np.log(2) / lam                  # s
u_half = t_half * u_lam / lam
print(f'lambda = {lam:.5f} +/- {u_lam:.5f} 1/s')
print(f'background = {bkg:.1f} counts per 10 s')
print(f'half-life = {t_half:.1f} +/- {u_half:.1f} s'
      f' = {t_half / 60:.3f} min')
r = (c - model(t, c0, lam, bkg)) / np.sqrt(np.maximum(c, 1))
chi2 = np.sum(r**2) / (len(c) - 3)
print(f'reduced chi-square = {chi2:.2f}')
