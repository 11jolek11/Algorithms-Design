from data.robots import Table, Robot
import inspect


def sort_by_group(group: str, table: Table):
    # t_copy = table.frame.copy()
    # t_copy.sort(key=lambda name: dict(list(inspect.getmembers(name)))[group])
    # return t_copy

    table.frame.sort(key=lambda name: dict(list(inspect.getmembers(name)))[group])


def gen_keys(vector: list):
    keys = []
    for key in vector:
        if type(key) is not list:
            keys.append([key, ])
        elif key is None:
            keys.append(None)
        else:
            keys.append(key)
    return keys


# V2
def have_prop(robot: Robot, vector: list):
    prop = [robot.type, robot.price, robot.robot_range, robot.camera]
    counter = 0
    for i in range(len(vector)):
        if vector[i] is not None and prop[i] in vector[i]:
            counter += 1
        else:
            counter -= 1
    return counter == len(prop)

# def binary_search(table: list, wanted, left=0, right=None):
#     if right is None:
#         right = len(table)

#     mid = left + (right - 1) // 2



if __name__ == '__main__':
    test = Table()
    test.fill(5)
    test.show()
    print("#################")
    sort_by_group("price", test)
    test.show()
