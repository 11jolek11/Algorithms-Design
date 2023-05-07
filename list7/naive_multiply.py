# def multiply(a: list, b: list):
#     result = [0 for _ in range(len(a) + len(b) - 1)]
#     for ind1, num1 in enumerate(a):
#         for ind2, num2 in enumerate(b):
#             result[ind1 + ind2] += num2*num1
#     return result

# def multiply(a: list, b: list):
#     result = [0 for _ in range(len(a) + len(b) - 1)]
#     for k in range(len(b)):
#         for l in range(k):
#             result[k] += a[l]*b[k-l]
#     return result
def multiply(A, B):
    m = len(A)
    n = len(B)
  
    prod = [0] * (m + n - 1)
            
    for i in range(m):
        for j in range(n):
            prod[i + j] += A[i] * B[j]
    return prod


if __name__ == "__main__":
    print(multiply([3, 2], [1, 3, 1]))
