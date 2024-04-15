from modules.getter import *
from modules.solver import *


def solve_handler_single_equation(equation_choice, lower_limit, upper_limit, epsilon, method_choice):
    equation_func = get_equation_function(equation_choice)
    derivative_func = get_derivative_function(equation_choice)
    if method_choice == 'bisection':
        root, iterations, value = bisection_method(equation_func, lower_limit, upper_limit, epsilon)
        if isinstance(root, str) and root == "Multiple roots found in the given interval.":
            return root
        elif isinstance(root, str) and root == "No root found in the given interval.":
            return root
        else:
            return f"Root found at x = {root} after {iterations} iterations using Bisection Method. F({root}) = {value}."
    elif method_choice == 'secant':
        root, iterations, value = secant_method(equation_func, lower_limit, upper_limit, epsilon)
        if isinstance(root, str) and root == "Multiple roots found in the given interval.":
            return root
        elif isinstance(root, str) and root == "No root found in the given interval.":
            return root
        else:
            return f"Root found at x = {root} after {iterations} iterations using Secant Method. F({root}) = {value}."

    elif method_choice == 'simple_iteration':
        root, iterations, value = simple_iteration_method(equation_func, lower_limit, upper_limit, epsilon,
                                                          derivative_func)
        if isinstance(root, str) and root == "Multiple roots found in the given interval.":
            return root
        elif isinstance(root, str) and root == "No root found in the given interval.":
            return root
        elif isinstance(root, str) and root == (
                "Insufficient convergence condition. Try a different initial guess or function."):
            return root
        else:
            return f"Root found at x = {root} after {iterations} iterations using Simple Iteration Method. F({root}) = {value}."

    else:
        return "Error: Invalid method choice for solving."


def solve_handler_system_equations(system_equation_choice, initial_guess_x, initial_guess_y, epsilon):
    system_equation_func = get_system_equation_function(system_equation_choice)
    (root_x, root_y), iterations, errors, success = system_newton_method(system_equation_func[0],
                                                                         system_equation_func[1],
                                                                         initial_guess_x, initial_guess_y, epsilon)

    result = (f"Root: ({root_x}, {root_y}), "
              f"\nIterations: {iterations}, "
              f"\nError vector: {errors}, "
              f"\nCalculated correctly: {success}")
    return result



