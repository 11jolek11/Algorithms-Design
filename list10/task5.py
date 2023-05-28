from task4 import Graph
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
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


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
    import networkx as nx
    import matplotlib.pyplot as plt
    # Example graph represented as an adjacency matrix
    graph = np.asarray([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ])

    components = connected_components(graph)
    print(components)
 