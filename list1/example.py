import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for letter in ['A', 'B', 'C', 'D']:
    G.add_node(letter)

connections = [
    ('A', 'C'),
    ('C', 'B'),
    ('B', 'A'),
    ('A', 'D'),
    ('D', 'E'),
    ('E', 'A'),
]

G.add_edges_from(connections)

nodes_position = {
    'A': [2, 2],
    'B': [3, 3],
    'C': [3, 1],
    'D': [1, 1],
    'E': [1, 3],
}

nx.draw(G,nodes_position, with_labels=True)
plt.savefig('plot_task4.png')