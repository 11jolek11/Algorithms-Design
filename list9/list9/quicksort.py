from robots import Table, Robot


def partition(arr, low, high):
    """
    Hoare's partition
    """
    pivot = getattr(arr[low], "price")
    i = low - 1
    j = high + 1
    while (True):
        # Find leftmost element greater than
        # or equal to pivot
        i += 1
        while (getattr(arr[i], "price") < pivot):
            i += 1
        # Find rightmost element smaller than
        # or equal to pivot
        j -= 1
        while (getattr(arr[j], "price") > pivot):
            j -= 1
        # If two pointers met.
        if (i >= j):
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr: list[Robot], low, high):
    # print(type(table))
    # arr = table.frame
    '''QuickSort
    arr --> Array to be sorted,
    low --> Starting index,
    high --> Ending index '''
    if (low < high):
        ''' pi is partitioning index, arr[p] is now
        at right place '''
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    t = Table()
    t.fill(5)
    t.show()
    quickSort(t.frame, 0, 4)
    t.show()
