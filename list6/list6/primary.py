from math import sqrt, floor



# def find_primary(divider: int, orginal_number: int, result: list=[]):
#     if divider == floor(sqrt(orginal_number)):
#         print(result)
#         return result
#     for number in range(2, divider):
#         if divider % number == 0:
#             result.append(number)
#             find_primary(int(divider/number), orginal_number, result)


# def find_primary(divider: int, orginal_number: int, result: list=[]):
#     for number in range(2, floor(sqrt(divider))+1):
#         print(f'{number}/{divider}')
#         if divider % number == 0:
#             result.append(number)
#             find_primary(int(divider/number), orginal_number, result)
#             break
#     return result

def find_primes(orginal_number, divider, result):
    print(f'New spawn {orginal_number} {divider} {result}')
    for number in range(2, floor(sqrt(divider))+1):
       if orginal_number%number == 0:
            print(f'{orginal_number}/{number} = {orginal_number/number}')  
            result.append(number)
            return find_primes(orginal_number/number, number, result)
            # break
    return result


def prime_factorize(number):
    def recurse(factors, x, n):
        if x<2: return factors 
        if n >  floor(sqrt(x))+1: 
            factors.append(x)
            return factors
        if x%n==0:
            factors.append(n)
            return recurse(factors, x/n, n)
        else:
            return recurse(factors, float(x), n+1)
    return recurse([], number, 2)


if __name__ == "__main__":
    # print(find_primes(100, 100, []))
    print(prime_factorize(125))

