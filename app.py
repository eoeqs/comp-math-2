from flask import Flask, render_template, request, jsonify
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
        lower_limit = float(request.form.get('lower_limit'))
        upper_limit = float(request.form.get('upper_limit'))
        epsilon = float(request.form.get('epsilon'))
        method_choice = request.form.get('method_choice')

        equation_func = get_equation_function(equation_choice)

        equation_latex = equations[equation_choice]
        desmos_data = {
            'equation_latex': equation_latex,
            'lower_limit': lower_limit,
            'upper_limit': upper_limit
        }

        result = solve_handler_single_equation(equation_choice, lower_limit, upper_limit, epsilon, method_choice)
        if result.startswith("Error"):
            return render_template('index.html', equations=equations, error_message=result)
        else:
            error_message = "Select an equation or system to display the graph."
            return render_template('index.html', equations=equations, error_message=error_message, result=result)

    elif equation_type == 'system':
        pass

    else:
        return render_template('index.html', equations=equations, error_message="Invalid equation type")


if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True)
