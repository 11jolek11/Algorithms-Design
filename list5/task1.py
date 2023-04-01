# cache = {0: 1}

# def first(n):
#     if n in cache:
#         print('first')
#         print(cache)
#         return cache[n]

#     cache[n] = 3**n + first(n-1)
#     return cache[n]


cache = {-1: 0, 0:0}
def second(n):
    if n in cache:
        return cache[n]

    cache[n] = n + second(n - 2)
    return cache[n]


# cache = {0: 0, 1: 1}

# def fibonacci(n) -> float:
#     if n in cache:
#         return cache[n]

#     cache[n] = fibonacci(n-1) + fibonacci(n-2)
#     return cache[n]


if __name__ == "__main__":
    print([second(i) for i in range(4)])
    # print([first(i) for i in range(3)])
   #print(fibonacci(4))

