def ENWD(a, b):
    if b == 0:
        return a
    return ENWD(b, a%b)


def find_factors(num):
    divs = []
    for value in range(1, num + 1):
        if num % value == 0:
            divs.append(value)
    return divs


def RNWD(a, b):
    divx = find_factors(a)
    divy = find_factors(b)
    pos_sol = set(divx).intersection(divy)
    return max(pos_sol)
