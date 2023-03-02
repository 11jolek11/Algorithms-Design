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
    G.add_edge(node_number, node_number+1)

G.remove_node(number_of_nodes)
nx.draw(G, nodes_position, with_labels=True)
plt.savefig('plot_task4.png')
