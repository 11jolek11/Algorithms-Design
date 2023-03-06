import networkx as nx
import  matplotlib.pyplot as plt
import numpy as np
import uniform 



number_of_nodes = int(input('Insert number of nodes: '))

G = nx.Graph()
nodes_position = {}

for node_number in range(number_of_nodes):
    position_x = uniform.LCG.uniform_range(2, 5)
    position_y = uniform.LCG.uniform_range(2, 5)

    G.add_node(node_number)
    nodes_position[node_number] = [position_x, position_y]

# connections = []

# for i in range(len(G.nodes)-1):
#     connections.append((i, i+1))

# G.add_edges_from(connections)

nx.draw(G, nodes_position, with_labels=True)
plt.savefig('plot_task4.png')
