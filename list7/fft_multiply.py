import numpy as np
import transform

def poly_multiply_3(p, q):
    """
    Multiply two polynomials p and q using FFT.
    """
    n = len(p) + len(q) - 1

    if len(p) < n:
        p = [*[0.]*(n-len(p)), *p]
    if len(q) < n:
        q = [*[0. + 0.j]*(n -len(q)), *q]

    P = transform.cooley_tukey(p)
    Q = transform.cooley_tukey(q)

    # if len(P) < len(Q):
    #     P = [*[0. + 0.j]*(len(Q)-len(P)), *P]

    # if len(P) > len(Q):
    #     print("Hello")
    #     Q = [*[0. + 0.j]*(len(P)-len(Q)), *Q]
    # if len(P) < n:
    #     P = [*[0. + 0.j]*(n-len(P)), *P]
    # if len(Q) < n:
    #     Q = [*[0. + 0.j]*(n -len(Q)), *Q]

    R = []

    print(len(P))
    print(len(Q))

    for i in range(n):
        R.append(P[i]*Q[i])

    r = transform.ifft(R)

    return r.real


# def poly_multiply(p, q):
#     """
#     Multiply two polynomials p and q using FFT.
#     """
#     # Compute the degree of the product polynomial
#     n = len(p) + len(q) - 1

#     # Compute the FFT of the coefficient sequences of the input polynomials
#     P = np.fft.fft(p, n)
#     Q = np.fft.fft(q, n)
#     # Compute the coefficient sequence of the product polynomial
#     # by element-wise multiplication of the FFTs
#     R = P * Q

#     # Compute the inverse FFT of the product coefficient sequence to
#     # obtain the product polynomial
#     r = np.fft.ifft(R).real

#     return r


# if __name__ == '__main__':
#     print(poly_multiply([2, 1, 2], [3, 4]))

def poly_multiply(p, q):
    """
    Multiply two polynomials p and q using FFT.
    """
    n = len(p) + len(q) - 1

    P = np.fft.fft(p, n)
    Q = np.fft.fft(q, n)


    R = P * Q

    r = np.fft.ifft(R).real

    return r


if __name__ == '__main__':
    print(poly_multiply([2, 1, 2], [3, 4]))
