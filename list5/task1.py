from math import sqrt



# cache = {0: 1}

# def first(n):
#     if n in cache:
#         return cache[n]

#     cache[n] = 3**n + first(n-1)
#     return cache[n]

# def check_first(n):
#     tt = lambda n: 0.5*(-3+3**(n+1)+2*cache[0])
#     ground_truth = [tt(i) for i in range(n)]
#     test = [first(i) for i in range(n)]
#     for i in range(n):
#         if ground_truth[i] - test[i] != 0:
#             return False
#     return True



cache = {-1: 0, 0:0}
def second(n):
    if n in cache:
        return cache[n]

    cache[n] = n + second(n - 2)
    return cache[n]

def check_second(n):
    # tt = lambda n: 0.25*n*(n+3) - 0.125*(2*n+3)*(-1)**(2*n) + cache[-1] + cache[0]*(-1)**n
    # tt = lambda n: 0.25*n*(n+3) - 0.125*(2*n+3)*(-1)**(2*n)
    tt = lambda n: 0.125*(2*(n+1)*(n+2)+ (-1)**(n+1) + (-1)**(2*n+1)*(2*n+3))

    ground_truth = [tt(i) for i in range(-1, n)]
    test = [second(i) for i in range(-1, n)]
    for i in range(n):
        if ground_truth[i] - test[i] != 0:
            print(f'Test: {test[i]}, true value: {ground_truth[i]}')
            return False
    return True





# cache = {0: 0, 1: 1}

# def fibonacci(n) -> float:
#     if n in cache:
#         return cache[n]

#     cache[n] = fibonacci(n-1) + fibonacci(n-2)
#     return cache[n]

# def check_fibonacci(n):
#     fib = lambda n: (((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)*(1/sqrt(5))
#     ground_truth = [fib(i) for i in range(n)]
#     test = [fibonacci(i) for i in range(n)]
#     for i in range(n):
#         if ground_truth[i] - test[i] != 0:
#             return False
#     return True


if __name__ == "__main__":
    # print([second(i) for i in range(4)])
    # print([first(i) for i in range(3)])
   # print(check_fibonacci(4))
   print(check_second(4))

