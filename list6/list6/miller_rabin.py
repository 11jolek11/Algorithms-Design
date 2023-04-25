import random



def fast_modulo(a:int , b: int, n: int):
    """
    a^b mod n
    """
    d = 1
    b = bin(b)[2:]
    k = len(b)
    # a = a%n
    for i in range(k-1, -1, -1):
        if b[i] == '1':
            d = (d*a)%n
        a = (a**2)%n
    return d


# def witness(a, n):
#     d = 1
#     b = bin(n-1)[2:]
#     k = len(b)
#     for i in range(k-1, -1, -1):
#         x = d
#         # TODO: may need to swap "a" with "d"
#         # d = (d**2)%n
#         # d = fast_modulo(d, 2, n)
#         a = fast_modulo(a, 2, n)
#         if d == 1 and x != 1 and x != n -1:
#             return True
#         if b[i] != '1':
#             d = (d*a)%n
#     if d != 1:
#         return True
#     return False


# def test(n, t):
#     temp = []
#     for _ in range(t):
#         a = random.randint(1, n-1)
#         temp.append(witness(a, n))
#     # Check if all runs were True
#     if all(temp):
#         return True
#     return False


import random

def miller_rabin(n, q):
    # if n<=3:
    #     raise Exception('n should b greater than 3.')
    if n % 2 == 0:
        return False
    # Find u odd such that n-1 = 2^k * u 
    u = n - 1
    k = 0
    while (u % 2 == 0):
        u //= 2
        k+=1
    for _ in range(q):
        #Let a be randomly chosen from {2,...,n − 2};
        a = random.randint(1,n-1)
        # b = a^u mod n
        # b = pow(a,u,n)
        b = fast_modulo(a, u, n)
        if b==1 or b ==n-1:
            continue
        for _ in range (k-1):
            # b= (b*b) % n
            b = fast_modulo(b, 2, n)
            if b==n-1: break 
        else: 
            return False
    return True    


if __name__ == '__main__':
    n = 1935751
    t = 10
    print(set([miller_rabin(n, t) for _ in range(1000)]))
    # print(set([witness(1, n-1) for _ in range(10000)]))
    # print(witness(1, n-1))
    # print(test(n, 10))
