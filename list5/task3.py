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

        a = 0
        b = 0
        helper = 0

        # Sortowanie pomiedzy rozlamami
        while a < len(L) and b < len(R):
            if L[a] < R[b]:
                table[helper] = L[a]
                a += 1
            else:
                table[helper] = R[b]
                b += 1
            helper += 1

        # po przejsciu tabel, merge
        while a < len(L):
            table[helper] = L[a]
            a += 1
            helper += 1

        while b < len(R):
            table[helper] = R[b]
            b += 1
            helper += 1


if __name__ == '__main__':
    table = [6, 5, 12, 10, 9, 1]

    mergesort(table)
    print(table)
