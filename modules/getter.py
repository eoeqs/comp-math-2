import math

from modules.functions import *
from modules.validator import *


def get_value():
    value = input().strip()
    value = value.replace(',', '.')
    return value


def get_filename(filename=None):
    if filename:
        return filename
    print("Input file name: ")
    filename = get_value()
    while not validate_filename(filename):
        print("Input correct file name: ")
        filename = get_value()
    return filename


def get_one_string_from_file(filename):
    with open(filename, "r") as file:
        a = file.readline()
        return a


def get_choice(choice=None):
    if choice is None:
        choice = input().strip()
    while not validate_choice(choice):
        print("Invalid choice. Please enter a valid choice: ")
        choice = input().strip()

    return choice


def input_data_from_keyboard():
    lower_limit = float(input("Enter the lower limit of the interval: "))
    upper_limit = float(input("Enter the upper limit of the interval: "))
    initial_guess = float(input("Enter the initial approximation to the root: "))
    epsilon = float(input("Enter the calculation error: "))
    return lower_limit, upper_limit, initial_guess, epsilon


def input_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    lower_limit, upper_limit, initial_guess, epsilon = map(float, data)
    return lower_limit, upper_limit, initial_guess, epsilon


def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    lower_limit, upper_limit, initial_guess, epsilon = map(float, data)
    return lower_limit, upper_limit, initial_guess, epsilon


def get_equation_function(choice):
    equations = {
        1: equation1,
        2: equation2,
        3: equation3,
    }
    return equations.get(choice)


# Система 1
def system1_equation1_func_x(x, y):
    return math.sin(x - y) - x * y + 1


def system1_equation1_func_y(x, y):
    return y + math.cos(x - 2)


# Система 2
def system2_equation1_func_x(x, y):
    return math.sin(x + y) - 1.1 * x - 0.1


def system2_equation1_func_y(x, y):
    return x ** 2 + y ** 2 - 1


def get_system_equation_function(system_equation_choice):
    if system_equation_choice == 'system1':
        return system1_equation1_func_x, system1_equation1_func_y
    elif system_equation_choice == 'system2':
        return system2_equation1_func_x, system2_equation1_func_y
    else:
        raise ValueError("Invalid system equation choice")


def get_derivative_function(choice):
    derivatives = {
        1: derivative_equation1,
        2: derivative_equation2,
        3: derivative_equation3,
    }
    return derivatives.get(choice)
