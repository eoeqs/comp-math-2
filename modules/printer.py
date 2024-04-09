import numpy as np
from tabulate import tabulate


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_matrix(matrix):
    print(f"{Colors.HEADER}Matrix:{Colors.END}")
    print(tabulate(matrix))


def print_results(matrix, a, x_current, x_previous, k):
    print("****************************************")
    print(f"{Colors.GREEN}Final results:{Colors.END}")

    print(f"{Colors.BOLD}Accuracy:{Colors.END} %.10f" % a)

    base_print(matrix, x_current, x_previous, k)


def print_intermediate_results(matrix, x_current, x_previous, k):
    print("****************************************")
    print(f"{Colors.CYAN}Intermediate results:{Colors.END}")

    base_print(matrix, x_current, x_previous, k)


def base_print(matrix, x_current, x_previous, k):
    print(f"{Colors.BOLD}Resulting vectors of variables:{Colors.END}")
    for number in x_current:
        print(np.around(number, 10), end="\t")
    print()

    print(f"{Colors.BOLD}Number of iterations:{Colors.END} %d" % k)
    print_inaccuracy(matrix, x_current, x_previous)


def print_inaccuracy(matrix, x_current, x_previous):
    print(f"{Colors.BOLD}Vector of inaccuracies:{Colors.END}", end=' ')
    print(np.array(x_current) - np.array(x_previous), end=' ')
    print()
