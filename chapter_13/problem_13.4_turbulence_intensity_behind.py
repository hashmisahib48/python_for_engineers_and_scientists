# Problem 13.4  Turbulence intensity from a hot-wire record with hum
import numpy as np
import pandas as pd
from scipy import signal

df = pd.read_csv('hotwire.csv')           # time s, velocity m/s
u = df['u_ms'].to_numpy()
fs = 1 / (df['t_s'][1] - df['t_s'][0])    # Hz
n = len(u)

def report(label, x):
    """Print mean, rms fluctuation and turbulence intensity."""
    u_mean, u_rms = x.mean(), x.std()
    tu = 100 * u_rms / u_mean             # turbulence intensity, %
    print(f'{label:8s} U = {u_mean:.3f} m/s  '
          f'u_rms = {u_rms:.3f} m/s  Tu = {tu:.2f} %')

amp = 2 * np.abs(np.fft.rfft(u - u.mean())) / n
freq = np.fft.rfftfreq(n, d=1 / fs)
k = np.argmax(amp)
print(f'largest spectral line: {freq[k]:.2f} Hz, '
      f'{amp[k]:.3f} m/s')
report('raw', u)

b, a = signal.iirnotch(freq[k], Q=30, fs=fs)   # notch, hum
u_clean = signal.filtfilt(b, a, u)
report('notched', u_clean)
hum = u - u_clean
print(f'removed hum amplitude = {np.sqrt(2) * hum.std():.3f} m/s')

# uncertainty of the mean: samples are correlated, so use
# the mean of 40 blocks of 0.1 s as independent estimates
blocks = u_clean.reshape(40, -1).mean(axis=1)
u_se = blocks.std(ddof=1) / np.sqrt(40)
print(f'U = {u_clean.mean():.3f} +/- {2 * u_se:.3f} m/s (~95 %)')
