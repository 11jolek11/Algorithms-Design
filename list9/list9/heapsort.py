from robots import Table, Robot


def heapify(arr: list[Robot], n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and getattr(arr[i], "price") < getattr(arr[left], "price"):
        largest = left

    if right < n and getattr(arr[largest], "price") < getattr(arr[right], "price"):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# def heapSort(table: Table):
#     arr = table.frame

def heapSort(arr: list[Robot]):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':
    t = Table()
    t.fill(5)
    t.show()
    heapSort(t.frame)
    t.show()
