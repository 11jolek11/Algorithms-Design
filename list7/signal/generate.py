import numpy as np



class Signal():
    def __init__(self, A:list, a:list, B:list, b:list, value_axis=None, time_axis=None, func_str="") -> None:
        if len(A) != len(a) and len(B) != len(b):
            raise ValueError("Wrong size!")

        self.A = A
        self.a = a
        self.B = B
        self.b = b

        self._time_axis = time_axis
        self._value_axis = value_axis

        if not func_str:
            self._func = f'{A[0]}*np.sin({a[0]}*t) + {B[0]}*np.cos({b[0]}*t)'
        else:
            self._func = func_str

        for i in range(1, len(A)):
            self._func += f' + {A[i]}*np.sin({a[i]}*t)'
 
        for i in range(1, len(B)):
            self._func += f' + {B[i]}*np.cos({b[i]}*t)'
 
        self._lambda_func = lambda t: eval(self._func)
        # self._lambda_func = lambda t: 3*np.sin(2*t) + 2*np.cos(3*t)


    def __str__(self) -> str:
        return self._func


    def generate_array(self, start=0, stop=20, step=0.1, save=True):
        arr = np.empty(int((stop-start)/step))
        time = []
        datapoint = np.arange(start, stop, step)
        for point in range(int((stop-start)/step)): 
            arr[point] = self._lambda_func(datapoint[point])
            time.append(point)
        if save:
            self._value_axis = arr
        return arr, time

