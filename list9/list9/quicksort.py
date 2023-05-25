from robots import Table, Robot


def partition(arr, low, high):
    """
    Hoare's partition
    """
    pivot = getattr(arr[low], "price")
    i = low - 1
    j = high + 1
    while (True):

        # Najbardziej po lewej >= pivot
        i += 1
        while (getattr(arr[i], "price") < pivot):
            i += 1
        # Najbardziej po prawej <= pivot
        j -= 1
        while (getattr(arr[j], "price") > pivot):
            j -= 1
        # Zetkniecie pointerow
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
        ''' pi is partitioning index, arr[p] OK'''
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)

def quicksort_wrapper(arr: list[Robot]):
    quickSort(arr, 0, len(arr)-1)


if __name__ == '__main__':
    t = Table()
    t.fill(5)
    t.show()
    # quickSort(t.frame, 0, 4)
    quicksort_wrapper(t.frame)
    t.show()
