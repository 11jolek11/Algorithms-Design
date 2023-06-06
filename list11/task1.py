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
    
    def save_binary_tree(self, root, file_path):
        def pre_order_traversal(node, file):
            if node is None:
                return

            file.write("N " + str(node.value) + "\n")  # Save the node value

            if node.left is not None:
                file.write("L ")  # Indicate we are moving to the left child
                pre_order_traversal(node.left, file)

            if node.right is not None:
                file.write("R ")  # Indicate we are moving to the right child
                pre_order_traversal(node.right, file)
        
        with open(file_path, 'w') as file:
            pre_order_traversal(root, file)


    def load_binary_tree(self, file_path):
        def parse_next_token(file):
            return file.readline().strip().split(' ', 1)

        def build_tree(file):
            token, value = parse_next_token(file)

            if token == "N":
                node = Node(int(value))
                next_token, _ = parse_next_token(file)

                if next_token == "L":
                    node.left = build_tree(file)
                elif next_token == "R":
                    node.right = build_tree(file)

                return node

            return None

        with open(file_path, 'r') as file:
            return build_tree(file)

    
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
    
    # def preorder_traversal(self):
    #     result = []
    #     self._preorder_helper(self.root, result)
    #     return result

    # def _preorder_helper(self, node, result):
    #     if node is not None:
    #         result.append(node.key)
    #         # self.plot_binary_tree(color_node=node)
    #         # self.plot_binary_tree(color_node=node)
    #         self._preorder_helper(node.left, result)
    #         self._preorder_helper(node.right, result)


    # def create_memory_array(self, root):
    #     # Calculate the total number of nodes in the binary tree
    #     def count_nodes(node):
    #         if node is None:
    #             return 0
    #         return 1 + count_nodes(node.left) + count_nodes(node.right)

    #     # Create an empty memory array with the calculated size
    #     size = count_nodes(root)
    #     memory_array = [None] * size

    #     # Traverse the binary tree in pre-order and fill the memory array
    #     def fill_memory_array(node, index):
    #         if node is None:
    #             memory_array[index] = None
    #             return None

    #         # Store the current node's value at the current index in the memory array
    #         memory_array[index] = node.value

    #         # Recursively traverse the left and right subtrees
    #         fill_memory_array(node.left, 2 * index + 1)
    #         fill_memory_array(node.right, 2 * index + 2)

    #         # Start filling the memory array from the root node
    #     fill_memory_array(root, 0)

    #     return memory_array

    def create_memory_array(self, root):
        if not root:
            return []

        queue = [root]
        memory_array = []

        while queue:
            node = queue.pop(0)

            if node:
                memory_array.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
            else:
                memory_array.append(None)

        return memory_array
    
    def recreate_binary_tree(self, memory_array):
        if not memory_array:
            return None

        # Create the root node
        root = Node(memory_array[0])

        queue = [root]
        i = 1

        while queue and i < len(memory_array):
            node = queue.pop(0)

            # Create the left child
            if memory_array[i] is not None:
                node.left = Node(memory_array[i])
                queue.append(node.left)
            i += 1

            # Create the right child
            if i < len(memory_array) and memory_array[i] is not None:
                node.right = Node(memory_array[i])
                queue.append(node.right)
            i += 1
        return root
    
    def plot_binary_tree(self, root):
        def plot_node(node, x, y, dx, dy):
            if node is None:
                return

            # Plot current node
            plt.text(x, y, str(node.value), fontsize=12, ha='center', va='center', 
                    bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

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


    
    def save(self, root: Node, file_path: str):
        temp = str(self.create_memory_array(root))
        # TODO: awaiting implementation. Zapis jak do tablicy 1D
        with open(file_path, "w") as file:
            file.write(temp)

    def load(self, file_path: str):
        # root = Node(1)
        #TODO: awaiting implementation.
        sequence = ""
        with open(file_path) as file:
            sequence = file.read()
        self.root = self.recreate_binary_tree(eval(sequence))
        # print(sequence)



if __name__ == "__main__":
    tree = BinaryTreeOperator()
    tree2 = BinaryTreeOperator()

    # tree.add_node("", 7)
    # tree.add_node("L", 4)
    # tree.add_node("R", 9)
    # tree.add_node("LL", 2)
    # tree.add_node("LR", 5)
    # tree.add_node("RL", 8)

    tree.add_node("", 7)
    tree.add_node("L", 4)
    tree.add_node("R", 9)
    tree.add_node("LL", 2)
    tree.add_node("LLL", 5)
    tree.plot_binary_tree(tree.root)

    tree.save(tree.root, "tree.txt")
    tree.load("tree.txt")

    # x = tree.create_memory_array(tree.root)
    # print(tree2.recreate_binary_tree(x).value)
    # print(tree2.recreate_binary_tree(x).left.value)
    # print(tree2.recreate_binary_tree(x).right.value)
    # print(tree2.recreate_binary_tree(x).left.left.value)
    # print(tree2.recreate_binary_tree(x).left.left.left.value)
    # tree.plot_binary_tree(tree.root)
    # tree.delete_node("R")

    # tree.plot_binary_tree(tree.root)
    # tree.save_binary_tree(tree.root, "tree.txt")

    # print(tree.load_binary_tree("tree.txt"))
    # tree_data = [1, 2, 3, 4, 5, 6]
    # tree_data = [7, 4 ,9 , 2, 5, 8]
    # tree = BinaryTreeOperator.create_binary_tree(tree_data)
    # BinaryTreeOperator.plot_binary_tree(tree)
    # BinaryTreeOperator.add_node(tree, "LLL", 9)
    # BinaryTreeOperator.plot_binary_tree(tree)
