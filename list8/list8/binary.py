from data.robots import Table, Robot
from math import floor
import inspect


def sort_by_group(group: str, table: Table):
    # table.frame.sort(key=lambda name: dict(list(inspect.getmembers(name)))[group])
    table.frame.sort(key=lambda name: getattr(name, group))


def binary_search(table: list, wanted, group: str, left, right):
    while left < right:

        # mid = left + (right - 1) // 2
        mid = floor(left + (right - 1))

        # if dict(list(inspect.getmembers(table[mid])))[group] == wanted:
        if getattr(table[mid], group) == wanted:
            # if getattr(table[mid], group) is wanted:
            return table[mid]

        # elif dict(list(inspect.getmembers(table[mid])))[group] >= wanted:
        elif getattr(table[mid], group) >= wanted:
            right = mid - 1

        else:
            left = mid + 1


def binary_repeat(table: Table, wanted: list, group: str):
    # found = False
    # i = 0
    for i in range(len(wanted)):
        result = binary_search(table.frame, wanted[i], group, 0, len(table.frame)-1)
        if result is not None:
            print(result)
            break


if __name__ == "__main__":
    test = Table()
    test.fill(200)
    # test.frame = [
    #     Robot('AGV', 700.0, 22, 0),
    #     Robot('ASV', 699.0, 42, 0),
    #     Robot('ASV', 698.0, 97, 1),
    #     Robot('ASV', 698.0, 17, 1),
    #     Robot('AGV', 698.0, 41, 1)
    # ]
    # test.show()
    sort_by_group("robot_range", test)
    # test.show()
    search_keys = [2, 98, 902]
    # print(binary_search(test.frame, 42, "robot_range", 0, len(test.frame)-1))

    binary_repeat(test, search_keys, "robot_range")
