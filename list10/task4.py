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

    # def generate_adjacency_matrix(self):
    #     # FIXME:
    #     total_sum = self.no_of_edges
    #     matrix = np.zeros((self.no_of_vertexes, self.no_of_vertexes), dtype=int)
    #     while np.sum(matrix) != total_sum:
    #         # FIXME: może przeskoczyć total_sum
    #         indices = np.random.choice(self.no_of_vertexes**2, total_sum, replace=False)
    #         # print(indices)
    #         matrix.flat[indices] = 1
    #         matrix = (matrix + matrix.T)//2
    #     self.adjacency_matrix = matrix

    def generate_adjacency_matrix(self):
        count = self.no_of_edges
        # count = self.no_of_vertexes
        matrix = np.zeros((self.no_of_vertexes, self.no_of_vertexes))
        avaible_indexes = [i for i in range(self.no_of_vertexes**2)]
        random.shuffle(avaible_indexes)
        test = []
        while count > 0:
            # test.append(count)
            index = avaible_indexes.pop(0)
            matrix.flat[index] = 1
            test.append(index)
            count -= 1
        matrix = np.ceil((matrix + matrix.T)/2)
        matrix = matrix.astype(int)
        self.adjacency_matrix = matrix

    def gen_incidence_matrix(self):
        # [[0 1 0 0 1]
        # [0 0 0 0 0]
        # [0 0 0 0 0]
        # [1 1 0 0 0]
        # [0 1 0 0 0]]
        # self.adjacency_matrix = np.asarray(
        #     [[0, 1, 0, 0, 1],
        #     [0, 0 , 0, 0, 0],
        #     [0, 0, 0, 0, 0],
        #     [1, 1, 0, 0, 0],
        #     [0, 1, 0, 0, 0]]
        # )
        # [[1 0 0 0 0]
        # [0 1 0 0 1]        # [0 0 1 0 0]
        # [0 0 0 0 0]
        # [0 1 0 0 0]]
        num_vertices = len(self.adjacency_matrix)
        num_edges = int((np.sum(self.adjacency_matrix)+np.trace(self.adjacency_matrix))/ 2)
        incidence_matrix = np.zeros((num_vertices, num_edges), dtype=int)
        edge_count = 0

        for i in range(num_vertices):
            for j in range(i, num_vertices):
                if self.adjacency_matrix[i][j] == 1:
                    incidence_matrix[i][edge_count] = 1
                    incidence_matrix[j][edge_count] = 1
                    edge_count += 1

        self.incidence_matrix = incidence_matrix

        # if np.sum(self.adjacency_matrix) == 0:
        #     self.generate_adjacency_matrix()

        # n = self.adjacency_matrix.shape[0]
        # m = np.count_nonzero(self.adjacency_matrix) // 2  # Assuming undirected graph, counting non-zero entries
        # incidence_matrix = np.zeros((n, m))

        # edge_count = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if self.adjacency_matrix[i, j] == 1:
        #             incidence_matrix[i, edge_count] = 1
        #             incidence_matrix[j, edge_count] = 1
        #             edge_count += 1


if __name__ == "__main__":
    p = Graph(5, 0.5)
    # p = Graph(100, 0.01)
    # p = Graph(400, 1)
    p.generate_adjacency_matrix()
    print(p.adjacency_matrix)
    print(p.no_of_vertexes)
    print(p.no_of_edges)
    # print((10*(10-1)//2)*0.7)
    p.gen_incidence_matrix()
    print(p.incidence_matrix)
