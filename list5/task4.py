# def pathfinder(G, v_start, v_end, path_len=0):
#     if path_len >= len(G):
#         return False
#     
#     if G[v_start][v_end]:
#         return True

#     for v_nbor, edge in enumerate(G[v_start]):
#         if edge:
#             print(edge)
#             if pathfinder(G, v_nbor, v_end, path_len+1):
#                 return True

#     return False


# G = [[1, 1, 0, 0, 0],
#      [0, 1, 0, 0, 0],
#      [0, 0, 1, 0, 0],
#      [0, 1, 1, 1, 0],
#      [1, 0, 0, 1, 1]]

# # print(pathfinder(G, 3, 1))


# def dfs_recursive(graph, vertex, target, path=[]):
#     path += [vertex]

#     for neighbor in graph[vertex]:
#         print(neighbor == target)
#         if neighbor == target:
#             path += [neighbor]
#             return path
#         if neighbor not in path:
#             path = dfs_recursive(graph, neighbor, target, path)

#     return path


# adjacency_matrix = {1: [2, 3], 2: [4, 5],
#                     3: [5], 4: [6], 5: [6],
#                     6: [7], 7: []}

# print(dfs_recursive(adjacency_matrix, 1, 4))
# [1, 2, 4, 6, 7, 5, 3]




class Graph:
    def __init__(self, graph: dict[str, list[str]]):
        self.visited = []
        self.queue = []
        self.travel = []
        self.graph = graph

    def bfs(self, node, target):
    # TODO: Dodaj obsluge pojedynczych nodow
        print(node)
        if len(self.graph[node]) == 0 or len(self.graph[target]) == 0:
            print("Single node")
            return 0
        self.travel.append(node)
        if node not in self.visited:
            self.visited.append(node)
        for neighbour in self.graph[node]:
            if neighbour == target:
                print(neighbour)
                self.travel.append(neighbour)
                print("hallo")
                # return self.travel
                return 0
            if neighbour not in self.visited:
                self.queue.append(neighbour)
                self.visited.append(neighbour)

        if self.queue:
            vertex = self.queue.pop(0)
            self.bfs(vertex, target)


# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': [],
#     'G': []
# }

# graph = {
#             'A': ['B', 'D'],
#             'B': ['A', 'C'],
#             'C': ['B', 'D'],
#             'D': ['A', 'C']
#         }


# graph = {
#             'A': []
#         }


graph = {
            'A': ['B', 'D'],
            'B': ['A'],
            'D': ['A'],
            'G': []
        }

g = Graph(graph)
print(g.bfs('A', 'G'))
print(g.travel)
