# def bubbleSort(alist):
#     # Time complexity O(n^2)
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i]<alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#     return(alist)

def biggest_element(table: list[float | int]) -> float:
    # O(n)
    register = table[0]
    for item in table:
        if item >= register:
            register = item
    return register


def biggest_second_element(table: list[float | int]) -> float:
    if len(table) == 1:
        return table
    
    mx = max(table[0], table[1]) 

    b_max = min(table[0], table[1]) 

    for i in range(2,len(table)): 
        if table[i] > mx: 
            b_max = mx
            mx = table[i] 
        if  mx != table[i] and table[i] > b_max: 
            b_max = table[i]
    return b_max


def custom_mean(table: list[float | int]) -> float:
    p = 0
    temp = 0
    # while i <= len(table):
    for i in range(len(table)):
        p += 1
        temp += table[i]
    return temp / p


if __name__ == "__main__":
    # test = [1, 4, 3, 2, 5, 3, 1]
    test = [10, 20, 4, 45, 99, 20]
    # print(biggest_element(test))
    print(biggest_second_element(test))
    # print(test())
    # print(custom_mean(test))

# def bubbleSort(alist):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i]<alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#     return(alist)