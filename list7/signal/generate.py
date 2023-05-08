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
        self.number_of_samples = int(self._sampling_freq//self._signal_freq)
        self._freq_interval = self._sampling_freq / self.number_of_samples
        self._time_domain = np.linspace(0,
                                        (self.number_of_sample - 1)*self._time_interval,
                                        self.number_of_samples)
        self._freq_domain = np.linspace(0,
                                        (self.number_of_sample - 1)*self._freq_interval,
                                        self.number_of_samples)
        self.signal = np.empty(self._time_domain.size)
        self.transform = np.empty(self._freq_domain.size)

    def generate(self):
        self.signal = self._gen_func(self._signal_freq*self._time_domain)

    def make_fft(self):
        self.transform = np.fft.fft(self.signal)


class CreateSignal():
    def __init__(self,
                 A: list,
                 a: list,
                 B: list,
                 b: list,
                 value_axis=None,
                 time_axis=None,
                 func_str="") -> None:
        if len(A) != len(a) and len(B) != len(b):
            raise ValueError("Wrong size!")

        self.A = A
        self.a = a
        self.B = B
        self.b = b

        self._time_axis = time_axis
        self._value_axis = value_axis

        if not func_str:
            self._gen_func = f'{A[0]}*np.sin({a[0]}*t) + {B[0]}*np.cos({b[0]}*t)'
        else:
            self._gen_func = func_str

        for i in range(1, len(A)):
            self._gen_func += f' + {A[i]}*np.sin({a[i]}*t)'

        for i in range(1, len(B)):
            self._gen_func += f' + {B[i]}*np.cos({b[i]}*t)'

        self._lambda_func = lambda t: eval(self._gen_func)
        # self._lambda_func = lambda t: 3*np.sin(2*t) + 2*np.cos(3*t)

    def __str__(self) -> str:
        return self._gen_func

    # def generate_array(self, start=0, stop=20, step=0.1, save=True):
    #     arr = np.empty(int((stop-start)/step))
    #     time = []
    #     datapoint = np.arange(start, stop, step)
    #     for point in range(int((stop-start)/step)):
    #         arr[point] = self._lambda_func(datapoint[point])
    #         time.append(point)
    #     if save:
    #         self._value_axis = arr
    #     return arr, time
