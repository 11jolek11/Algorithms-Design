import time



def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return(alist)

def biggest_element(table: list[float | int]) -> float:
    register = table[0]
    for item in table:
        if item >= register:
            register = item
    return register


def biggest_second_element(table: list[float | int]) -> float:
    temp = -100
    # table = sorted(table, reverse=True)
    table = bubbleSort(table)
    for i in range(len(table)):
        if table[i] >= temp:
            if table[i] == table[i+1]:
                return table[i]
            # temp = table[i]


def custom_mean(table: list[float | int]) -> float:
    p = 0
    temp = 0
    # while i <= len(table):
    for i in range(len(table)):
        p += 1
        temp += table[i]
    return temp / p


if __name__ == "__main__":
    test = [1, 4, 3, 2, 5, 1]
    # print(biggest_element(test))
    print(biggest_second_element(test))
    # print(custom_mean(test))

# def bubbleSort(alist):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i]<alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#     return(alist)