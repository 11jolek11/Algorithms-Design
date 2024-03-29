def get_bit(line, pos_for_bit, state, powe):
    k = powe[pos_for_bit - 1]
    if line % (k // 2):
        return str(state[pos_for_bit - 1])
    else:
        bit = 1 - state[pos_for_bit - 1]
        state[pos_for_bit - 1] = bit
        if line % k == 0:
            state[pos_for_bit - 1] = 1 - bit
            bit = 1 - bit
        return str(bit)


def gray_codes(n):
    # O(2^n)
    lines = 1 << n
    state = [0] * n
    powe = [1 << i for i in range(1, n + 1)]
    for line in range(lines):
        gray_code = ""
        for pos_for_bit in range(n, 0, -1):
            gray_code += get_bit(line, pos_for_bit, state, powe)
        yield gray_code


def subset_sum(set_A: list, target=0):
    discovered = []
    codes = gray_codes(len(set_A))
    while True:
        try:
            decision = next(codes)
        except StopIteration:
            print("Complete!")
            break
        temp = []
        for i in range(len(set_A)):
            temp.append(set_A[i] * int(decision[i]))
            # if sum(temp) == target and int(decision[i]) >= 1:
        if sum(temp) == target:
            discovered.append(tuple(decision))

    discovered = list(set(discovered))
    print(discovered)

    to_return = []

    for item in discovered:
        temp = []
        for i in range(len(item)):
            if item[i] == "1":
                temp.append(set_A[i])
        to_return.append(temp)
    return tuple(to_return)
    # return set(discovered)


if __name__ == "__main__":
    print(subset_sum([4, -4, 1]))

# def gray_codes(n):
#   if n == 1:
#     return ['0', '1']
#   r = gc(n - 1)
#   return ['0' + e for e in r] + ['1' + e for e in reversed(r)]
