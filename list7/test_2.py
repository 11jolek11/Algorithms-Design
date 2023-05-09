import numpy as np
import matplotlib.pyplot as plt

A = [2, 1, 1]
a = ['2*np.pi*35', '2*np.pi*20', '2*np.pi*15']
B = [0]
b = [0]

A = [2, 4]
a = ['2*np.pi', 'np.pi*20']
B = [0]
b = [0]

_lambda_func = None

_gen_func = f'{A[0]}*np.sin({a[0]}*t) + {B[0]}*np.cos({b[0]}*t)'

for i in range(1, len(A)):
    _gen_func += f' + {A[i]}*np.sin({a[i]}*t)'
for i in range(1, len(B)):
    _gen_func += f' + {B[i]}*np.cos({b[i]}*t)'

print(_gen_func)

_lambda_func = lambda t: eval(_gen_func)

LP = 128

CP = 1 / LP

MP = np.arange(CP, 1, CP)

fstep = 1

S = _lambda_func(MP)

# CZ = np.arange(0, LP - 1, fstep)
CZ = np.arange(0, LP/2 - 1, fstep)

Y = np.fft.fft(S)

fig, axs = plt.subplots(2)
axs[0].plot(MP, S)
axs[1].plot(CZ, np.abs(Y)[:CZ.shape[0]], color="tab:orange")
plt.show()

Y_to_plot = np.abs(Y)[:CZ.shape[0]]

Y = np.fft.fftshift(Y)

frequencies = [LP//2 - 25, LP//2 + 36]
for frequency in frequencies:
    Y[frequency] = 0

# Y[:CZ.shape[0]] = Y[:CZ.shape[0]]*(np.absolute(CZ) < 2)
# TODO: imlement me!
# Y = Y*(np.absolute(CZ) < 2)
print(Y.shape)
Y = np.fft.fftshift(Y)

S_NEW = np.fft.ifft(Y).real

Y = np.fft.fft(S_NEW)

plt.plot(CZ, Y_to_plot, color="tab:orange", label="Old")
plt.plot(CZ, np.abs(Y)[:CZ.shape[0]], label="New")
plt.legend()
plt.show()

plt.plot(MP, S, label="Old")
plt.plot(MP, S_NEW, color="tab:red", label="New")
plt.legend()
plt.show()
