import time



def biggest_element(table: list[float | int]) -> float:
    register = table[0]
    for item in table:
        if item >= register:
            register = item
    return register


def biggest_second_element(table: list[float | int]) -> float:
    pass    


def custom_mean(table: list[float | int]) -> float:
    p = 0
    temp = 0
    # while i <= len(table):
    for i in range(len(table)):
        p += 1
        temp += table[i]
    return temp / p


if __name__ == "__main__":
    test = [1, 4, 4, 5, 1]
    print(biggest_element(test))
    print(biggest_second_element(test))
    print(custom_mean(test))
