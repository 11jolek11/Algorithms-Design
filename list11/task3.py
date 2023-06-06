import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from robots import Robot, RobotCreator


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, attr):
        self.root = None
        self.attr = attr

    def insert(self, key):
        self.root = self._insert_helper(self.root, key)

    def _insert_helper(self, node, key):
        if node is None:
            return Node(key)

        if getattr(key, self.attr) < getattr(node.key, self.attr):
            node.left = self._insert_helper(node.left, key)
        elif getattr(key, self.attr) > getattr(node.key, self.attr):
            node.right = self._insert_helper(node.right, key)
        return node
    
    def generate(self, input: list):
        for element in input:
            self.insert(element)

    def search(self, key):
        return self._search_helper(self.root, key)

    def _search_helper(self, node, key):
        if node is None or getattr(node.key, self.attr) == key:
            return node

        if key < getattr(node.key, self.attr):
            return self._search_helper(node.left, key)
        else:
            return self._search_helper(node.right, key)

    def delete(self, key):
        self.root = self._delete_helper(self.root, key)

    def _delete_helper(self, node, key):
        if node is None:
            return node

        if key < getattr(node.key, self.attr):
            node.left = self._delete_helper(node.left, key)
        elif key > getattr(node.key, self.attr):
            node.right = self._delete_helper(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # If the node has both left and right children
            # Find the minimum value in the right subtree
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._delete_helper(node.right, min_node.key)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node is not None:
            # self.plot_binary_tree(color_node=node)
            self._inorder_helper(node.left, result)
            result.append(node.key)
            self.plot_binary_tree(self.root, color_node=node)
            self._inorder_helper(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        if node is not None:
            result.append(node.key)
            # self.plot_binary_tree(color_node=node)
            self.plot_binary_tree(self.root, color_node=node)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        if node is not None:
            # self.plot_binary_tree(color_node=node)
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.key)
            self.plot_binary_tree(self.root, color_node=node)

    def rotate_right(self, key):
        self.root = self._rotate_right_helper(self.root, key)

    def _rotate_right_helper(self, node, key):
        if node is None:
            return node

        if key < getattr(node.key, self.attr):
            node.left = self._rotate_right_helper(node.left, key)
        elif key > getattr(node.key, self.attr):
            node.right = self._rotate_right_helper(node.right, key)
        else:
            if node.left is None:
                return node
            new_root = node.left
            node.left = new_root.right
            new_root.right = node
            return new_root

        return node

    def rotate_left(self, key):
        self.root = self._rotate_left_helper(self.root, key)

    def _rotate_left_helper(self, node, key):
        if node is None:
            return node

        if key < getattr(node.key, self.attr):
            node.left = self._rotate_left_helper(node.left, key)
        elif key > getattr(node.key, self.attr):
            node.right = self._rotate_left_helper(node.right, key)
        else:
            if node.right is None:
                return node
            new_root = node.right
            node.right = new_root.left
            new_root.left = node
            return new_root

        return node
    
    def save(self, file_path: str):
        content = list(map(str, self.preorder_traversal()))
        with open(file_path, "w") as file:
            for node in content:
                file.write(f'{node}\n')

    def load(self, file_path: str):
        with open(file_path) as file:
            for node in file:
                self.insert(int(node))
    
    # def plot_binary_tree(self, color_node=Robot("g", -1.0, -1, -1)):
    # def plot_binary_tree(self, color_node=None):
    #     G = nx.Graph()
    #     color_map = []
    #     # color_map = ['red' if node == color_node else 'lightblue' for node in G]

    #     def add_edges(node, parent=None):
    #         if node:
    #             if node == color_node:
    #                 color_map.append("red")
    #             else:
    #                 color_map.append("lightblue")
    #             G.add_node(getattr(node.key, self.attr))
    #             if parent:
    #                 G.add_edge(getattr(parent.key, self.attr), getattr(node.key, self.attr))
    #             add_edges(node.left, node)
    #             add_edges(node.right, node)

    #     add_edges(self.root)

    #     # pos = nx.spring_layout(G)
    #     pos = nx.spectral_layout(G)
    #     plt.figure(figsize=(8, 6))
    #     nx.draw(G, pos, with_labels=True, node_size=1500, node_color=color_map, font_size=12, font_weight="bold",
    #             width=2, edge_color="gray")
    #     plt.axis("off")
    #     plt.show()
    def plot_binary_tree(self, root, color_node=None):
        def plot_node(node, x, y, dx, dy):
            if node is None:
                return

            # Plot current node
            if node != color_node:
                plt.text(x, y, str(node.key), fontsize=12, ha='center', va='center', 
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
            else:
                plt.text(x, y, str(node.key), fontsize=12, ha='center', va='center', 
                        bbox=dict(facecolor='red', edgecolor='black', boxstyle='circle'))

            # Plot left child
            if node.left is not None:
                x_left = x - dx
                y_left = y - dy
                plt.plot([x, x_left], [y, y_left], 'b-', lw=1)
                plot_node(node.left, x_left, y_left, dx / 2, dy)

            # Plot right child
            if node.right is not None:
                x_right = x + dx
                y_right = y - dy
                plt.plot([x, x_right], [y, y_right], 'b-', lw=1)
                plot_node(node.right, x_right, y_right, dx / 2, dy)

        # Set up the figure and axes
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.axis('off')

        # Recursively plot the tree starting from the root
        plot_node(root, 0, 0, 1, 1)

        # Adjust plot margins and display the plot
        plt.margins(0.1)
        plt.show()


if __name__ == "__main__":
    tree = BST("robot_range")
    temp = []
    wzor = [5, 7, 3, 4, 2, 1]
    for i in range(len(wzor)):
        r = RobotCreator.create()
        # r.robot_range = i*10
        r.robot_range = wzor[i]
        temp.append(r)
        print(str(r))
    tree.generate(temp)
    # tree.plot_binary_tree(tree.root)
    # tree.plot_binary_tree()


    # tree.generate([8, 3, 10, 1, 6, 14, 13, 4, 7])
    # tree.plot_binary_tree()

    # tree.insert(8)
    # tree.insert(3)
    # tree.insert(10)
    # tree.insert(1)
    # tree.insert(6)
    # tree.insert(14)
    # tree.insert(13)
    # tree.insert(4)
    # tree.insert(7)
    # tree.plot_binary_tree()

    # print(tree.search(0).key)
    # tree.plot_binary_tree()
    # tree.delete(0)
    # tree.plot_binary_tree()
    # tree.insert(7)
    # tree.delete(6)
    # tree.plot_binary_tree()
    # tree.delete(8)
    # tree.plot_binary_tree()
    # print(tree.inorder_traversal())
    # print(tree.preorder_traversal())
    print(tree.postorder_traversal())

    # tree.generate([5, 3, 7, 2, 4, 8])
    # tree.plot_binary_tree()
    # tree.rotate_left(5)
    # tree.plot_binary_tree()

    # tree.generate([20, 2, 3, 6, 5, 12, 9])
    # tree.plot_binary_tree()
    # tree.rotate_left(5)
    # tree.plot_binary_tree()

    # tree.generate([20, 2, 3, 6, 5, 12, 9])
    # tree.plot_binary_tree()
    # tree.rotate_right(5)
    # tree.plot_binary_tree()

    # path = "graph_test.txt"

    # tree.generate([50, 70, 60, 20, 90, 10, 40, 100])
    # print(tree.postorder_traversal())
    # print(tree.preorder_traversal())
    # print(tree.inorder_traversal())
    # print("###############")
    # tree.save(path)
    # tree2 = BST()
    # tree2.load(path)
    # print(tree2.postorder_traversal())
    # print(tree2.preorder_traversal())
    # print(tree2.inorder_traversal())
