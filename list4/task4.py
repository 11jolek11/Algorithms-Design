import timeit
import random



def profile(target, data_size: int, data_form: str):
    if data_form == "matrix":
        data_a = [
            [random.randint(0, 1000) for _ in range(data_size)] for _ in range(data_size)
        ]
        data_b = [
            [random.randint(0, 1000) for _ in range(data_size)] for _ in range(data_size)
        ]

        start_time = timeit.default_timer()
        target(data_a, data_b)
        captured = timeit.default_timer() - start_time
        return captured
    elif data_form == "list":
        data = [random.randint(0, 1000) for _ in range(data_size)]
        # print(len(data))
        start_time = timeit.default_timer()
        target(data)
        captured = timeit.default_timer() - start_time
        return captured
