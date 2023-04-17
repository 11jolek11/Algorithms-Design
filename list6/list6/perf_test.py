import timeit
import matplotlib.pyplot as plt

from NWD import ENWD, RNWD


def profile(target, n, m: int=10000):
    if not callable(target):
        raise Exception("Not a function!")
    
    q_series = [i for i in range(m)]
    times = []
    for q in q_series:
        start_time = timeit.default_timer()
        target(n, q)
        times.append(timeit.default_timer() - start_time)
    return times


def visualize(func, n, b: int):
    results = []
    axis_tickets = list(range(b))
    results.append(profile(func, n, b))
    # plt.plot(axis_tickets, results)
    plt.scatter(axis_tickets, results)
    plt.savefig('task5_sctter.png')


if __name__ == '__main__':
    visualize(RNWD, 256, 100)
