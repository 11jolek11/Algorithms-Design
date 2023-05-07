def wrapper_max(table, n):
    if n == 1: #O1
        return table[0] #O1
    x = wrapper_max(table[n//2:], n - n//2)#dziele
    return x if x > table[0] else table[0]


def maximum(table):
    return wrapper_max(table, len(table))


def custom_avr(table):
    n = len(table)
    if n == 1:
        return table[0]
    else:
        midpoint = n // 2
        return (midpoint * custom_avr(table[:midpoint]) + (n - midpoint) * custom_avr(table[midpoint:])) / n

# u
def sbig(table, n: int, first: float|int, second: float|int):
    if n < 2:
        print(f'Second --> {second}')
    else:
        if table[n] > first:
            second = first
            first = table[n]
        elif table[n] > second and table[n] != first:
            second = table[n]
        sbig(table, n-1 , first, second)


if __name__ == "__main__":
    # p = [2, 2, 1, 7, 7, 4, -3]
    from random import randint
    p = [randint(1, 6) for _ in range(100000)]
    print(maximum(p))
    # print(custom_avr(p))
    # print(findsecondlargest(p, 0, 5, 2))
    # sbig(p, len(p)-1, max(p[:2]), min(p[:2]))
