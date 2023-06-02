# # # import random

# # # def generate_matrix(m, n):
# # #     matrix = [[0] * n for _ in range(m)]
# # #     while n > 0:
# # #         i = random.randint(0, m - 1)
# # #         j = random.randint(0, n - 1)
# # #         if matrix[i][j] == 0:
# # #             matrix[i][j] = 1
# # #             n -= 1
# # #     return matrix

# # # # Example usage:
# # # m = 3  # Number of rows
# # # n = 4  # Number of columns
# # # total_sum = 6  # Desired sum of all elements

# # # # Ensure the desired sum is achievable
# # # if total_sum > m * n:
# # #     print("The desired sum is greater than the total number of elements in the matrix.")
# # # else:
# # #     matrix = generate_matrix(m, n)
# # #     print(matrix)


# # import numpy as np

# # def generate_matrix(n, total_sum):
# #     matrix = np.zeros((n, n), dtype=int)
# #     while np.sum(matrix) != total_sum:
# #         indices = np.random.choice(n**2, total_sum, replace=False)
# #         matrix.flat[indices] = 1
# #     return matrix

# # # # Example usage:
# # # m = 3  # Number of rows
# # # n = 4  # Number of columns
# # # total_sum = 6  # Desired sum of all elements

# # # # Ensure the desired sum is achievable
# # # if total_sum > m * n:
# # #     print("The desired sum is greater than the total number of elements in the matrix.")
# # # else:
# # #     matrix = generate_matrix(m, n, total_sum)
# # #     print(matrix)

# # # Example usage:
# # # m = 3  # Number of rows
# # n = 4  # Number of columns
# # total_sum = 6  # Desired sum of all elements

# # # Ensure the desired sum is achievable
# # matrix = generate_matrix(n, total_sum)
# # print(matrix)


# import numpy as np

# def adjacency_to_incidence(adjacency_matrix):
#     # Get the dimensions of the adjacency matrix
#     num_vertices = len(adjacency_matrix)
#     num_edges = int(np.sum(adjacency_matrix) / 2)  # Assuming undirected graph

#     # Create an empty incidence matrix
#     incidence_matrix = np.zeros((num_vertices, num_edges))

#     # Iterate over each edge in the adjacency matrix
#     edge_count = 0
#     for i in range(num_vertices):
#         for j in range(i+1, num_vertices):
#             if adjacency_matrix[i][j] == 1:
#                 # Set the appropriate entries in the incidence matrix
#                 incidence_matrix[i][edge_count] = 1
#                 incidence_matrix[j][edge_count] = 1
#                 edge_count += 1

#     return incidence_matrix

# # Example usage
# adjacency_matrix = np.array([[0, 1, 0, 1],
#                              [1, 0, 1, 1],
#                              [0, 1, 0, 0],
#                              [1, 1, 0, 0]])

# incidence_matrix = adjacency_to_incidence(adjacency_matrix)
# print(incidence_matrix)
import numpy as np


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return None

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0



def connected_components(graph):
    num_vertices = len(graph)
    ds = DisjointSet(num_vertices)

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] == 1:
                ds.union(i, j)

    components = {}
    for i in range(num_vertices):
        root = ds.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)

    return list(components.values())


if __name__ == "__main__":
    # Macierz sąsiedztwa
    # Graf niespójny
    graph = np.asarray([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ])

    # Graf spójny
    # graph = np.asarray(
    #     [
    #         [0, 1, 0, 0, 0],
    #         [1, 0, 0, 0, 1],
    #         [0, 0, 0, 1, 1], 
    #         [0, 0, 1, 0, 1], 
    #         [0, 1, 1, 1, 0]
    #     ])


    components = connected_components(graph)
    print(components)
