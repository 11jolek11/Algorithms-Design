# '''
# Basic implementation of Cooley-Tukey FFT algorithm in Python
# Reference:
# https://en.wikipedia.org/wiki/Fast_Fourier_transform
# '''

# __author__ = 'Darko Lukic'
# __email__ = 'lukicdarkoo@gmail.com'


# import numpy as np
# import matplotlib.pyplot as plt


# SAMPLE_RATE = 8192
# N = 128


# def fft(x):
#     X = list()
#     for k in range(N):
#         window = 1
#         X.append(x[k] * window)
#     fft_rec(X)
#     return X


# def fft_rec(X):
#     N = len(X)
#     if N <= 1:
#         return x
#     even = np.array(X[0:N:2])
#     odd = np.array(X[1:N:2])
#     fft_rec(even)
#     fft_rec(odd)
#     for k in range(N//2):
#         t = np.exp(-2j * np.pi * k / N) * odd[k]
#         X[k] = even[k] + t
#         X[N//2 + k] = even[k] - t


# x_values = np.arange(0, N, 1)

# # 32 - 256Hz
# x = np.sin((2*np.pi*x_values))
# # 64 - 128Hz
# x += np.sin((2*np.pi*x_values))

# X = fft(x)

# # Plotting
# _, plots = plt.subplots(2)

# # Plot in time domain
# plots[0].plot(x)

# # Plot in frequent domain
# powers_all = np.abs(np.divide(X, N/2))
# powers = powers_all[0:N//2]
# frequencies = np.divide(np.multiply(SAMPLE_RATE, np.arange(0, N//2)), N)
# plots[1].plot(frequencies, powers)

# # Show plots
# plt.savefig("test.png")

# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.fftpack
# import numpy as np

# # Number of samplepoints
# N = 500
# # sample spacing
# T = 1.0 / 800.0
# # x = np.linspace(0.0, N*T, N)
# x = np.linspace(0, N*T, N)

# # y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
# y = 2*np.sin(2*35*np.pi*x) + np.sin(2*20*np.pi*x) + np.sin(2*15*np.pi*x)
# yf = np.fft.fft(y)
# xf = np.fft.fftfreq(N, T)
# xf = np.fft.fftshift(xf)
# print(yf.shape)
# print(xf.shape)

# # xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# fig, ax = plt.subplots()
# # ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
# ax.plot(xf, np.abs(yf))

# plt.savefig("test.png")

import numpy as np
import matplotlib.pyplot as plt

# Number of samplepoints
N = 200
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
# y = 2*np.sin(2*35*np.pi*x) + np.sin(2*20*np.pi*x) + np.sin(2*15*np.pi*x)
# y = np.cos(x)
y = 1*np.sin(2*np.pi*x) + 0*np.cos(0*x) + 4*np.sin(6*np.pi*x)
plt.plot(x, y)
plt.show()
yf = np.fft.rfft(y)
# xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
xf = np.fft.rfftfreq(N, T)

fig, ax = plt.subplots()
# ax.plot(xf[:N//2], np.abs(yf[:N//2]))
ax.plot(xf, np.abs(yf))

plt.show()

# ######################################################################################################################3

# Fs = 2000
# tstep = 1 / Fs

# f0 = 100

# N = int(10*Fs/f0)

# t = np.linspace(0, (N-1)*tstep, N)
# fstep = Fs/N
# f = np.linspace(0, (N-1)*fstep, N)

# y = 1*np.sin(2*np.pi*f0*t) + 4 * np.sin(2*np.pi*3*f0*t)

# X = np.fft.fft(y)

# X_mag = np.abs(X)/N

# f_plot = f[0:int(N/2+1)]
# X_mag_plot = 2*X_mag[0:int(N/2+1)]

# X_mag_plot[0] = X_mag_plot[0] / 2

# fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
# ax1.plot(t, y, '.-')
# ax2.plot(f_plot, X_mag_plot, '.-')
# plt.show()



LP = 128

CP = 1 / LP

# MP = np.arange(0, (N-1)*CP, CP)
MP = np.arange(CP, 1, CP)

fstep = 1
# CZ = np.arange(0, LP/2 - 1, fstep)
CZ = np.arange(0, LP - 1, fstep)

print(CZ.shape)
# CZ = np.fft.fftshift(CZ)[0:LP//2]

# y = 1*np.sin(2*np.pi*t) + 4 * np.sin(2*np.pi*3*t)
S = 2*np.sin(2*np.pi*35*MP) + np.sin(2*np.pi*20*MP) + np.sin(2*np.pi*15*MP)

Y = np.abs(np.fft.fft(S))
Y = np.fft.fftshift(Y)

print(CZ.shape)
print(Y.shape)


plt.plot(CZ, Y)
plt.show()

# X_mag = np.abs(X)/N

# f_plot = f[0:int(N/2+1)]
# X_mag_plot = 2*X_mag[0:int(N/2+1)]

# X_mag_plot[0] = X_mag_plot[0] / 2

# fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
# ax1.plot(t, y, '.-')
# ax2.plot(f_plot, X_mag_plot, '.-')
# plt.show()
