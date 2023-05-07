from math import pi, e
import numpy as np


def cooley_tukey(x):
    """
    Cooley-Tukey implementation
    """
    N = len(x)
    if N == 1:
        return [
            x[0],
        ]

    X = [0 for _ in range(N)]
    even = cooley_tukey(x[0::2])
    odd = cooley_tukey(x[1::2])
    for k in range(N // 2):
        omega = e ** (-2j * pi * k / N)
        X[k] = even[k] + omega * odd[k]
        X[k + N // 2] = even[k] - omega * odd[k]
    return X


def ifft(x):
    """
    Inverse Fourier transform using conjungate
    """
    # Take the complex conjugate of the input array
    x_conj = np.conjugate(x)

    # Apply the forward FFT on the conjugate input array
    y_conj = np.fft.fft(x_conj)

    # Take the complex conjugate of the resulting array to obtain the inverse FFT
    final = np.conjugate(y_conj)
    # Divide the resulting array by the length of the input array
    final /= len(x)

    return final


if __name__ == "__main__":
    x_values = np.arange(0, 128, 1)

    x_test = np.sin((2 * np.pi * x_values / 32.0))
    x_test += np.sin((2 * np.pi * x_values / 64.0))
    x_test = x_test.tolist()

    X_in = cooley_tukey(x_test)

    X_test = np.fft.fft(x_test)

    print("Test of cooley_tukey")
    print(np.allclose(X_in, X_test))

    print("Test of ifft")
    print(np.allclose(ifft(X_test), x_test))
    print(np.allclose(ifft(X_test), np.fft.ifft(X_test)))
