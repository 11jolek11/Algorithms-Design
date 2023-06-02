# from robots import RobotCreator


# class Node():
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value


# class BinarySearchTree():
#     def __init__(self, root: Node | None=None):
#         self.root = root

#     def insert(self, new_value):
#         new_node = Node(new_value)
#         current_root = self.root
#         parent_root = None
#         temp = 0
#         while current_root is not None:
#             parrent_root = current_root
#             if new_node.value < current_root.value:
#                 current_root = current_root.left
#             else:
#                 current_root = current_root.right
#         if parent_root is None:
#             self.root = new_node
#         elif new_node.value < parent_root.value:
#             parent_root.left = new_node
#         else:
#             parent_root.right = new_node


        



# if __name__ == "__main__":
#     pass
from task1 import BinaryTreeOperator
import networkx as nx
import matplotlib.pyplot as plt


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
            node.left = self._insert_helper(node.left, key, self.attr)
        elif getattr(key, self.attr) > getattr(node.key, self.attr):
            node.right = self._insert_helper(node.right, key, self.attr)
        return node
    
    def generate(self, input: list):
        for element in input:
            self.insert(self.root, element)

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

        if getattr(key, self.attr) < getattr(node.key, self.attr):
            node.left = self._delete_helper(node.left, key)
        elif getattr(key, self.attr) > getattr(node.key, self.attr):
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
    
    @staticmethod
    def plot_binary_tree(root):
        G = nx.Graph()

        def add_edges(node, parent=None):
            if node:
                # TODO: Add node can take any hashable python object so you can add Node objects instead of value
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
