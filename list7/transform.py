import numpy as np
from math import cos, sin, log, pi
from cmath import exp



def fft_recursive(x):
    """
    Compute the one-dimensional discrete Fourier Transform of the signal x using the recursive FFT algorithm.
    """
    # Compute the length of the input signal x
    N = len(x)
    
    # If the signal has only one element, return it
    if N == 1:
        return x
    
    # Split the signal into even and odd parts
    even = fft_recursive(x[::2])
    odd = fft_recursive(x[1::2])
    
    # Compute the values of the DFT at each frequency using the butterfly method
    k = np.arange(N)
    t = np.exp(-2j * np.pi * k / N)
    DFT = np.concatenate([even + t[:N//2] * odd, even + t[N//2:] * odd])
    
    return DFT


def bit_reverse(x):
    N = len(x)
    temp = [i for i in range(N)]
    for k in range(N):
        b = sum(
                1 << int(log(N, 2)) - 1 -
                i for i in range(int(log(N, 2))) if k >> i & 1
                )
        temp[k] = x[b]
        temp[b] = x[k]
    return temp


def cooley_tucker(x):
    """
    Compute the FFT using Cooley Tucker algorithm.
    """
    N = len(x)
    X = bit_reverse(x)

    for i in range(1, int(log(N, 2)) + 1):
        stride = 2 ** i
        w = exp(-2.0j * pi / stride)
        for j in range(0, N, stride):
            v = 1
            for k in range(stride // 2):
                X[k + j + stride // 2] = X[k + j] - v * X[k + j + stride // 2]
                X[k + j] -= X[k + j + stride // 2] - X[k + j]
                v *= w
    return X


def ifdft(X: list[complex]):
    x = [0 for _ in range(len(X))]
    for n in range(len(X)):
        for k in range(len(X)):
            theta = (2 * pi * k * n)/len(x)
            x[n] += X[k].real * cos(theta) + X[k].imag * sin(theta)
        x[n] /= len(X)
    return x


import numpy as np

def ifft(X):
    N = len(X)
    x = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j*np.pi*k*n/N)
        x[n] /= N
    return x


#Driver code
if __name__ == "__main__":
    x = np.array([0, 1, 2, 3])
    X = cooley_tucker(x)
    print(X)
    print("^^^^^^")
    print(ifft(X))
    print("$$$$$4444")
    test = np.fft.fft(x)
    print("**********")
    print(cooley_tucker(X))
    print()
    print(test)
    print(np.fft.ifft(test))

