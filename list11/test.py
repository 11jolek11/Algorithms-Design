class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def save_binary_tree(root, file_path):
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


# def load_binary_tree(file_path):
#     def parse_next_token(file):
#         return file.readline().strip().split(' ', 1)

#     def build_tree(file):
#         token, value = parse_next_token(file)

#         if token == "N":
#             node = Node(int(value))
#             next_token, _ = parse_next_token(file)

#             if next_token == "L":
#                 node.left = build_tree(file)
#             elif next_token == "R":
#                 node.right = build_tree(file)

#             return node

#         return None

#     with open(file_path, 'r') as file:
#         return build_tree(file)

if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Save the binary tree
    save_binary_tree(root, "tree.txt")
    # Load the binary tree
    loaded_root = load_binary_tree("tree.txt")

    # Print the values of the reconstructed tree
    def print_tree_in_order(node):
        if node is None:
            return

        print_tree_in_order(node.left)
        print(node.value)
        print_tree_in_order(node.right)

    print_tree_in_order(loaded_root.left.value)
