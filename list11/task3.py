import networkx as nx
import matplotlib.pyplot as plt
# from networkx.drawing.nx_pydot import graphviz_layout
from networkx.drawing.nx_agraph import graphviz_layout


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_helper(self.root, key)

    def _insert_helper(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert_helper(node.left, key)
        elif key > node.key:
            node.right = self._insert_helper(node.right, key)
        return node
    
    def generate(self, input: list):
        for element in input:
            self.insert(element)

    def search(self, key):
        return self._search_helper(self.root, key)

    def _search_helper(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search_helper(node.left, key)
        else:
            return self._search_helper(node.right, key)

    def delete(self, key):
        self.root = self._delete_helper(self.root, key)

    def _delete_helper(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_helper(node.left, key)
        elif key > node.key:
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
            self._inorder_helper(node.left, result)
            result.append(node.key)
            self._inorder_helper(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        if node is not None:
            result.append(node.key)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        if node is not None:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.key)

    def rotate_right(self, key):
        self.root = self._rotate_right_helper(self.root, key)

    def _rotate_right_helper(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._rotate_right_helper(node.left, key)
        elif key > node.key:
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

        if key < node.key:
            node.left = self._rotate_left_helper(node.left, key)
        elif key > node.key:
            node.right = self._rotate_left_helper(node.right, key)
        else:
            if node.right is None:
                return node
            new_root = node.right
            node.right = new_root.left
            new_root.left = node
            return new_root

        return node
    
    @classmethod
    def save(cls, root: Node, file_path: str):
        # TODO: awaiting implementation. Zapis jak do tablicy 1D
        with open(file_path) as file:
            pass

    @classmethod
    def load(cls, file_path: str):
        #TODO: awaiting implementation.
        with open(file_path) as file:
            pass
    
    # @staticmethod
    # def plot_binary_tree(root):
    # @classmethod
    def plot_binary_tree(self):
        G = nx.Graph()

        def add_edges(node, parent=None):
            if node:
                # TODO: Add node can take any hashable python object so you can add Node objects instead of value
                G.add_node(node.key)
                if parent:
                    G.add_edge(parent.key, node.key)
                add_edges(node.left, node)
                add_edges(node.right, node)

        add_edges(self.root)

        # pos = nx.spring_layout(G)
        pos = nx.spectral_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=12, font_weight="bold",
                width=2, edge_color="gray")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    tree = BST()

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

    # print(tree.search(14).left.key)
    # tree.plot_binary_tree()
    # tree.delete(7)
    # tree.plot_binary_tree()
    # tree.insert(7)
    # tree.delete(6)
    # tree.plot_binary_tree()
    # tree.delete(8)
    # tree.plot_binary_tree()
    # print(tree.inorder_traversal())
    # print(tree.preorder_traversal())
    # print(tree.postorder_traversal())

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

    tree.generate([50, 70, 60, 20, 90, 10, 40, 100])
    print(tree.postorder_traversal())
    print(tree.preorder_traversal())
    print(tree.inorder_traversal())
    tree2 = BST()

    # tree.plot_binary_tree()

    pass
