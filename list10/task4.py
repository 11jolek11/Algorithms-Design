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
        self.no_of_edges = int((self.no_of_vertexes*(self.no_of_vertexes-1)/2)*self.packing_ratio)

        self.incidence_matrix = np.zeros((self.no_of_vertexes, self.no_of_edges))
        self.adjacency_matrix = np.zeros((self.no_of_vertexes, self.no_of_vertexes))

    def generate_adjacency_matrix(self):
        total_sum = self.no_of_edges
        matrix = np.zeros((self.no_of_vertexes, self.no_of_vertexes), dtype=int)
        while np.sum(matrix) != total_sum:
            indices = np.random.choice(self.no_of_vertexes**2, total_sum, replace=False)
            matrix.flat[indices] = 1
        self.adjacency_matrix = matrix

    # def generate_adjacency_matrix(self, num_nodes, degree_of_filling):
    #     max_edges = (num_nodes * (num_nodes - 1)) // 2
    #     num_edges = int(max_edges * degree_of_filling)
    #     edge_indices = random.sample(range(max_edges), num_edges)
        
    #     adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    #     count = 0
        
    #     for i in range(num_nodes):
    #         for j in range(i+1, num_nodes):
    #             if count in edge_indices:
    #                 weight = random.randint(1, 10)
    #                 adjacency_matrix[i][j] = weight
    #                 adjacency_matrix[j][i] = weight
    #             count += 1
        
    #     return adjacency_matrix


    # def gen_adjacency_matrix(self):
    #     for i in range(self.no_of_vertexes):
    #         for j in range(i, self.no_of_vertexes):
    #             if i == j:
    #                 self.incidence_matrix[i][j] = np.random.choice([0, 1])  # Set diagonal elements randomly
    #             else:
    #                 self.incidence_matrix[i][j] = np.random.randint(2)  # Set upper triangular elements randomly

    #     # Reflect the upper triangular self.incidence_matrix to the lower triangular part
    #     for i in range(self.no_of_vertexes):
    #         for j in range(i):
    #             self.incidence_matrix[i][j] = self.incidence_matrix[j][i]

    #     # Calculate the current sum of all elements
    #     current_sum = np.sum(self.incidence_matrix)

    #     # Adjust the sum to match the desired total_sum
    #     diff = int(self.no_of_edges*2 - current_sum)
    #     if diff > 0:
    #         # Add 1s randomly to reach the desired sum
    #         # indices = []
    #         # for _ in range(diff):
    #         #     indices.append(random.choice(np.where(self.incidence_matrix == 0)))
    #         # self.incidence_matrix[indices] = 1


    #         # indices = np.random.choice(np.where(self.incidence_matrix == 0), diff, replace=False)
    #         # self.incidence_matrix[indices] = 1
    #         indices = np.argwhere(self.incidence_matrix == 0)
    #         indices_to_change = random.sample(list(indices), diff)
    #         for item in indices_to_change:
    #             self.incidence_matrix[item] = 1
            



        # elif diff < 0:
            # indices = np.argwhere(self.incidence_matrix == 1)
            # indices_to_change = random.sample(list(indices), diff)
            # self.incidence_matrix[indices_to_change] = 0
            # Remove 1s randomly to reach the desired sum
            # indices = np.random.choice(np.where(self.incidence_matrix == 1), -diff, replace=False)

            # indices = random.choice(np.where(self.incidence_matrix == 1))
            # self.incidence_matrix[indices] = 0

            # indices = []
            # for _ in range(diff):
            #     indices.append(random.choice(np.where(self.incidence_matrix == 0)))
            # self.incidence_matrix[indices] = 0

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


if __name__ == "__main__":
    p = Graph(5, 0.7)
    p.generate_adjacency_matrix()
    print(p.adjacency_matrix)
    print(np.sum(p.adjacency_matrix))
    print((10*(10-1)//2)*0.7)
    p.gen_incidence_matrix()
    print(p.incidence_matrix)
