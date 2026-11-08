# Problem 13.3  Natural frequency and damping of a wing model
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

df = pd.read_csv('ringdown.csv')          # time s, acceleration g
t = df['t_s'].to_numpy()
a = df['accel_g'].to_numpy()
fs = 1 / (t[1] - t[0])                    # Hz

# step 1: FFT peak gives a first guess of the frequency
amp = 2 * np.abs(np.fft.rfft(a)) / len(a)
freq = np.fft.rfftfreq(len(a), d=1 / fs)
f_fft = freq[np.argmax(amp)]
print(f'FFT peak: {f_fft:.2f} Hz (resolution {fs / len(a):.2f} Hz)')

# step 2: fit a decaying cosine, starting from the FFT guess
def ring(t, a0, zeta, fn, phi):
    wn = 2 * np.pi * fn                   # rad/s
    wd = wn * np.sqrt(1 - zeta**2)
    return a0 * np.exp(-zeta * wn * t) * np.cos(wd * t + phi)

p0 = [a.max(), 0.02, f_fft, 0.0]
p, cov = curve_fit(ring, t, a, p0=p0)
u = np.sqrt(np.diag(cov))
print(f'natural frequency = {p[2]:.3f} +/- {u[2]:.3f} Hz')
print(f'damping ratio     = {p[1]:.5f} +/- {u[1]:.5f}')
print(f'quality factor Q  = {1 / (2 * p[1]):.0f}')
t_half = np.log(2) / (p[1] * 2 * np.pi * p[2])
print(f'amplitude halves every {t_half:.2f} s')
