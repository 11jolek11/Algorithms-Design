import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinaryTreeOperator:
    def __init__(self):
        self.root = None
        self.pos = []
        self.operations = {}
    
    @staticmethod
    def plot_binary_tree(root):
        # TODO: implement position adding
        G = nx.Graph()

        def add_edges(node, parent=None):
            if node:
                G.add_node(node.value)
                if parent:
                    G.add_edge(parent.value, node.value)
                add_edges(node.left, node)
                add_edges(node.right, node)

        add_edges(root)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=12, font_weight="bold",
                width=2, edge_color="gray")
        plt.axis("off")
        plt.show()
    
    def add_node(self, instrution: str, value: int):
        if self.root is None:
            self.root = Node(value)
        root = self.root
        for move in instrution:
            if move == "L" and root.left is not None:
                root = root.left
            elif move == "L" and root.left is None:
                print("add left child")
                root.left = Node(value)
            elif move == "R" and root.right is not None:
                root = root.right
            elif move == "R" and root.right is None:
                print("add right child")
                root.right = Node(value)
    
    def delete_node(self, instrution: str):
        root = self.root
        current_root = root
        parent_root = None
        direction_flag = instrution[-1]
        for move in instrution:
            if move == "L":
                parent_root = current_root
                current_root = root.left
            elif move == "R":
                parent_root = current_root
                current_root = root.right
        if direction_flag == "L":
            parent_root.left = None
            del current_root
        if direction_flag == "R":
            parent_root.right = None
            del current_root
    
    @staticmethod
    def save(root: Node, file_path: str):
        # TODO: awaiting implementation. Zapis jak do tablicy 1D
        with open(file_path) as file:
            pass

    @staticmethod
    def load(file_path: str):
        root = Node(1)
        #TODO: awaiting implementation.
        with open(file_path) as file:
            pass
        return root



if __name__ == "__main__":
    tree = BinaryTreeOperator()
    tree.add_node("", 7)
    tree.add_node("L", 4)
    tree.add_node("R", 9)
    tree.add_node("LL", 2)
    tree.add_node("LR", 5)
    tree.add_node("RL", 8)
    tree.plot_binary_tree(tree.root)
    tree.delete_node("R")
    tree.plot_binary_tree(tree.root)
    # tree_data = [1, 2, 3, 4, 5, 6]
    # tree_data = [7, 4 ,9 , 2, 5, 8]
    # tree = BinaryTreeOperator.create_binary_tree(tree_data)
    # BinaryTreeOperator.plot_binary_tree(tree)
    # BinaryTreeOperator.add_node(tree, "LLL", 9)
    # BinaryTreeOperator.plot_binary_tree(tree)

