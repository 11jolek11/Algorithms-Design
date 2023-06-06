import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def plot_binary_tree(root):
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

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    plot_binary_tree(root)
