import timeit
import random
import matplotlib.pyplot as plt

from fft_multiply import poly_multiply
# from naive_multiply_ll import multiply_from_list
from naive_multiply import multiply



def profile(target, data_size: int, data_form: str):
        poly1 = [random.randint(1, 1000) for _ in range(data_size)]
        poly2 = [random.randint(1, 1000) for _ in range(data_size)]
        # print(len(data))
        start_time = timeit.default_timer()
        target(poly1, poly2)
        captured = timeit.default_timer() - start_time
        return captured


def visualize(func: list, tags: list[str], plot_path: str, a: int, b: int, step=1, data_form='list'):
    results_a = []
    results_b = []
    axis_tickets = []
    for n in range(a, b, step):
        axis_tickets.append(n)

        results_a.append(profile(func[0], n, data_form=data_form))
        results_b.append(profile(func[1], n, data_form=data_form))
    # plt.plot(axis_tickets, results)
    plt.scatter(axis_tickets, results_a, label=tags[0])
    # plt.scatter(axis_tickets, results_b, label=tags[1])
    plt.legend()
    plt.show()
    # plt.savefig(plot_path)


if __name__ == "__main__":
    visualize([multiply, poly_multiply], ['naive', 'fft'], "task4_scatter.png", 1, 256*2)
