def max_heapify(robots: list, i):
    left = i*2
    right = i*2 + 1 

    if left <= len(robots) and getattr(robots[left], "price") > getattr(robots[i], "price"):
        largest = left
    else:
        largest = i
    if right <= len(robots) and getattr(robots[right], "price") > getattr(robots[largest], "price"):
        largest = right
    if largest != i:
        temp = robots[i]
        robots[i] = robots[largest]
        robots[largest] = temp
        del temp
        max_heapify(robots, largest)

def build_max_heap(robots: list):
    n = len(robots)

    for i in range(0, len(robots//2 - 1), -1):
        max_heapify(robots, i)
