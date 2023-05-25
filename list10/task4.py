import numpy as np
import random


class Graph:
    def __init__(self, vertex_no: int, packing_ratio: float) -> None:
        if packing_ratio > 1 or packing_ratio < 0:
            raise ValueError("Packing ratio out of bounds [0, 1] !!!")
        if vertex_no == 0:
            raise ValueError("Empty graph")
        
        self.packing_ratio = packing_ratio
        self.no_of_vertexes = vertex_no
        self.no_of_edges = (self.no_of_vertexes(self.no_of_vertexes-1)/2)*self.packing_ratio

        self.incidence_matrix = np.zeros((self.no_of_vertexes, self.no_of_edges))
        self.adjacency_matrix = np.zeros((self.no_of_vertexes, self.no_of_vertexes))


    def gen_adjacency_matrix(self):
        for i in range(self.no_of_vertexes):
            for j in range(i, self.no_of_vertexes):
                if i == j:
                    self.incidence_matrix[i][j] = np.random.choice([0, 1])  # Set diagonal elements randomly
                else:
                    self.incidence_matrix[i][j] = np.random.randint(2)  # Set upper triangular elements randomly

        # Reflect the upper triangular self.incidence_matrix to the lower triangular part
        for i in range(self.no_of_vertexes):
            for j in range(i):
                self.incidence_matrix[i][j] = self.incidence_matrix[j][i]

        # Calculate the current sum of all elements
        current_sum = np.sum(self.incidence_matrix)

        # Adjust the sum to match the desired total_sum
        diff = self.no_of_edges*2 - current_sum
        if diff > 0:
            # Add 1s randomly to reach the desired sum
            indices = np.random.choice(np.where(self.incidence_matrix == 0), diff, replace=False)
            self.incidence_matrix[indices] = 1
        elif diff < 0:
            # Remove 1s randomly to reach the desired sum
            indices = np.random.choice(np.where(self.incidence_matrix == 1), -diff, replace=False)
            self.incidence_matrix[indices] = 0

    # def gen_incidence_matrix(self):
    #     total_sum = self.no_of_edges*2
    #     while total_sum > 0:
    #         # Randomly select a cell
    #         row = random.randint(0, self.no_of_vertexes - 1)
    #         col = random.randint(0, self.no_of_vertexes - 1)

    #         # If the cell is already 1, skip to the next iteration
    #         if self.incidence_matrix[row][col] == 1:
    #             continue

    #         # Place a 1 in the selected cell
    #         self.incidence_matrix[row][col] = 1
    #         total_sum -= 1

    #         # If the desired total_sum is reached, break the loop
    #         if total_sum == 0:
    #             break
    
    def gen_incidence_matrix(self):
        if np.sum(self.adjacency_matrix) == 0:
            self.gen_adjacency_matrix()

        n = self.adjacency_matrix.shape[0]
        m = np.count_nonzero(self.adjacency_matrix) // 2  # Assuming undirected graph, counting non-zero entries
        incidence_matrix = np.zeros((n, m))

        edge_count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.adjacency_matrix[i, j] == 1:
                    incidence_matrix[i, edge_count] = 1
                    incidence_matrix[j, edge_count] = -1
                    edge_count += 1
