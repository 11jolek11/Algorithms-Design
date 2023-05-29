from robots import RobotCreator
import numpy as np


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


    def delete(self, key, attr: str):
        # FIXME: usuwanie ze środka nie działa poprawnie wycina wszystko
        current_index = self.head

        while current_index is not None:
            current_node = self.nodes[current_index]

            if getattr(current_node[1], attr) == key:
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

                # self.nodes[current_index] = [None, None, None]  # <-- empty node
                self.nodes[current_index] = [-1, -1, -1]  # <-- empty node
                # del self.nodes[current_index]

            current_index = current_node[2]

    def search(self, key, attr):
        current_index = self.head

        while current_index is not None:
            current_node = self.nodes[current_index]

            if getattr(current_node[1], attr) == key:
                return current_node[1]

            current_index = current_node[2]

        return None

    # def display(self):
    #     current_index = self.head

    #     while current_index is not None:
    #         current_node = self.nodes[current_index]
    #         print(current_node[1], end="---")
    #         current_index = current_node[0]

    #     print()

    def merge_sort(self, attr: str="price"):
        # TODO: sortowanie wzgledem ceny <== DONE
        self.head = self._merge_sort(self.head, attr)
        self._update_tail()

    def _merge_sort(self, head, attr):
        if head is None or self.nodes[head][2] is None:
            return head

        middle = self._get_middle(head)

        # split
        next_to_middle = self.nodes[middle][2]
        self.nodes[middle][2] = None
 
        left = self._merge_sort(head, attr)
        right = self._merge_sort(next_to_middle, attr)

        # Merge
        return self._merge(left, right, attr)

    def _get_middle(self, head):
        slow = head
        fast = head

        while fast is not None and self.nodes[fast][2] is not None:
            fast = self.nodes[self.nodes[fast][2]][2]
            if fast is not None:
                slow = self.nodes[slow][2]

        return slow

    def _merge(self, left, right, attr):
        if left is None:
            return right
        if right is None:
            return left

        if getattr(self.nodes[left][1], attr) <= getattr(self.nodes[right][1], attr):
            result = left
            self.nodes[result][2] = self._merge(self.nodes[left][2], right, attr)
        else:
            result = right
            self.nodes[result][2] = self._merge(left, self.nodes[right][2], attr)

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


if __name__ == "__main__":
    my_list = LinkedList()

    my_list.insert(RobotCreator.create())
    # print(my_list.nodes)
    my_list.insert(RobotCreator.create())
    # print(my_list.nodes)
    my_list.insert(RobotCreator.create())
    # print(my_list.nodes)
    my_list.insert(RobotCreator.create())

    # my_list.display()

    # my_list.merge_sort()
    # my_list.display()

    my_list.nodes[0][1].robot_range = 88

    # print("########################################")
    # # my_list.display()
    # print(np.asarray(my_list.nodes))
    # print(my_list.search(88, "robot_range"))
    # print("########################################")


    my_list.nodes[1][1].price = 1000.0
    # print("---------------------------------------------")
    print(np.asarray(my_list.nodes))
    print("---------------------------------------------")
    # my_list.display()
    my_list.delete(1000.0, "price")
    print(np.asarray(my_list.nodes))
    # my_list.display()

