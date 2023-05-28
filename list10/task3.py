# class LinkedList:
#     def __init__(self):
#         self.nodes = []
#         self.head = None
#         self.tail = None

#     def is_empty(self):
#         return self.head is None

#     def insert(self, key):
#         new_node = [None, key, None]

#         if self.is_empty():
#             self.head = 0
#             self.tail = 0
#         else:
#             new_node[2] = self.head
#             self.nodes[self.head][0] = len(self.nodes)
#             self.head = len(self.nodes)

#         self.nodes.append(new_node)

#     def delete(self, key):
#         current_index = self.head

#         while current_index is not None:
#             current_node = self.nodes[current_index]

#             if current_node[1] == key:
#                 prev_index = current_node[0]
#                 next_index = current_node[2]

#                 if prev_index is not None:
#                     self.nodes[prev_index][2] = next_index
#                 else:
#                     self.head = next_index

#                 if next_index is not None:
#                     self.nodes[next_index][0] = prev_index
#                 else:
#                     self.tail = prev_index

#                 self.nodes[current_index] = [None, 0, None]  # Replace with empty node
#                 return  # Found and deleted the node

#             current_index = current_node[2]

#     def search(self, key):
#         current_index = self.head

#         while current_index is not None:
#             current_node = self.nodes[current_index]

#             if current_node[1] == key:
#                 return current_node

#             current_index = current_node[2]

#         return None

#     def display(self):
#         current_index = self.head

#         while current_index is not None:
#             current_node = self.nodes[current_index]
#             print(current_node[1], end=" ")
#             current_index = current_node[2]

#         print()

#     def sort(self):
#         if self.is_empty():
#             return

#         n = len(self.nodes)
#         for i in range(n - 1):
#             for j in range(n - i - 1):
#                 node1 = self.nodes[j]
#                 node2 = self.nodes[j + 1]
#                 if node1[1] > node2[1]:
#                     self.nodes[j], self.nodes[j + 1] = self.nodes[j + 1], self.nodes[j]

#         # Update head and tail
#         self.head = self.nodes[0][2]
#         self.tail = self.nodes[n - 1][0]
#         self.nodes[self.head][0] = None
#         self.nodes[self.tail][2] = None


# # Example usage:
# my_list = LinkedList()

# my_list.insert(5)
# my_list.insert(10)
# my_list.insert(15)
# my_list.insert(20)

# my_list.display()  # Output: 20 15 10 5

# my_list.delete(10)
# my_list.delete(15)

# my_list.display()  # Output: 20 5

# node = my_list.search(20)
# if node is not None:
#     print("Node found!")
# else:
#     print("Node not found!")

# my_list.sort()
# my_list.display()  # Output: 5 20


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

                self.nodes[current_index] = [None, None, None]  # Replace with empty node
                return  # Found and deleted the node

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

    def merge_sort(self):
        self.head = self._merge_sort(self.head)
        self._update_tail()

    def _merge_sort(self, head):
        if head is None or self.nodes[head][2] is None:
            return head

        # Find the middle of the linked list
        middle = self._get_middle(head)

        # Split the linked list into two halves
        next_to_middle = self.nodes[middle][2]
        self.nodes[middle][2] = None

        # Perform merge sort recursively on both halves
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        # Merge the two sorted halves
        return self._merge(left, right)

    def _get_middle(self, head):
        slow = head
        fast = head

        while fast is not None and self.nodes[fast][2] is not None:
            fast = self.nodes[self.nodes[fast][2]][2]
            if fast is not None:
                slow = self.nodes[slow][2]

        return slow

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if self.nodes[left][1] <= self.nodes[right][1]:
            result = left
            self.nodes[result][2] = self._merge(self.nodes[left][2], right)
        else:
            result = right
            self.nodes[result][2] = self._merge(left, self.nodes[right][2])

        self.nodes[result][0] = None

        return result

    def _update_tail(self):
        current_index = self.head

        while current_index is not None:
            next_index = self.nodes[current_index][2]

            if next_index is None:
                self.tail = current_index
                break

            current_index = next_index


# Example usage:
my_list = LinkedList()

my_list.insert(5)
my_list.insert(10)
my_list.insert(15)
my_list.insert(20)

my_list.display()  # Output: 20 15 10 5

# my_list.delete(10)
# my_list.delete(15)

my_list.display()  # Output: 20 5

my_list.merge_sort()
my_list.display()  # Output: 5 20
