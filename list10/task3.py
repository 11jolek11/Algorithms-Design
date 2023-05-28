# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def is_empty(self):
#         return self.head is None

#     def insert(self, key):
#         new_node = [None, key, None]

#         if self.is_empty():
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node[0] = self.tail
#             self.tail[2] = new_node
#             self.tail = new_node

#     def delete(self, key):
#         current = self.head

#         while current is not None:
#             if current[1] == key:
#                 prev_node = current[0]
#                 next_node = current[2]

#                 if prev_node is not None:
#                     prev_node[2] = next_node
#                 else:
#                     self.head = next_node

#                 if next_node is not None:
#                     next_node[0] = prev_node
#                 else:
#                     self.tail = prev_node

#                 return  # Found and deleted the node

#             current = current[2]

#     def search(self, key):
#         current = self.head

#         while current is not None:
#             if current[1] == key:
#                 return current

#             current = current[2]

#         return None

#     def display(self):
#         current = self.head

#         while current is not None:
#             print(current[1], end=" ")
#             current = current[2]

#         print()


# # Example usage:
# my_list = LinkedList()

# my_list.insert(5)
# my_list.insert(10)
# my_list.insert(15)
# my_list.insert(20)

# my_list.display()  # Output: 5 10 15 20

# my_list.delete(5)
# # my_list.delete(10)
# # my_list.delete(15)

# my_list.display()  # Output: 5 20

# # node = my_list.search(20)
# # if node is not None:
# #     print("Node found!")
# # else:
# #     print("Node not found!")


# class LinkedList:
#     def __init__(self):
#         self.table = {}
#         self.head = None
#         self.tail = None
#         self.index = 0

#     def is_empty(self):
#         return self.head is None

#     def insert(self, key):
#         new_node = [None, key, None]

#         if self.is_empty():
#             self.head = self.index
#             self.tail = self.index
#         else:
#             new_node[0] = self.tail
#             self.table[self.tail][2] = self.index
#             self.tail = self.index

#         self.table[self.index] = new_node
#         self.index += 1

#     def delete(self, key):
#         current_index = self.head

#         while current_index is not None:
#             current_node = self.table[current_index]

#             if current_node[1] == key:
#                 prev_index = current_node[0]
#                 next_index = current_node[2]

#                 if prev_index is not None:
#                     self.table[prev_index][2] = next_index
#                 else:
#                     self.head = next_index

#                 if next_index is not None:
#                     self.table[next_index][0] = prev_index
#                 else:
#                     self.tail = prev_index

#                 del self.table[current_index]  # Remove node from table
#                 return  # Found and deleted the node

#             current_index = current_node[2]

#     def search(self, key):
#         current_index = self.head

#         while current_index is not None:
#             current_node = self.table[current_index]

#             if current_node[1] == key:
#                 return current_node

#             current_index = current_node[2]

#         return None

#     def display(self):
#         current_index = self.head

#         while current_index is not None:
#             current_node = self.table[current_index]
#             print(current_node[1], end=" ")
#             current_index = current_node[2]

#         print()


# # Example usage:
# my_list = LinkedList()

# my_list.insert(5)
# my_list.insert(10)
# my_list.insert(15)
# my_list.insert(20)

# my_list.display()  # Output: 5 10 15 20

# my_list.delete(10)
# my_list.delete(15)

# my_list.display()  # Output: 5 20

# node = my_list.search(20)
# if node is not None:
#     print("Node found!")
# else:
#     print("Node not found!")

class LinkedList:
    def __init__(self):
        self.nodes = []
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert(self, key):
        new_node = [None, key, None]

        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            new_node[2] = self.head
            self.nodes[self.head][0] = len(self.nodes)
            self.head = len(self.nodes)

        self.nodes.append(new_node)

    def delete(self, key):
        current_index = self.head

        while current_index is not None:
            current_node = self.nodes[current_index]

            if current_node[1] == key:
                prev_index = current_node[0]
                next_index = current_node[2]

                if prev_index is not None:
                    self.nodes[prev_index][2] = next_index
                else:
                    self.head = next_index

                if next_index is not None:
                    self.nodes[next_index][0] = prev_index
                else:
                    self.tail = prev_index

                self.nodes[current_index] = [[], [], []]
                # del self.nodes[current_index]  # Remove node from list
                # return  # Found and deleted the node

            current_index = current_node[2]

    def search(self, key):
        current_index = self.head

        while current_index is not None:
            current_node = self.nodes[current_index]

            if current_node[1] == key:
                return current_node

            current_index = current_node[2]

        return None

    def display(self):
        current_index = self.head

        while current_index is not None:
            current_node = self.nodes[current_index]
            print(current_node[1], end=" ")
            current_index = current_node[2]

        print()


# Example usage:
my_list = LinkedList()

my_list.insert(5)
my_list.insert(10)
my_list.insert(15)
my_list.insert(20)

my_list.display()  # Output: 20 15 10 5

my_list.delete(5)
my_list.display()
my_list.delete(15)

my_list.display()  # Output: 20 5

node = my_list.search(20)
if node is not None:
    print("Node found!")
else:
    print("Node not found!")
