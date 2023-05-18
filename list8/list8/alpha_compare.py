from hash_dict import HashTable
from binary import binary_search
from linear import linear_search
from data.robots import Table, Robot
import matplotlib.pyplot as plt
import timeit
import random
from statistics import mean


def measure(n, max_iters=1):
    times_a = []
    times_b = []
    times_c = []

    if n < 1:
        raise ValueError("n too small!")
    tab = Table()
    tab.fill(n)
    # search_for_price = [float(random.randint(1, len(tab.frame))) for _ in range(max_iters)]
    search_for_price = []

    # im większa alpha tym szybszy czas wykonania
    #  a -> alpha 0.25
    #  b -> alpha 0.5
    #  c -> alpha 0.75
    a = HashTable(max_size=len(tab.frame), alpha=0.25)
    b = HashTable(max_size=len(tab.frame), alpha=0.5)
    c = HashTable(max_size=len(tab.frame), alpha=0.75)

    for i in range(len(tab.frame)):
        tab.frame[i].price = float(i) + 3.0
        search_for_price.append(float(i) + 3.0)

    for robot in tab.frame:
        a.insert_item(robot, "price")
        b.insert_item(robot, "price")
        c.insert_item(robot, "price")

    # for s in search_for_price:
    #     linear_search_keys = [None, [s], None, None]
    #     start_time = timeit.default_timer()
    #     linear_search(tab.frame, linear_search_keys)
    #     captured = timeit.default_timer() - start_time
    #     # times_linear[str(n)] += captured/max_iters
    #     times_linear.append(captured)

    # FIXME:
    # for s in search_for_price:
    #     start_time = timeit.default_timer()
    #     binary_search(tab.frame, s, "price", 0, len(tab.frame)-1)
    #     captured = timeit.default_timer() - start_time
    #     # times_binary[str(n)] += captured/max_iters
    #     times_binary.append(captured)

    for s in search_for_price:
        start_time = timeit.default_timer()
        a.search_item(s, "price")
        captured = timeit.default_timer() - start_time
        # times_hash[str(n)] += captured/max_iters
        times_a.append(captured)

    for s in search_for_price:
        start_time = timeit.default_timer()
        b.search_item(s, "price")
        captured = timeit.default_timer() - start_time
        # times_hash[str(n)] += captured/max_iters
        times_b.append(captured)

    for s in search_for_price:
        start_time = timeit.default_timer()
        c.search_item(s, "price")
        captured = timeit.default_timer() - start_time
        # times_hash[str(n)] += captured/max_iters
        times_c.append(captured)
    # return mean(times_binary)
    return mean(times_a), mean(times_b), mean(times_c)


if __name__ == '__main__':
    # linear binary hash
    a = []
    b = []
    c = []
    labels = []
    # print(measure(200))
    for i in range(1, 1200):
        labels.append(i)
        temp = measure(i)
        a.append(temp[0])
        b.append(temp[1])
        c.append(temp[2])

    plt.scatter(labels, a)
    plt.scatter(labels, b, c="tab:orange")
    plt.scatter(labels, c, c="tab:green")
    plt.show()
