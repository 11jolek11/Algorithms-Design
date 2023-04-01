def swap(table, a, b):
    temp = table[a]
    table[a] = table[b]
    table[b] = temp
    return table


# def task(tablica):
#     # for i in 
#     # for i in range(len(t
#     for i in range(len(tablica)):
#         temp_a = 0
#         temp_b = 0
#         if tablica[i]%2 != 0:
#             temp_a = i
#         if tablica[-i]%2 == 0:
#             temp_b = -i
#         swap(tablica, temp_a, temp_b)
#     return tablica


def taskw(table):
    for x in range(len(table)//2):
        for y in range(len(table)//2, 0, -1):
            if table[x] % 2 == 0 and table[len(table)- y]%2 != 0:
                table = swap(table, x,len(table) - y)
    return table

# def taskr(tab)

if __name__ == "__main__":
    print(taskw([0, 2, 5, 3, 8, 3, 1, 4]))
    print(taskw([0, 2, 4, 6]))
    print(taskw([1, 3, 5, 7]))
