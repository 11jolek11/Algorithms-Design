# import itertools as it



# def erat3( ):
#     D = { 9: 3, 25: 5 }
#     yield 2
#     yield 3
#     yield 5
#     MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
#     MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

#     for q in it.compress(
#             it.islice(it.count(7), 0, None, 2),
#             it.cycle(MASK)):
#         p = D.pop(q, None)
#         if p is None:
#             D[q*q] = q
#             yield q
#         else:
#             x = q + 2*p
#             while x in D or (x%30) not in MODULOS:
#                 x += 2*p
#             D[x] = p


# if __name__ == '__main__':
#     gen = erat3()
#     x = [next(gen) for _ in range(10000)]
#     print(x)




# def test(a, b):
#     nwd = 1 

#     x, y = 0, 0
#     while x < len(a):
#         while y < len(b):
#                 if a[x] == b[y]:
#                         print(a.pop(x))
#                         nwd *= b.pop(y)
#                 else:
#                         y += 1
#         x += 1
#     return nwd

# if __name__ == '__main__':
#     a = [2, 2, 5]
#     b = [2, 2, 3, 5]
#     print(test(a, b))
    # test(b ,a)

def test(a, b):
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


if __name__ == '__main__':
    x = [1, 2, 2, 4, 5]
    y = [2, 2, 2, 3, 5, 7]
    print(test(y, x))
    print(test(x , y))
