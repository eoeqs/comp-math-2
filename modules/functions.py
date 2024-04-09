def f1(x, y):
    return x ** 2 + y ** 2 - 4


def f2(x, y):
    return x + y - 2


def derivative_equation1(x):
    return 8.22 * x ** 2 - 3.86 * x - 15.28


def derivative_equation2(x):
    return 3 * x ** 2 + 4.56 * x - 1.934


def derivative_equation3(x):
    return 13.35 * x ** 2 + 15.62 * x - 9.62


equations = {
    1: r"2.74x^{3} - 1.93x^{2} - 15.28x - 3.72",
    2: r"x^{3} + 2.28x^{2} - 1.934x - 3.907",
    3: r"4.45x^{3} + 7.81x^{2} - 9.62x - 8.17",
}


def equation1(x):
    return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72


def equation2(x):
    return x ** 3 + 2.28 * x ** 2 - 1.934 * x - 3.907


def equation3(x):
    return 4.45 * x ** 3 + 7.81 * x ** 2 - 9.62 * x - 8.17
