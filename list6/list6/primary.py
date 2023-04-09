from math import sqrt, floor



# def find_primary(divider: int, orginal_number: int, result: list=[]):
#     if divider == floor(sqrt(orginal_number)):
#         print(result)
#         return result
#     for number in range(2, divider):
#         if divider % number == 0:
#             result.append(number)
#             find_primary(int(divider/number), orginal_number, result)


def find_primary(divider: int, orginal_number: int, result: list=[]):
    # 
    for number in range(2, floor(sqrt(divider))+1):
        # if divider / number == 1:
        #     result.append(number)
        #     return result
        if divider % number == 0:
            result.append(number)
            find_primary(int(divider/number), orginal_number, result)
        # else:
        #     result.append(divider)
    return result


if __name__ == "__main__":
    print(find_primary(125, 125))

