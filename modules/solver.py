import math


def bisection_method(equation_func, lower_limit, upper_limit, epsilon):
    roots = []
    iterations = 0
    if equation_func(lower_limit) * equation_func(upper_limit) > 0:
        return "No root found in the given interval.", iterations, None

    while abs(upper_limit - lower_limit) > epsilon:
        iterations += 1
        mid = (lower_limit + upper_limit) / 2
        if equation_func(mid) == 0:
            roots.append(mid)
            break
        elif equation_func(mid) * equation_func(lower_limit) < 0:
            upper_limit = mid
        else:
            lower_limit = mid

    if roots:
        return roots, iterations, [equation_func(root) for root in roots]
    else:
        return "Multiple roots found in the given interval.", iterations, None


def secant_method(equation_func, x0, x1, epsilon, max_iterations=1000):
    roots = []
    iterations = 0
    while iterations < max_iterations:
        x2 = x1 - (equation_func(x1) * (x1 - x0)) / (equation_func(x1) - equation_func(x0))
        iterations += 1
        if abs(x2 - x1) < epsilon:
            roots.append(x2)
            break
        x0, x1 = x1, x2
    if roots:
        return roots, iterations, [equation_func(root) for root in roots]
    else:
        return "Multiple roots found in the given interval.", iterations, None


def simple_iteration_method(equation_func, lower_limit, upper_limit, epsilon, max_iterations=1000):
    roots = []
    iterations = 0
    if equation_func(lower_limit) * equation_func(upper_limit) > 0:
        return "No root found in the given interval.", None, None

    x0 = (lower_limit + upper_limit) / 2

    while iterations < max_iterations:
        iterations += 1
        x1 = equation_func(x0)
        derivative_x = abs((equation_func(x1) - equation_func(x0)) / (x1 - x0))
        q = derivative_x

        if not math.isnan(q) and q >= 1:
            return "Insufficient convergence condition. Try a different initial guess or function.", None, None

        if abs(x1 - x0) < epsilon:
            roots.append(x1)
            break

        x0 = x1

    if roots:
        return roots, iterations, [equation_func(root) for root in roots]
    else:
        return "Multiple roots found in the given interval.", iterations, None


def system_newton_method(f1, f2, x0, y0, epsilon, max_iterations=1000):
    x = x0
    y = y0
    iterations = 0
    errors = []

    while iterations < max_iterations:
        iterations += 1
        f1_val = f1(x, y)
        f2_val = f2(x, y)
        jacobian = calculate_jacobian(f1, f2, x, y)

        delta_x, delta_y = solve_linear_system(jacobian, [-f1_val, -f2_val])

        x += delta_x
        y += delta_y

        error = max(abs(delta_x), abs(delta_y))
        errors.append(error)

        if error < epsilon:
            break

    return (x, y), iterations, errors


def calculate_jacobian(f1, f2, x, y, h=1e-6):
    jacobian = [[0, 0], [0, 0]]

    jacobian[0][0] = (f1(x + h, y) - f1(x, y)) / h
    jacobian[0][1] = (f1(x, y + h) - f1(x, y)) / h

    jacobian[1][0] = (f2(x + h, y) - f2(x, y)) / h
    jacobian[1][1] = (f2(x, y + h) - f2(x, y)) / h

    return jacobian


def solve_linear_system(matrix, vector):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det != 0:
        inv_det = 1 / det
        x = (matrix[1][1] * vector[0] - matrix[0][1] * vector[1]) * inv_det
        y = (matrix[0][0] * vector[1] - matrix[1][0] * vector[0]) * inv_det
        return x, y
    else:
        return None, None
