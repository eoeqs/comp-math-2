from flask import Flask, render_template, request
from modules.solution_handler import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', equations=equations)


@app.route('/solve', methods=['POST'])
def solve():
    equation_type = request.form.get('equation_type')

    if equation_type == 'single':
        equation_choice = int(request.form.get('equation'))
        lower_limit = replace_comma_with_dot(request.form.get('lower_limit'))
        upper_limit = replace_comma_with_dot(request.form.get('upper_limit'))
        epsilon = replace_comma_with_dot(request.form.get('epsilon'))
        method_choice = request.form.get('method_choice')
        data_source = request.form.get('data_source')
        save_to_file = request.form.get('save_to_file')
        if not (equation_choice and method_choice):
            return render_template('index.html', equations=equations, error_message="All fields must be filled")

        if data_source == 'file':
            file_input = request.form.get('file_input')
            if not file_input:
                return render_template('index.html', equations=equations, error_message="Please enter file name")

            if not validate_filename(file_input):
                return render_template('index.html', equations=equations, error_message="File not found")

            try:
                lower_limit, upper_limit, epsilon = input_data_from_file(file_input)
            except ValueError:
                return render_template('index.html', equations=equations, error_message="Invalid input in file.")

        else:
            if not (lower_limit and upper_limit and epsilon):
                return render_template('index.html', equations=equations, error_message="All fields must be filled")

            try:
                lower_limit = float(lower_limit)
                upper_limit = float(upper_limit)
                epsilon = float(epsilon)
            except ValueError:
                return render_template('index.html', equations=equations,
                                       error_message="Invalid input. Please enter valid numbers.")

            valid, message = validate_input_data(lower_limit, upper_limit, epsilon)
            if not valid:
                return render_template('index.html', equations=equations, error_message=message)
        equation_func = get_equation_function(equation_choice)
        derivative_func = get_derivative_function(equation_choice)

        equation_latex = equations[equation_choice]
        desmos_data = {
            'equation_latex': equation_latex,
            'lower_limit': lower_limit,
            'upper_limit': upper_limit
        }

        result = solve_handler_single_equation(equation_choice, lower_limit, upper_limit, epsilon, method_choice)
        if save_to_file and result and not result.startswith("Error"):
            filename = f"result_{equation_choice}_{method_choice}.txt"
            with open(filename, 'w') as file:
                file.write(result)
                message = f"Result has been saved to {filename}"
            return render_template('index.html', equations=equations, message=message)

        if result.startswith("Error"):
            return render_template('index.html', equations=equations, error_message=result)
        else:
            return render_template('index.html', equations=equations, result=result)

    elif equation_type == 'system':
        system_equation_choice = request.form.get('system_equation')
        initial_guess_x = request.form.get('system_initial_guess_x')
        initial_guess_y = request.form.get('system_initial_guess_y')
        epsilon = request.form.get('epsilon_system')
        if not system_equation_choice:
            return render_template('index.html', equations=equations, error_message="Please choose a system equation")

        if not (initial_guess_x and initial_guess_y and epsilon):
            return render_template('index.html', equations=equations, error_message="All fields must be filled")

        try:
            initial_guess_x = float(initial_guess_x)
            initial_guess_y = float(initial_guess_y)
            epsilon = float(epsilon)
        except ValueError:
            return render_template('index.html', equations=equations,
                                   error_message="Invalid input. Please enter valid numbers.")

        valid, message = validate_input_data_system(epsilon)
        if not valid:
            return render_template('index.html', equations=equations, error_message=message)

        system_equation_func = get_system_equation_function(system_equation_choice)
        result = solve_handler_system_equations(system_equation_choice, initial_guess_x, initial_guess_y, epsilon)

        if result.startswith("Error"):
            return render_template('index.html', equations=equations, error_message=result)
        else:
            return render_template('index.html', equations=equations,  result=result)

    else:
        return render_template('index.html', equations=equations, error_message="Invalid equation type")


if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True)
