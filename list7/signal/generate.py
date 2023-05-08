import numpy as np
from typing import Callable


class Signal():
    def __init__(self, func: Callable[[np.ndarray], np.ndarray],
                 number_of_samples: int) -> None:
        self._gen_func = func
        # liczba probek LP
        self.number_of_samples = number_of_samples
        # czestosc probek CP
        self._sampling_freq = 1/self.number_of_samples
        # momenty probkowania MP
        self._probe_moments = np.arange(0, (self.number_of_samples - 1)*self._sampling_freq + 1, self._sampling_freq)

        # czestotliwosc CZ
        # self._freq_domain = np.arange(0, self.number_of_samples/2, 1)
        self._freq_domain = np.fft.rfftfreq(self.number_of_samples, 1/self.number_of_samples)
        print(self._freq_domain[0])
        print(self._freq_domain[1] - self._freq_domain[0])


        self.signal = np.empty(self._probe_moments.size)
        self.transform = np.empty(self._freq_domain.size)

    def generate(self):
        self.signal = self._gen_func(self._probe_moments)
        return self._probe_moments, self.signal

    def make_fft(self):
        self.transform = np.fft.fft(self.signal)
        return self._freq_domain, np.abs(self.transform[0:int(self.number_of_samples/2) + 1])/se
        # return self._freq_domain, 2*np.abs(self.transform[0:int(self.number_of_samples/2)])


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

    def create(self, number_of_samples=128):
        return Signal(self._lambda_func, number_of_samples)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    creator = CreateSignal(['2', '1', '1'], ['70*np.pi', '40*np.pi', '30*np.pi'], ['0'], ['0'])
    print(str(creator))
    p = creator.create()
    plt.plot(*p.generate())
    plt.show()
    plt.plot(*p.make_fft(), '.-', color="tab:orange")
    plt.show()
