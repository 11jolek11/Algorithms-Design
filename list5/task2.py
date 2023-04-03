def wrapper_max(a, n):
    if n == 1:
        return a[0]
    x = wrapper_max(a[n//2:], n - n//2)
    return x if x > a[0] else a[0]
def maximum(a):
    return wrapper_max(a, len(a))


def average(a):
    n = len(a)
    if n == 1:
        return a[0]
    else:
        mid = n // 2
        return (mid * average(a[:mid]) + (n - mid) * average(a[mid:])) / n


def fsbig(num, n: int, first: float|int, second: float|int):
    if n < 2:
        print(f'Second: {second}')
    else:
        if num[n] > first:
            second = first
            first = num[n]
        elif num[n] > second and num[n] != first:
            second = num[n]

        n -= 1

        fsbig(num, n , first, second)


if __name__ == "__main__":
    p = [2, 2, 1, 7, 7, 4, 3]
    # print(findsecondlargest(p, 0, 5, 2))
    fsbig(p, len(p)-1, max(p[:2]), min(p[:2]))
