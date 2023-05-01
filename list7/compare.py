import timeit
import random
import matplotlib.pyplot as plt

from fft_multiply import poly_multiply
from naive_multiply_ll import multiply



def profile(target, data_size: int, data_form: str):
        data = [random.randint(0, 1000) for _ in range(data_size)]
        # print(len(data))
        start_time = timeit.default_timer()
        target(data)
        captured = timeit.default_timer() - start_time
        return captured


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
   visualize(mergesort, 1, 20)