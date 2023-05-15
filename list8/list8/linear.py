from data.robots import Table, Robot
from typing import List


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
        elif vector[i] is None:
            counter += 1
        else:
            counter -= 1
    return counter == len(prop)

# V3
# def have_prop(robot: Robot, vector: list):
#     prop = [robot.type, robot.price, robot.robot_range, robot.camera]
#     counter = 0
#     for i in range(len(vector)):
#         if vector[i] is not None and prop[i] in vector[i]:
#             counter += 1
#         else:
#             counter -= 1
#     return counter == len(prop)

def linear_search(data: list, search: list):
    for robot in data:
        # V1
        # if ((robot.type is in search[0]) ^ (search[0] == None)) and (robot.price is in search[1] ^ search[1] == None) and (robot.robot_range is in search[2] ^ search[2] == None) and (robot.camera is in search[3] ^ search[3] == None):
        #     return robot
        # V2
        if have_prop(robot, search):
            return robot
        # V3 
        # if have_prop(robot, search):
        #     return True
    return None

if __name__ == "__main__":
    test = Table()
    test.frame = [
        Robot('AGV', 700.0, 22, 0),
        Robot('ASV', 699.0, 42, 0),
        Robot('ASV', 698.0, 41, 1),
        Robot('ASV', 698.0, 41, 1),
        Robot('AGV', 698.0, 41, 1)
    ]
    search_keys = [['ASV', 'AGV'], None, None, [1]]

    print(linear_search(test.frame, search_keys))
    # test.show()
