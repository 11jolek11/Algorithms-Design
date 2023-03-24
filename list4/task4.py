import timeit
import random



def profile(target: function, data_size: int, data_form: str):
    if data_form is "matrix":
        # data = np.random.rand(data_size, data_size).tolist()
        data_a = [
            [random.randint(0, 10) for _ in range(data_size)] for _ in range(data_size)
        ]
        data_b = [
            [random.randint(0, 10) for _ in range(data_size)] for _ in range(data_size)
        ]

        start_time = timeit.default_timer()
        function(data_a, data_b)
        captured = timeit.default_timer() - start_time
        return captured
    elif data_form is "list":
        data = [random.randint(0, 10) for _ in range(data_size)]
        start_time = timeit.default_timer()
        function(data)
        captured = timeit.default_timer() - start_time
        return captured
