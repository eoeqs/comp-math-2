import math


def bisection_method(equation_func, lower_limit, upper_limit, epsilon):
    roots = []
    iterations = 0
    f_x0 = equation_func(lower_limit)
    f_x1 = equation_func(upper_limit)
    num_roots_on_interval = count_roots_on_interval(equation_func, min(lower_limit, upper_limit),
                                                    max(lower_limit, upper_limit))
    print(num_roots_on_interval)
    if num_roots_on_interval == 0:
        return "No root found in the given interval.", iterations, None
    elif f_x0 == 0:
        return [lower_limit], iterations, [f_x0]
    elif f_x1 == 0:
        return [upper_limit], iterations, [f_x1]

    while iterations < 1000:
        iterations += 1
        x = (lower_limit + upper_limit) / 2
        print(x)
        if equation_func(x) == 0:
            roots.append(x)
            break
        elif equation_func(x) * equation_func(lower_limit) < 0:
            upper_limit = x
        else:
            lower_limit = x
        if abs(upper_limit - lower_limit) < epsilon or abs(equation_func(x)) < epsilon:
            roots.append(x)
            break

    if num_roots_on_interval > 1:
        return "Multiple roots found in the given interval.", iterations, None
    elif len(roots) == 1:
        return roots, iterations, [equation_func(root) for root in roots]
    else:
        return "No root found in the given interval.", iterations, None


def secant_method(equation_func, lower_limit, upper_limit, epsilon, max_iterations=1000):
    roots = []
    iterations = 0
    f_x0 = equation_func(lower_limit)
    f_x1 = equation_func(upper_limit)
    num_roots_on_interval = count_roots_on_interval(equation_func, min(lower_limit, upper_limit),
                                                    max(lower_limit, upper_limit))
    if num_roots_on_interval == 0:
        return "No root found in the given interval.", iterations, None
    elif f_x0 == 0:
        return [lower_limit], iterations, [f_x0]
    elif f_x1 == 0:
        return [upper_limit], iterations, [f_x1]

    while iterations < max_iterations:
        x2 = upper_limit - (upper_limit - lower_limit) * f_x1 / (f_x1 - f_x0)
        iterations += 1
        f_x2 = equation_func(x2)

        if abs(f_x2) < epsilon:
            roots.append(x2)
            break

        lower_limit, upper_limit = upper_limit, x2
        f_x0, f_x1 = f_x1, f_x2

    if num_roots_on_interval > 1:
        return "Multiple roots found in the given interval.", iterations, None
    elif len(roots) == 1:
        return roots, iterations, [equation_func(root) for root in roots]
    else:
        return "No root found in the given interval.", iterations, None


def simple_iteration_method(equation_func, lower_limit, upper_limit, epsilon, derivative_func, max_iterations=1000):
    try:
        roots = []
        iterations = 0
        f_x0 = equation_func(lower_limit)
        f_x1 = equation_func(upper_limit)
        num_roots_on_interval = count_roots_on_interval(equation_func, min(lower_limit, upper_limit),
                                                        max(lower_limit, upper_limit))
        if num_roots_on_interval == 0:
            return "No root found in the given interval.", iterations, None
        elif f_x0 == 0:
            return [lower_limit], iterations, [f_x0]
        elif f_x1 == 0:
            return [upper_limit], iterations, [f_x1]

        if derivative_func(lower_limit) * derivative_func(upper_limit) > 0:
            lambda_value = -1 / max(abs(derivative_func(lower_limit)), abs(derivative_func(upper_limit)))
        else:
            lambda_value = 1 / max(abs(derivative_func(lower_limit)), abs(derivative_func(upper_limit)))

        x0 = (lower_limit + upper_limit) / 2

        while iterations < max_iterations:
            iterations += 1
            x1 = x0 + lambda_value * equation_func(x0)
            derivative_x = abs(1 + lambda_value * derivative_func(x0))
            q = derivative_x

            if not math.isnan(q) and q >= 1:
                return "Insufficient convergence condition. Try a different initial guess or function.", None, None

            if abs(x1 - x0) < epsilon:
                roots.append(x1)
                break

            x0 = x1

        if num_roots_on_interval > 1:
            return "Multiple roots found in the given interval.", iterations, None
        elif len(roots) == 1:
            return roots, iterations, [equation_func(root) for root in roots]
        else:
            return "No root found in the given interval.", iterations, None
    except OverflowError:
        return None, None, "Error: Non-convergence or too many iterations required."


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

        x_prev, y_prev = x, y
        x += delta_x
        y += delta_y

        error = max(abs(delta_x), abs(delta_y))
        errors.append(error)
        if error < epsilon:
            if abs(f1(x, y)) < epsilon and abs(f2(x, y)) < epsilon:
                return (x, y), iterations, errors, True
            else:
                return (x, y), iterations, errors, False

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


def count_roots_on_interval(equation_func, lower_limit, upper_limit, num_points=1000):
    num_roots = 0
    step = (upper_limit - lower_limit) / num_points
    x_values = [lower_limit + i * step for i in range(num_points)]
    for i in range(len(x_values) - 1):
        if equation_func(x_values[i]) * equation_func(x_values[i + 1]) <= 0:
            num_roots += 1
    return num_roots
