# TODO: Add checking dimensions
def matrix_multi(matrix_a: list[list], matrix_b: list[list]) -> list[list[float]]:
    # matrix_result =[[0.0, 0.0], [0.0, 0.0]]
    matrix_result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]
    for y in range(len(matrix_a)):
        for x in range(len(matrix_a)):
            for k in range(len(matrix_a[0])):
                matrix_result[y][x] += float(matrix_a[y][k]*matrix_b[k][x])
    return matrix_result


if __name__ == "__main__":
    a = [[1, 1], [1, 1]]
    b = a

    print(matrix_multi(a, b))
# Strassen algorithm
# https://vaibhaw-vipul.medium.com/matrix-multiplication-optimizing-the-code-from-6-hours-to-1-sec-70889d33dcfa
# https://coffeebeforearch.github.io/2020/06/23/mmul.html
