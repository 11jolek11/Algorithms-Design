class Graph:
    def __init__(self, graph: dict[str, list[str]]):
        self.visited = []
        self.ax_queue = []
        self.travel = []
        self.graph = graph

    def bfs(self, node, target):
        print(node)
        # Sprawdzam czy nie mam doczynienia z odlaczonymi nodami
        if len(self.graph[node]) == 0 or len(self.graph[target]) == 0:
            print("Single node")
            return 0
        
        self.travel.append(node)
        if node not in self.visited:
            self.visited.append(node)

        for neighbour in self.graph[node]:
            # Waunek stopu
            if neighbour == target:
                print(neighbour)
                self.travel.append(neighbour)
                print("hallo")
                # return self.travel
                return 0
            
            if neighbour not in self.visited:
                self.ax_queue.append(neighbour)
                self.visited.append(neighbour)

        # Jesli kolejka pomocnicza nie pusta to idz dalej
        if self.ax_queue:
            step = self.ax_queue.pop(0)
            self.bfs(step, target)


if __name__ == "__main__":
    # graph = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [],
    #     'E': ['F'],
    #     'F': [],
    #     'G': []
    # }

    graph = {
                'A': ['B', 'D'],
                'B': ['A', 'C'],
                'C': ['B', 'D'],
                'D': ['A', 'C']
            }


    # graph = {
    #             'A': []
    #         }


    # graph = {
    #             'A': ['B', 'D'],
    #             'B': ['A'],
    #             'D': ['A'],
    #             'G': []
    #         }

    g = Graph(graph)
    print(g.bfs('B', 'D'))
    print(g.travel)
