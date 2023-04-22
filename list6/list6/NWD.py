def ENWD(a, b):
    if b == 0:
        return a
    return ENWD(b, a%b)


def find_factors(num):
    factors = []
    k = 2
    while num != 1:
        while num % k == 0:
            num //= k
            factors.append(k)
        k += 1
    
    return factors


# def RNWD(a, b):
#     nwd = 1

#     divx = sorted(find_factors(a))
#     divy = find_factors(b)

#     # print(divx)
#     # print(divy)

#     for i in range(min([len(divx), len(divy)])):
#         if divy[i] == divx[i]:
#             nwd *= divx[i]
#     return nwd
#     # while divy[i] == divx[i]:
#     #     nwd *= divx[i]
#     #     i += 1
#     # return nwd

# def RNWD(a, b):
#     # TODO: add search for common factors
#     nwd = 1
#     divx = sorted(find_factors(max([a, b])))
#     divy = sorted(find_factors(min([a, b])))

#     for x in range(len(divx)):
#         for y in range(len(divy)):
#             if divx[x] == divy[y]:
#                 nwd *= divx[x]
#                 divy[y] = 0
#     return nwd

    # x, y = 0, 0
    # l_x, l_y = len(divx), len(divy)
    # while x < l_x:
    #     while y < l_y:
    #             if divx[x] == divy[y]:
    #                     divx.pop(x)
    #                     nwd *= divy.pop(y)
    #                     l_x = len(divx)
    #                     l_y = len(divy)
    #             else:
    #                     y += 1
    #     x += 1
    #     y = 0
    # return nwd


def find_common(a, b):
    n = len(a) - 1
    m = len(b) - 1
    c = []
    i, j = 0, 0
    while i <= n and j <= m:
        if a[i] < b[j]:
            i += 1
        else:
            if b[j] < a[i]:
                j += 1
            else:
                c.append(a[i])
                i += 1
                j += 1
    return c


def RNWD(a, b):
    nwd = 1

    divx = find_factors(a)
    divy = find_factors(b)

    common = find_common(divx, divy)

    for item in common:
        nwd *= item

    return nwd












    # FIXME: 
    # for x in range(len(divx)):
    #     for y in range(len(divy)):
    #         if divx[x] == divy[y]:
    #             divx.pop(x)
    #             nwd *= divy.pop(y)
    # return nwd

    # x, y = 0, 0
    # while x <= len(divx):
    #     while y <= len(divy):
    #         pass

# def RNWD(a, b):
#     def prime_factors(num):
#         factors = []
#         while num % 2 == 0:
#             factors.append(2)
#             num //= 2

#         for i in range(3, int(num**0.5) + 1, 2):
#             while num % i == 0:
#                 factors.append(i)
#                 num //= i

#         if num > 2:
#             factors.append(num)

#         return factors

#     prime_factors_a = prime_factors(a)
#     prime_factors_b = prime_factors(b)

#     common_factors = list(set(prime_factors_a) & set(prime_factors_b))

#     if not common_factors:
#         return 1

#     gcd = 1
#     for factor in common_factors:
#         gcd *= factor

#     return gcd

if __name__ == '__main__':
    pass
    print(RNWD(10, 6))
    # print(ENWD(10, 6))
    # 2, 2, 5
    # 2, 2, 2, 5

    ###################
    print(RNWD(40, 20))
    ###################


    # print(gcd_prime_factorization(20, 40))
    print(RNWD(70, 30))
    print(RNWD(4, 6))
    print(RNWD(50, 50))
    print(RNWD(3, 7))
    # print(gcd_prime_factorization(30, 70))

    # print(ENWD(12, 20))
