from generate import Signal
from filter import Filter
import random
import numpy as np
import matplotlib.pyplot as plt



def clear_plot(data):
    fig, axs = plt.subplots(2)
    fig.tight_layout()

    # p = Signal(A, a, B, b)
    # print(str(p))
    # data, _ = p.generate_array()
    axs[0].plot(data)
    axs[0].title.set_text("Clear signal")

    axs[1].plot(np.abs(np.fft.fft(data)), color="tab:orange")
    axs[1].title.set_text("Clear signal freq")
    plt.savefig("test.png")



def filtered_plot(data):
    fig, axs = plt.subplots(2)
    fig.tight_layout()

    axs[0].plot(data)
    axs[0].title.set_text("Filtered signal")

    axs[1].plot(np.abs(np.fft.fft(data)), color="tab:orange")
    axs[1].title.set_text("Filtered signal freq")
    plt.savefig("fil.png")


if __name__ == "__main__":
    p = Signal([2], [3], [3], [2])
    print(str(p))
    data, _ = p.generate_array()
    clear_plot(data)
    to_remove = list(range(26))
    # to_remove = np.arange(0, 20, 0.1)[:25]
    filter = Filter()
    filter.signal = data
    filter.out(to_remove)
    filtered_plot(filter.signal)

