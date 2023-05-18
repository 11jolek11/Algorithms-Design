from generate import CreateSignal, Signal
from filter import Filter
import numpy as np
import matplotlib.pyplot as plt


def clear_plot(signal: Signal):
    fig, axs = plt.subplots(2)
    fig.tight_layout()

    # p = Signal(A, a, B, b)
    # print(str(p))
    # data, _ = p.generate_array()
    axs[0].plot(*signal.generate())
    axs[0].title.set_text("Clear signal")

    t, _ = signal.generate()
    print(t[1]-t[0])
    print(len(t))
    print(t[-1])

    freq_domain, freq_data = signal.make_fft()
    length = len(freq_domain)

    freq_domain, freq_data = freq_domain, np.abs(freq_data)/length

    # freq_domain, freq_data = freq_domain[0:int((length/2) + 1)], 2*freq_data[0:int((length/2) + 1)]

    axs[1].plot(freq_domain, freq_data, color="tab:orange")
    axs[1].title.set_text("Clear signal freq")
    # plt.savefig("test.png")
    plt.show()
# ###################################################################################################################
    # fig, axs = plt.subplots(2)
    # fig.tight_layout()

    # axs[0].plot(freq_domain, freq_data)
    # axs[0].title.set_text("Freq before")

    # f, _ = signal.make_fft()
    # print(f[1]-f[0])
    # print(len(f))
    # print(f[-1])

    # freq_domain, freq_data = signal.make_fft()
    # length = len(freq_domain)

    # freq_domain, freq_data = freq_domain, np.abs(freq_data)/length

    # freq_domain, freq_data = freq_domain[0:int((length/2) + 1)], 2*freq_data[0:int((length/2) + 1)]

    # axs[1].plot(freq_domain, freq_data, color="tab:orange")
    # axs[1].title.set_text("Freq after")
    # # plt.savefig("test.png")
    # plt.show()


def filtered_plot(data):
    fig, axs = plt.subplots(2)
    fig.tight_layout()

    axs[0].plot(data)
    axs[0].title.set_text("Filtered signal")

    axs[1].plot(np.abs(np.fft.fft(data)), color="tab:orange")
    axs[1].title.set_text("Filtered signal freq")
    plt.savefig("fil.png")


if __name__ == "__main__":
    # creator = CreateSignal([2], [3], [3], [2])
    creator = CreateSignal([1, 4], [2, 6], [0], [0])
    print(str(creator))
    p = creator.create()
    clear_plot(p)
    # to_remove = list(range(26))
    # # to_remove = np.arange(0, 20, 0.1)[:25]
    # filter = Filter()
    # filter.signal = data
    # filter.out(to_remove)
    # filtered_plot(filter.signal)
