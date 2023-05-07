# def multiply(a: list, b: list):
#     result = [0 for _ in range(len(a) + len(b))]
#     for i in range(len(a)):
#         for j in range(len(b)):
#             result[i+j] += a[i] + b[j]
#     return result

def multiply(a: list, b: list):
    result = [0 for _ in range(len(a) + len(b) - 1)]
    for ind1, num1 in enumerate(a):
        for ind2, num2 in enumerate(b):
            result[ind1 + ind2] += num2*num1
    return result


# def multiply(a: list, b: list):
#     result = [0 for _ in range(len(a) + len(b) - 1)]
#     for ind1, num1 in enumerate(a):
#         for ind2, num2 in enumerate(b):
#             result[ind1 - ind2] += num2*num1
#     return result


if __name__ == "__main__":
    print(multiply([4, 2, 1, 2], [2, 1, 5, 7]))

