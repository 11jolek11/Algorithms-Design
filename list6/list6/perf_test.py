import timeit
import matplotlib.pyplot as plt

from NWD import ENWD, RNWD, gcd_prime_factorization


def profile(target, n, m: int):
    # if not callable(target):
    #     raise Exception("Not a function!")
    
    q_series = [i for i in range(1, m)]
    times = []
    for q in q_series:
        start_time = timeit.default_timer()
        target(n, q)
        times.append(timeit.default_timer() - start_time)
    return times


# def visualize(func, n, b: int):
#     results = []
#     axis_tickets = list(range(1, b))
#     results.append(profile(func, n, b))
#     # plt.plot(axis_tickets, results)
#     plt.scatter(axis_tickets, results)
#     plt.savefig('task5_sctter.png')


def visualize(n, b: int):
    results1 = []
    results2 = []
    axis_tickets = list(range(1, b))
    results1.append(profile(RNWD, n, b))
    results2.append(profile(ENWD, n, b))
    # plt.plot(axis_tickets, results)
    plt.scatter(axis_tickets, results1)
    plt.scatter(axis_tickets, results2, color="tab:orange")
    plt.savefig('task5_sctter.png')


if __name__ == '__main__':
    # visualize(RNWD, 10, 100)
    visualize(10, 100)


    # print(gcd_prime_factorization(56, 0))

    # for i in range(10):
        # print(gcd_prime_factorization(56, i))
