# Wykres cz. składowych


import numpy as np
import matplotlib.pyplot as plt


LP = 128

CP = 1 / LP

MP = np.arange(0, (LP-1)*CP, CP)

fstep = 1
CZ = np.arange(0, LP/2 - 1, fstep)

S = 2*np.sin(2*np.pi*35*MP) + np.sin(2*np.pi*20*MP) + np.sin(2*np.pi*15*MP)

Y = np.abs(np.fft.fft(S) / (LP/2))[:CZ.shape[0]]

fig, axs = plt.subplots(2)
fig.tight_layout()

axs[0].plot(MP, S)
axs[0].title.set_text("Signal")

axs[1].plot(CZ, Y, color="tab:orange")
axs[1].title.set_text("Freq")
plt.show()
