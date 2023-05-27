# import random

# def generate_matrix(m, n):
#     matrix = [[0] * n for _ in range(m)]
#     while n > 0:
#         i = random.randint(0, m - 1)
#         j = random.randint(0, n - 1)
#         if matrix[i][j] == 0:
#             matrix[i][j] = 1
#             n -= 1
#     return matrix

# # Example usage:
# m = 3  # Number of rows
# n = 4  # Number of columns
# total_sum = 6  # Desired sum of all elements

# # Ensure the desired sum is achievable
# if total_sum > m * n:
#     print("The desired sum is greater than the total number of elements in the matrix.")
# else:
#     matrix = generate_matrix(m, n)
#     print(matrix)


import numpy as np

def generate_matrix(n, total_sum):
    matrix = np.zeros((n, n), dtype=int)
    while np.sum(matrix) != total_sum:
        indices = np.random.choice(n**2, total_sum, replace=False)
        matrix.flat[indices] = 1
    return matrix

# # Example usage:
# m = 3  # Number of rows
# n = 4  # Number of columns
# total_sum = 6  # Desired sum of all elements

# # Ensure the desired sum is achievable
# if total_sum > m * n:
#     print("The desired sum is greater than the total number of elements in the matrix.")
# else:
#     matrix = generate_matrix(m, n, total_sum)
#     print(matrix)

# Example usage:
# m = 3  # Number of rows
n = 4  # Number of columns
total_sum = 6  # Desired sum of all elements

# Ensure the desired sum is achievable
matrix = generate_matrix(n, total_sum)
print(matrix)