from task4 import Graph
import numpy as np


class DisjointSet:
    def __init__(self, n):
        # make set
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

    # def make_set(self, x):
    #     if x not in self.parent:
    #         self.parent[x] = x
    #         self.rank[x] = 0



def connected_components(graph):
    num_vertices = len(graph)
    # num_vertices = graph.shape[0]
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
    from task4 import Graph

    p = Graph(100, 0.01)
    p.generate_adjacency_matrix()
    dfrgg = p.adjacency_matrix

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


    components = connected_components(dfrgg)
    print(components)
    print(len(components))
