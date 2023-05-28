class LinkedList:
    def __init__(self):
        # Wzorzec głowy
        self.head = [None, None, None]
        # Head pointer to nie wartownik!
        self.head_pointer = None
        # self.content = [0 for _ in range(10)]
        self.content = []

    def is_empty(self):
        return len(self.content) == 0
        # return self.head is [None, None, None]

    def insert(self, key):
        new_node = [None, key, None]
        if self.is_empty():
            self.head = new_node
            self.content.append(self.head)
            self.head_pointer = 0
        else:
            current_node = self.content[self.head_pointer]
            while current_node[2] is not None:
                current_node = self.content[current_node[2]]
            # current_node[2] = new_node
            # new_node[0] = current_node

    def search(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node[1] == key:
                return current_node
            current_node = current_node[2]
        return None

    def delete(self, key):
        node_to_delete = self.search(key)
        if node_to_delete is None:
            return
        if node_to_delete[0] is None:
            self.head = node_to_delete[2]
        else:
            node_to_delete[0][2] = node_to_delete[2]
            if node_to_delete[2] is not None:
                node_to_delete[2][0] = node_to_delete[0]

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node[1], end=" ")
            current_node = current_node[2]
        print()

# Example usage:
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.display()  # Output: 10 20 30

node = linked_list.search(20)
print(node)  # Output: [None, 20, [None, 30, None]]

linked_list.delete(20)
linked_list.display()  # Output: 10 30
