# Problem 9.4: xenon-135 after a reactor shutdown, by eigenvalues
import numpy as np

LAM_I = np.log(2) / (6.58 * 3600)   # I-135 decay constant, 1/s
LAM_X = np.log(2) / (9.14 * 3600)   # Xe-135 decay constant, 1/s
G_I, G_X = 0.0639, 0.00237          # fission yields, -
SIG_X = 2.65e-18                    # Xe-135 absorption, cm^2
PHI = 3.0e13                        # flux, neutrons/(cm^2 s)

# equilibrium before shutdown, per unit fission rate density
n0 = np.array([G_I / LAM_I, (G_I + G_X) / (LAM_X + SIG_X * PHI)])
a = np.array([[-LAM_I, 0.0],        # dN/dt = A N after shutdown
              [LAM_I, -LAM_X]])
w, v = np.linalg.eig(a)             # eigenvalues, eigenvectors
w, v = w.real, v.real               # both are real for this A
c = np.linalg.solve(v, n0)          # n0 = v @ c

t = np.linspace(0.0, 72.0, 7201)    # hours after shutdown
mode = np.exp(w[:, np.newaxis] * t * 3600)   # (2, 7201)
n = v @ (c[:, np.newaxis] * mode)   # (2, 7201): iodine, xenon
xe = n[1] / n0[1]                   # xenon relative to start

k = xe.argmax()
late = t[xe > 1.0].max()            # last time above the start
ts = t * 3600                       # s, for the Bateman check
bat = (n0[1] * np.exp(-LAM_X * ts) + LAM_I * n0[0] / (LAM_X - LAM_I)
       * (np.exp(-LAM_I * ts) - np.exp(-LAM_X * ts))) / n0[1]
print(f'Eigenvalues (1/h): {w * 3600}')
print(f'Equilibrium I/Xe ratio: {n0[0] / n0[1]:.3f}')
print(f'Xenon peak: {xe[k]:.3f} x start, at {t[k]:.2f} h')
print(f'Xenon above its start value until {late:.2f} h')
print(f'Xenon after 72 h: {xe[-1]:.4f} x start')
print(f'Largest gap to Bateman: {np.abs(xe - bat).max():.1e}')
