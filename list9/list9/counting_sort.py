from robots import Table, Robot


def counting_sort(arr, max_value):
    count = [0] * (max_value + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num] - 1] = num
        count[num] -= 1

    return output


def counting_sort_robot(arr, max_value=100):
    count = [0] * (max_value + 1)
    output = [0] * len(arr)

    for num in range(len(arr)):
        count[getattr(arr[num], "robot_range")] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[getattr(arr[i], "robot_range")] - 1] = num
        count[getattr(arr[i], "robot_range")] -= 1

    return output

if __name__ == "__main__":
    # arr = [4, 2, 2, 8, 3, 3, 1]
    # sorted_arr = counting_sort(arr, 8)
    # print(sorted_arr)

    t = Table()
    t.fill(5)
    t.show()
    t.frame = counting_sort_robot(t.frame)
    t.show()
