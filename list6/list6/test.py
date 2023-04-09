def find_factors(num):
    divs = []
    for value in range(1, num + 1):
        if num % value == 0:
            divs.append(value)
    return divs

def hcf(x, y):
    divx = find_factors(x)
    divy = find_factors(y)
    pos_sol = set(divx).intersection(divy)
    return max(pos_sol)

print(hcf(56, 12)) 

# def find_factors(num):
#     divs = []
#     for value in range(1, num + 1):
#         if num % value == 0:
#             divs.append(value)
#     return divs

# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for a in range(2,x-1): # technically you can go upto sqrt(n) but if math is allowed 
#             if x % a == 0:
#                 return False
#     return True

# def hcf(x, y):
#     if is_prime(x) and is_prime(y):
#         return 1

#     divx = find_factors(x)
#     divy = find_factors(y)
#     pos_sol = [x for x in divx if x in divy]
#     return max(pos_sol)

# print(hcf(4, 12)) 