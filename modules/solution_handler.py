from modules.getter import *
from modules.solver import *


def solve_handler_single_equation(equation_choice, lower_limit, upper_limit, epsilon, method_choice):
    equation_func = get_equation_function(equation_choice)

    if method_choice == 'bisection':
        result = bisection_method(equation_func, lower_limit, upper_limit, epsilon)
        return f"Root found at x = {result} "
    elif method_choice == 'secant':
        result, iterations = secant_method(equation_func, lower_limit, upper_limit, epsilon)
        if result is not None:
            return f"Root found at x = {result} after {iterations} iterations using Secant Method"
        else:
            return "Error: Maximum number of iterations reached for Secant Method"
    elif method_choice == 'simple_iteration':
        result, iterations = simple_iteration_method(equation_func, lower_limit, upper_limit, epsilon)
        if result is not None:
            return f"Root found at x = {result} after {iterations} iterations using Simple Iteration Method"
        else:
            return "Error: Maximum number of iterations reached for Simple Iteration Method"
    else:
        return "Error: Invalid method choice for solving."


def solve_handler_system_equations(system_equation_choice, initial_guess_x, initial_guess_y, epsilon):
    system_equation_func = get_system_equation_function(system_equation_choice)
    print("System equation function:", system_equation_func)
    (root_x, root_y), iterations, errors = system_newton_method(system_equation_func[0], system_equation_func[1],
                                                                initial_guess_x, initial_guess_y, epsilon)
    print("System solution result:", (root_x, root_y), iterations, errors)
    result = f"Root: ({root_x}, {root_y}), Iterations: {iterations}"
    return result
