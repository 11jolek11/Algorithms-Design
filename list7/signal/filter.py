import numpy as np
from generate import Signal


class Filter():
    def __init__(self) -> None:
        self._signal = None
        self._signal_values = None
        self._signal_fft = None
        self._time_domain = None
        self._freq_domain = None

    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, new_value: Signal):
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
                mask.append(False)
            else:
                mask.append(True)
        return self._freq_domain[mask], self._signal_fft[mask]
