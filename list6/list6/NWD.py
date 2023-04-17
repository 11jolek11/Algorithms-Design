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

def gcd_prime_factorization(a, b):
    """
    Function to find the GCD of two numbers using prime factorization.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: The GCD of the two numbers.
    """
    # Function to find prime factors of a number
    def prime_factors(num):
        factors = []
        # Divide the number by 2 until it is odd
        while num % 2 == 0:
            factors.append(2)
            num //= 2

        # Divide the number by odd numbers starting from 3
        for i in range(3, int(num**0.5) + 1, 2):
            while num % i == 0:
                factors.append(i)
                num //= i

        # If the remaining number is greater than 2, it is a prime factor
        if num > 2:
            factors.append(num)

        return factors

    # Find prime factors of both numbers
    prime_factors_a = prime_factors(a)
    prime_factors_b = prime_factors(b)

    # Find the intersection of prime factors
    common_factors = list(set(prime_factors_a) & set(prime_factors_b))

    # If there are no common prime factors, the GCD is 1
    if not common_factors:
        return 1

    # Multiply the common prime factors to get the GCD
    gcd = 1
    for factor in common_factors:
        gcd *= factor

    return gcd

if __name__ == '__main__':
    print(RNWD(10, 6))
    print(ENWD(10, 6))