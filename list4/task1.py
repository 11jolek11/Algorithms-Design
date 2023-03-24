def biggest_element(table: list[float | int]) -> float:
    register = table[0]
    for item in table:
        if item >= register:
            register = item
    return register


def biggest_second_element(table: list[float | int]) -> float:
    registers = [0, table[0]]
    for i in range(len(table)):
        if table[i] > registers[1]:
            registers[1] = table[i]
        if table[i] == registers[1]:
            registers[0] == table[i]
    return registers[0]


def custom_mean(table: list[float | int]) -> float:
    i = 0
    temp = 0
    while i <= len(table):
        temp += table[i]
    return temp / i
