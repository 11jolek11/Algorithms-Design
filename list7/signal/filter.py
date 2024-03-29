import numpy as np
from generate import Signal


class Filter():
    def __init__(self) -> None:
        self._signal = None
        self._signal_values = None
        self._signal_fft = None
        self._time_domain = None
        self._freq_domain = None
        self.filtered = False

    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, new_value: Signal):
        if self.filtered:
            raise Exception("Cannot change the Signal")
        self._signal = new_value
        self._time_domain, self._signal_values = self._signal.generate()
        self._freq_domain, self._signal_fft = self._signal.make_fft()

    @signal.getter
    def signal(self):
        return self._signal_values

    def out(self, frequencies: list[float]):
        mask = []
        for i in range(len(self._freq_domain)):
            if self._freq_domain[i] in frequencies:
                mask.append(i)
        np.put(self._signal_fft, mask, 0.0)
        self._signal_values = np.fft.ifft(self._signal_fft)
        self.filtered = True
        return (self._freq_domain, self._signal_fft), ()
