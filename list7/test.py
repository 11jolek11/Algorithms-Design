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
N = 100
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
# y = 2*np.sin(2*35*np.pi*x) + np.sin(2*20*np.pi*x) + np.sin(2*15*np.pi*x)
y = np.cos(x)
yf = np.fft.fft(y)
# xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
xf = np.fft.fftfreq(N, T)

fig, ax = plt.subplots()
# ax.plot(xf[:N//2], np.abs(yf[:N//2]))
ax.plot(xf, np.abs(yf))

plt.show()
