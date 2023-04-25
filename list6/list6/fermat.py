import random



def fast_modulo(a:int , b: int, n: int):
    d = 1
    b = bin(b)[2:]
    k = len(b)
    # a = a%n
    for i in range(k-1, -1, -1):
        if b[i] == '1':
            d = (d*a)%n
        a = (a**2)%n
    return d


def test(n, t):
    
    for _ in range(t):
        a = random.randint(2, n-2)
        if fast_modulo(a, n-1, n) != 1:
            return False
    return True


if __name__ == "__main__":
    # print(fast_modulo(12, 53, 7))
    # print(test(17, 20))
    print(test(1935751, 20))

