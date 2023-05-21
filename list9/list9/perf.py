import timeit
import random
import matplotlib.pyplot as plt
from radix_sort import radix_sort
from quicksort import quickSort, quicksort_wrapper
from counting_sort import counting_sort_robot
from heapsort import heapSort
from robots import Table, Robot


def profile(target, data_size: int, data_form: str, table_gen: Table):
    if data_form == "matrix":
        data_a = [
            [random.randint(0, 15) for _ in range(data_size)] for _ in range(data_size)
        ]

        start_time = timeit.default_timer()
        target(data_a)
        captured = timeit.default_timer() - start_time
        return captured
    elif data_form == "list":
        # data = [random.randint(0, 1000) for _ in range(data_size)]
        # print(len(data))
        table_gen.frame = []
        table_gen.fill(data_size)
        start_time = timeit.default_timer()
        target(table_gen.frame)
        captured = timeit.default_timer() - start_time
        return captured


# def visualize(func: list, a: int, b: int, step=1, data_form='list'):
#     table = Table()
#     results = []
#     axis_tickets = []
#     for item in func:
#         for n in range(a, b, step):
#             axis_tickets.append(n)
#             results.append(profile(item, n, data_form=data_form, table_gen=table))
#     # plt.plot(axis_tickets, results)
#     plt.scatter(axis_tickets, results)
#     plt.show()
    # plt.savefig('task5_sctter.png')


if __name__ == "__main__":
    results = {
        'radix_sort': [],
        'heapSort': [],
        'quickSort': [],
        'counting_sort_robot': []
    }

    table = Table()

    axis_tick = []

    for n in range(1, 300):
        axis_tick.append(n)
        results['quickSort'].append(profile(quicksort_wrapper, n, data_form="list", table_gen=table))
        results['counting_sort_robot'].append(profile(counting_sort_robot, n, data_form="list", table_gen=table))
        results['heapSort'].append(profile(heapSort, n, data_form="list", table_gen=table))
        results['radix_sort'].append(profile(radix_sort, n, data_form="matrix", table_gen=table))
    
    plt.scatter(axis_tick, results['quickSort'], label='quickSort', c="tab:orange")
    plt.scatter(axis_tick, results['counting_sort_robot'], label='counting_sort_robot', c="tab:blue")
    plt.scatter(axis_tick, results['heapSort'], label='heapSort', c="tab:red")
    plt.scatter(axis_tick, results['radix_sort'], label='radix_sort', c="tab:green")
    plt.legend()
    plt.show()



#    visualize(counting_sort_robot, 1, 1000)
# counting_sort_robot
