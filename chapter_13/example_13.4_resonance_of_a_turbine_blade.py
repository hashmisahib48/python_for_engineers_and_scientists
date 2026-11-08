# Example 13.4  Spectrum of a turbine-blade strain-gauge signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

df = pd.read_csv('blade_gauge.csv')   # time s, strain microstrain
t, eps = df['t_s'].to_numpy(), df['strain_ue'].to_numpy()
fs = 1 / (t[1] - t[0])                    # sampling rate, Hz
n = len(eps)
f_rot = 9000 / 60                         # rotor speed, Hz

amp = 2 * np.abs(np.fft.rfft(eps - eps.mean())) / n   # microstrain
freq = np.fft.rfftfreq(n, d=1 / fs)                    # Hz
print(f'fs = {fs:.0f} Hz, resolution = {fs / n:.2f} Hz')
for k in np.flatnonzero(amp > 4.0):
    print(f'peak {freq[k]:7.1f} Hz  {amp[k]:5.1f} ue  '
          f'engine order {freq[k] / f_rot:5.2f}')

k = np.argmax(amp)
E = 200e9                                 # Young's modulus, Pa
print(f'stress amplitude = {E * amp[k] * 1e-12:.1f} MPa')

# band-pass filter, 4th order Butterworth, +/- 60 Hz round the peak
band = [freq[k] - 60, freq[k] + 60]
sos = signal.butter(4, band, btype='bandpass', fs=fs, output='sos')
eps_f = signal.sosfiltfilt(sos, eps)
print(f'filtered amplitude = {np.sqrt(2) * eps_f.std():.1f} ue')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5.4, 4.0))
ax1.plot(t * 1000, eps, lw=0.7, label='measured')
ax1.plot(t * 1000, eps_f, lw=1.4, label='band-pass')
ax1.set(xlim=(0, 30), ylim=(-150, 260), xlabel='Time (ms)',
        ylabel='Strain (µε)')
ax1.legend(loc='upper right', ncol=2)
ax2.plot(freq, amp, lw=0.9)
ax2.set(xlim=(0, 2500), xlabel='Frequency (Hz)',
        ylabel='Amplitude (µε)')
fig.tight_layout()
plt.show()
