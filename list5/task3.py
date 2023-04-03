def mergesort(table):
    """
    Custom merge sort implementation in python
    """
    if len(table) > 1:

        #  split_point punkt rozbicia tabeli
        split_point = len(table)//2
        L = table[:split_point]
        R = table[split_point:]

        # Odpalam rekurencje na obu polowach
        mergesort(L)
        mergesort(R)

        i = 0
        j = 0
        k = 0

        # Sortowanie wewnatrz
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                table[k] = L[i]
                i += 1
            else:
                table[k] = R[j]
                j += 1
            k += 1

        # po przejsciu tabel
        while i < len(L):
            table[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            table[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    table = [6, 5, 12, 10, 9, 1]

    mergesort(table)
    print(table)
