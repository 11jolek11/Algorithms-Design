from hash_dict import HashTable
from binary import binary_search
from linear import linear_search
from data.robots import Table, Robot
import matplotlib.pyplot as plt
import timeit
import random


# times_linear = {}
# times_binary = {}
# times_hash = {}

# def measure(n, max_iters=10):
#     if n < 1:
#         raise ValueError("n too small!")
#     tab = Table()
#     tab.fill(n)
#     search_for_price = [float(random.randint(1, len(tab.frame))) for _ in range(max_iters)]

#     h = HashTable(max_size=len(tab.frame), alpha=0.5)

#     for i in range(len(tab.frame)):
#         tab.frame[i].price = float(i) + 1.0

#     for robot in tab.frame:
#         h.insert_item(robot, "price")

#     for s in search_for_price:
#         linear_search_keys = [None, [s], None, None]
#         start_time = timeit.default_timer()
#         linear_search(tab.frame, linear_search_keys)
#         captured = timeit.default_timer() - start_time
#         times_linear[str(n)] = captured/max_iters

#         start_time = timeit.default_timer()
#         binary_search(tab.frame, s, "price", 0, len(tab.frame)-1)
#         captured = timeit.default_timer() - start_time
#         times_binary[str(n)] = captured/max_iters

#         start_time = timeit.default_timer()
#         h.search_item(s, "price")
#         captured = timeit.default_timer() - start_time
#         times_hash[str(n)] = captured/max_iters


# if __name__ == '__main__':
#     x = []
#     for i in range(1, 100):
#         x.append(i)
#         measure(i)

#     plt.scatter(x, times_linear.values(), c="tab:orange")
#     plt.scatter(x, times_binary.values())
#     plt.scatter(x, times_hash.values(), c="tab:red")

#     plt.savefig("z5.png")


# times_linear = {}
# times_binary = {}
# times_hash = {}


# def measure(n, max_iters=1):
#     if n < 1:
#         raise ValueError("n too small!")
#     tab = Table()
#     tab.fill(n)
#     search_for_price = [float(random.randint(1, len(tab.frame))) for _ in range(max_iters)]

#     h = HashTable(max_size=len(tab.frame), alpha=0.5)

#     for i in range(len(tab.frame)):
#         tab.frame[i].price = float(i) + 1.0

#     for robot in tab.frame:
#         h.insert_item(robot, "price")

#     for s in search_for_price:
#         linear_search_keys = [None, [s], None, None]
#         start_time = timeit.default_timer()
#         linear_search(tab.frame, linear_search_keys)
#         captured = timeit.default_timer() - start_time
#         times_linear[str(n)] += captured/max_iters

#         start_time = timeit.default_timer()
#         binary_search(tab.frame, s, "price", 0, len(tab.frame)-1)
#         captured = timeit.default_timer() - start_time
#         times_binary[str(n)] += captured/max_iters

#         start_time = timeit.default_timer()
#         h.search_item(s, "price")
#         captured = timeit.default_timer() - start_time
#         times_hash[str(n)] += captured/max_iters
#         print("1")


# if __name__ == '__main__':
#     measure(20)
#     print(times_linear)
from statistics import mean


def measure(n, max_iters=1):
    times_linear = []
    times_binary = []
    times_hash = []

    if n < 1:
        raise ValueError("n too small!")
    tab = Table()
    tab.fill(n)
    # search_for_price = [float(random.randint(1, len(tab.frame))) for _ in range(max_iters)]
    search_for_price = []

    # im większa alpha tym szybszy czas wykonania
    h = HashTable(max_size=len(tab.frame), alpha=0.5)

    for i in range(len(tab.frame)):
        tab.frame[i].price = float(i) + 3.0
        search_for_price.append(float(i) + 3.0)

    for robot in tab.frame:
        h.insert_item(robot, "price")

    for s in search_for_price:
        linear_search_keys = [None, [s], None, None]
        start_time = timeit.default_timer()
        linear_search(tab.frame, linear_search_keys)
        captured = timeit.default_timer() - start_time
        # times_linear[str(n)] += captured/max_iters
        times_linear.append(captured)

    # FIXME:
    for s in search_for_price:
        start_time = timeit.default_timer()
        binary_search(tab.frame, s, "price", 0, len(tab.frame)-1)
        captured = timeit.default_timer() - start_time
        # times_binary[str(n)] += captured/max_iters
        times_binary.append(captured)

    for s in search_for_price:
        start_time = timeit.default_timer()
        h.search_item(s, "price")
        captured = timeit.default_timer() - start_time
        # times_hash[str(n)] += captured/max_iters
        times_hash.append(captured)
    return mean(times_linear), mean(times_binary), mean(times_hash)
    # return mean(times_binary)


if __name__ == '__main__':
    # linear binary hash
    linear = []
    binary = []
    hash = []
    labels = []
    # print(measure(200))
    for i in range(1, 800):
        labels.append(i)
        temp = measure(i)
        linear.append(temp[0])
        binary.append(temp[1])
        hash.append(temp[2])

    plt.scatter(labels, linear)
    plt.scatter(labels, binary, c="tab:orange")
    plt.scatter(labels, hash, c="tab:green")
    plt.show()
