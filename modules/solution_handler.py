from flask import render_template, request

from modules.getter import *
from modules.solver import *
from modules.validator import validate_input_data


def solve_handler_single_equation(lower_limit, upper_limit, initial_guess, epsilon):
    equation_choice = int(request.form['equation'])
    data_source = request.form['data_source']

    is_valid, error_message = validate_input_data(lower_limit, upper_limit, initial_guess, epsilon)
    if not is_valid:
        return error_message

    equation_func = get_equation_function(equation_choice)
    print("Equation function:", equation_func)

    method_choice = request.form['method_choice']

    if method_choice == 'bisection':
        root_result = bisection_method(equation_func, lower_limit, upper_limit, epsilon)
        print("Bisection method result:", root_result)
        if root_result is None:
            error_message = "Bisection method is not applicable for the specified interval."
            return error_message
        root, iterations = root_result
    elif method_choice == 'secant':
        root, iterations = secant_method(equation_func, lower_limit, upper_limit, epsilon)

    result = f"Root: {root}, Iterations: {iterations}"
    return result


def solve_handler_system_equations(system_equation_choice, initial_guess_x, initial_guess_y, epsilon):
    system_equation_func = get_system_equation_function(system_equation_choice)
    print("System equation function:", system_equation_func)
    (root_x, root_y), iterations, errors = system_newton_method(system_equation_func[0], system_equation_func[1],
                                                                initial_guess_x, initial_guess_y, epsilon)
    print("System solution result:", (root_x, root_y), iterations, errors)
    result = f"Root: ({root_x}, {root_y}), Iterations: {iterations}"
    return result
