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


def RNWD(a, b):
    nwd = 1

    divx = find_factors(a)
    divy = find_factors(b)
    pos_sol = set(divx).intersection(divy)
    for element in pos_sol:
        nwd *= element
    return nwd

if __name__ == '__main__':
    print(RNWD(10, 6))