from math import sqrt, floor



def sieve(p: int):
    if p <= 1:
        print("p should be bigger than 1!")
        return []

    x = [True for _ in range(p+1)]

    for i in range(2, floor(sqrt(p))+1):
        if x[i]:
            for j in range(2, floor(p/i)+1):
                x[i*j] = False
    # return x[1:]
    mat = x[1:]
    for i in range(len(mat)):
        if mat[i] is True:
            print(i+1)


if __name__ == "__main__":
    n = 10
    numbers = list(range(n))
    binary = sieve(15)
    print(binary)

