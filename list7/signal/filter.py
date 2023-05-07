import numpy as np


class Filter():
    def __init__(self) -> None:
        self._signal = None
        self._signal_fft = None

    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, new_value: np.ndarray):
        self._signal = new_value
        self._signal_fft = np.fft.fft(self._signal)

    @signal.getter
    def signal(self):
        return self._signal

    def out(self, frequencies: list):
        # TODO: znajdz lepszy sposob na reprezentacje czestotliwosci do
        # usuniecia

        # frequencies: numery indeksow w do usuniecia
        self._signal_fft = np.delete(self._signal_fft, frequencies)
        self._signal = np.fft.ifft(self._signal_fft)
