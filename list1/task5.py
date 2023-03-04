import networkx as nx
import  matplotlib.pyplot as plt
import numpy as np
import uniform 
from math import sqrt
import sys



number_of_nodes = int(input('Insert number of nodes: '))
# print(number_of_nodes)

G = nx.Graph()
nodes_position = {}
radius = 1

class GraphCreator:
    def __init__(self, radius, number, graph=nx.Graph()) -> None:
        self.nodes_position = {}
        self.radius = radius

        self.number_of_nodes = list(range(number))
        # print(number)

        self.graph = graph
        # if graph is not None:
        #     self.graph = graph
        # else:
        #     self.graph = nx.Graph()

    @classmethod
    def generate_random_point(cls) -> list:
        position_x = uniform.LCG.uniform_range(1, 30)
        position_y = uniform.LCG.uniform_range(1, 30)
        # print(f'({position_x}, {position_y})')
        return [position_x, position_y]
    
    def check_distance(self, point: list[float]):
        result = None

        if len(list(self.nodes_position.values())) == 0:
            # print("$$$$$")
            # print("First point")
            return False
        
        for saved_point in list(self.nodes_position.values()):
            x = saved_point[0] - point[0]
            y = saved_point[1] - point[1]
            # print('$$$$$')
            # print(sqrt(x**2 + y**2))
            if sqrt(x**2 + y**2) <= 2*self.radius:
                # print(sqrt(x**2 + y**2))
                return True
            # if sqrt(x**2 + y**2) > 2*self.radius:
                # print('***')
                # print(sqrt(x**2 + y**2))
        return False
    
    def add_new_position(self, number):
        count = 0
        if count >= 100:
            return 1
        while count < 100:
            count += 1
            new_point = self.generate_random_point()
            temp = self.check_distance(new_point)
            if temp == False:
                # print(temp)
                self.graph.add_node(number)
                self.nodes_position[number] = new_point
                return 0
        return 1
            
    def get_postions(self):
        positions = list(self.nodes_position.values())
        for number in range(len(positions)):
            positions[number] = tuple(positions[number])
        return positions

    def create(self):
        # print(self.number_of_nodes)
        for node in self.number_of_nodes:
            p = self.add_new_position(node)
            if p == 1:
                return self.graph
        return self.graph
        
        # connections = []

        # for i in range(len(self.graph.nodes)-1):
        #     connections.append((i, i+1))
        # self.graph.add_edges_from(connections)


        

# def generate_nodes(graph: nx.Graph):
#     for node_number in range(number_of_nodes):
#         position_x = uniform.LCG.uniform_range(2, 5)
#         position_y = uniform.LCG.uniform_range(2, 5)

#         nodes_position[node_number] = [position_x, position_y]
#         graph.add_node(node_number)


# connections = []

# for i in range(len(G.nodes)-1):
#     connections.append((i, i+1))

# G.add_edges_from(connections)

creator = GraphCreator(radius=1, number=number_of_nodes, graph=G)
G = creator.create()
pos = creator.get_postions()

fig, axi = plt.subplots()

fig.set_figwidth = 5
fig.set_figheight = 5

axi.figure.set_figheight = 5
axi.figure.set_figwidth = 5

for item in pos:
    circle = plt.Circle(item, radius=1, color='r')
    axi.add_patch(circle)

# nx.draw(G, nodes_position, with_labels=True)
print(G)
nx.draw_networkx(G, pos, with_labels=True, ax=axi)
print(f'Total points: {len(G.nodes)}')

plt.savefig('plot_task5.png')
