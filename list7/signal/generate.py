import numpy as np
from typing import Callable


class Signal():
    def __init__(self, func: Callable[[np.ndarray], np.ndarray],
                 sampling_freq: int,
                 signal_freq: int) -> None:
        self._gen_func = func
        self._sampling_freq = sampling_freq
        self._signal_freq = signal_freq
        self._time_interval = 1/self._sampling_freq
        self.number_of_samples = int(10*self._sampling_freq//self._signal_freq)
        self._freq_interval = self._sampling_freq / self.number_of_samples
        self._time_domain = np.linspace(0,
                                        (self.number_of_samples - 1)*self._time_interval,
                                        self.number_of_samples) # use
        # self._freq_domain = np.linspace(0,
        #                                 (self.number_of_samples - 1)*self._freq_interval,
        #                                 self.number_of_samples)
        self._freq_domain = np.fft.rfftfreq(self.number_of_samples, self._freq_interval) # use
        # self._freq_domain = np.fft.fftfreq(self.number_of_samples, self._freq_interval)
        self.signal = np.empty(self._time_domain.size)
        self.transform = np.empty(self._freq_domain.size)

    def generate(self):
        self.signal = self._gen_func(self._signal_freq*self._time_domain)
        return self._time_domain, self.signal

    def make_fft(self):
        # self.transform = np.fft.fft(self.signal)
        self.transform = np.fft.rfft(self.signal)
        return self._freq_domain, self.transform


class CreateSignal():
    def __init__(self,
                 A: list,
                 a: list,
                 B: list,
                 b: list,
                 func_str="") -> None:
        if len(A) != len(a) and len(B) != len(b):
            raise ValueError("Wrong size!")

        self.A = A
        self.a = a
        self.B = B
        self.b = b

        if not func_str:
            self._gen_func = f'{A[0]}*np.sin({a[0]}*t) + {B[0]}*np.cos({b[0]}*t)'
        else:
            self._gen_func = func_str

        for i in range(1, len(A)):
            self._gen_func += f' + {A[i]}*np.sin({a[i]}*t)'

        for i in range(1, len(B)):
            self._gen_func += f' + {B[i]}*np.cos({b[i]}*t)'

        self._lambda_func = lambda t: eval(self._gen_func)

    def __str__(self) -> str:
        return self._gen_func

    def create(self, sampling_f=2000, signal_f=100):
        return Signal(self._lambda_func, sampling_f, signal_f)
