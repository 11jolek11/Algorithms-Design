def get_bit(line, bit_pos, state, powers):
    k = powers[bit_pos-1]
    if line % (k // 2):
        return str(state[bit_pos-1])
    else:
        bit = 1 - state[bit_pos - 1]
        state[bit_pos - 1] = bit
        if line % k == 0:
            state[bit_pos - 1] = 1 - bit
            bit = 1 - bit
        return str(bit)

def gray_codes(n):
    lines = 1 << n
    state = [0] * n
    powers = [1 << i for i in range(1, n + 1)]
    for line in range(lines):
        gray_code = ''
        for bit_pos in range(n, 0, -1):
            gray_code += get_bit(line, bit_pos, state, powers)
        yield gray_code

def subset_sum(set_A, target=0):
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
            temp.append(set_A[i]*int(decision[i]))
            # if sum(temp) == target and int(decision[i]) >= 1:
        if sum(temp) == target:
            discovered.append(tuple(decision))
    
    discovered = list(set(discovered))
    print(discovered)

    to_return = []

    for item in discovered:
        temp = []
        for i in range(len(item)):
            if item[i] == '1':
                temp.append(set_A[i])
        to_return.append(temp)
    return tuple(to_return)
    # return set(discovered)


if __name__ == "__main__":
    print(subset_sum([4, -4, 1]))
