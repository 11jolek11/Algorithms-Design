import numpy as np



def fft(x):
    """
    Compute the one-dimensional discrete Fourier Transform of the signal x using the recursive FFT algorithm.
    """
    # Compute the length of the input signal x
    N = len(x)
    
    # If the signal has only one element, return it
    if N == 1:
        return x
    
    # Split the signal into even and odd parts
    even = fft(x[::2])
    odd = fft(x[1::2])
    
    # Compute the values of the DFT at each frequency using the butterfly method
    k = np.arange(N)
    t = np.exp(-2j * np.pi * k / N)
    DFT = np.concatenate([even + t[:N//2] * odd, even + t[N//2:] * odd])
    
    return DFT

#Driver code
if __name__ == "__main__":
    x = np.array([1, 2, 3, 4])
    X = fft(x)
    print(X)

