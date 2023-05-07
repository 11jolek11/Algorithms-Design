from task4 import profile
from task1 import *
from task2 import matrix_multi
from task3 import subset_sum

import matplotlib.pyplot as plt



def visualize(func, a: int, b: int, step=1, data_form='list'):
    results = []
    axis_tickets = []
    for n in range(a, b, step):
        axis_tickets.append(n)
        results.append(profile(func, n, data_form=data_form))
    # plt.plot(axis_tickets, results)
    plt.scatter(axis_tickets, results)
    plt.savefig('task5_sctter.png')


if __name__ == "__main__":
    # visualize(biggest_element, 1, 10000)
    visualize(subset_sum, 1, 20)