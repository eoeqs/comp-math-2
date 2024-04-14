import math
import sympy as sp


def derivative_equation1(x):
    return 8.22 * x ** 2 - 3.86 * x - 15.28


def derivative_equation2(x):
    return 3 * x ** 2 + 4.56 * x - 1.934


def derivative_equation3(x):
    return 1 - 10 * math.cos(x)


equations = {
    1: r"2.74x^{3} - 1.93x^{2} - 15.28x - 3.72",
    2: r"x^{3} + 2.28x^{2} - 1.934x - 3.907",
    3: r"x - 10\sin(x)"
}


def equation1(x):
    return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72


def equation2(x):
    return x ** 3 + 2.28 * x ** 2 - 1.934 * x - 3.907


def equation3(x):
    return x - 10 * sp.sin(x)


equation_latex_1 = sp.latex(sp.sympify(equation1(sp.symbols('x'))))
equation_latex_2 = sp.latex(sp.sympify(equation2(sp.symbols('x'))))
equation_latex_3 = sp.latex(sp.sympify(equation3(sp.symbols('x'))))

equations_latex = {
    1: equation_latex_1,
    2: equation_latex_2,
    3: equation_latex_3,
}
