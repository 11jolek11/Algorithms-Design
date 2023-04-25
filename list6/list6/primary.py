from math import sqrt, floor



def prime_factorize(number):
    def recurse(factors, x, n):
        if x<2: return factors 
        if n >  floor(sqrt(x))+1: 
            factors.append(x)
            return factors
        if x%n==0:
            factors.append(n)
            return recurse(factors, x//n, n)
        else:
            return recurse(factors, x, n+1)
    return recurse([], number, 2)


if __name__ == "__main__":
    # print(find_primes(100, 100, []))
    print(prime_factorize(100))

