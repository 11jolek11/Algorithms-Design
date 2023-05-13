from data.robots import Table
import inspect


def sort_by_group(group: str, table: Table):
    # t_copy = table.frame.copy()
    # t_copy.sort(key=lambda name: dict(list(inspect.getmembers(name)))[group])
    # return t_copy

    table.frame.sort(key=lambda name: dict(list(inspect.getmembers(name)))[group])


def binary_search(table: Table, wanted, group, left=0, right=None):
    table = table.frame
    if right is None:
        right = len(table)

    mid = left + (right - 1) // 2

    if dict(list(inspect.getmembers(table[mid])))[group] == wanted:
        return table[mid]

    elif dict(list(inspect.getmembers(table[mid])))[group] < wanted:
        left = mid + 1

    else:
        right = mid - 1
    return False


def binary_repeat(table: Table, wanted: list, group):
    found = False
    i = 0
    while not found:
        result = binary_search(table, wanted[i], group)
        if result is not False:
            print(result)
            break
        i += 1


if __name__ == '__main__':
    test = Table()
    test.fill(5)
    test.show()
    print("#################")
    sort_by_group("price", test)
    test.show()
