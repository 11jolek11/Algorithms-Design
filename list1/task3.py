import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 


number_of_nodes = int(input("Enter number of nodes: "))

G = nx.complete_graph(number_of_nodes)
pos = nx.circular_layout(G)

subax = plt.subplot()
nx.draw(G, pos, with_labels=True)

plt.savefig('plot_task3.png')
