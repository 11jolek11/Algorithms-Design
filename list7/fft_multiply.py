import numpy as np

def poly_multiply(p, q):
    """
    Multiply two polynomials p and q using FFT.
    """
    # Compute the degree of the product polynomial
    n = len(p) + len(q) - 1
    
    # Compute the FFT of the coefficient sequences of the input polynomials
    P = np.fft.fft(p, n)
    Q = np.fft.fft(q, n)
    
    # Compute the coefficient sequence of the product polynomial by element-wise multiplication of the FFTs
    R = P * Q
    
    # Compute the inverse FFT of the product coefficient sequence to obtain the product polynomial
    r = np.fft.ifft(R).real
    
    return r


if __name__ == '__main__':
    print(poly_multiply([2, 1, 2], [3, 4]))
