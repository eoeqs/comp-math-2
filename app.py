import os
from flask import Flask, render_template, request, jsonify
from matplotlib import pyplot as plt
import numpy as np
from modules.solution_handler import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', equations=equations)


@app.route('/solve', methods=['POST'])
def solve():
    equation_type = request.form['equation_type']

    if equation_type == 'single':
        equation_choice = int(request.form['equation'])
        lower_limit = float(request.form['lower_limit'])
        upper_limit = float(request.form['upper_limit'])
        epsilon = float(request.form['epsilon'])
        method_choice = request.form['method_choice']

        result = solve_handler_single_equation(equation_choice, lower_limit, upper_limit, epsilon, method_choice)
        if result.startswith("Error"):
            return render_template('index.html', equations=equations, error_message=result)
        else:
            return render_template('index.html', equations=equations, result=result)

    elif equation_type == 'system':
        system_equation_choice = request.form['system_equation']
        initial_guess_x = float(request.form['system_initial_guess_x'])
        initial_guess_y = float(request.form['system_initial_guess_y'])
        epsilon = float(request.form['epsilon'])

        result = solve_handler_system_equations(system_equation_choice, initial_guess_x, initial_guess_y, epsilon)
        if result.startswith("Error"):
            return render_template('index.html', equations=equations, error_message=result)
        else:
            return render_template('index.html', equations=equations, result=result)

    else:
        return render_template('index.html', equations=equations, error_message="Invalid equation type")


@app.route('/plot', methods=['POST'])
def plot():
    equation_type = request.form['equation_type']

    if equation_type == 'single':
        equation_choice = int(request.form['equation'])
        lower_limit = float(request.form['lower_limit'])
        upper_limit = float(request.form['upper_limit'])

        equation_func = get_equation_function(equation_choice)

        x_values = np.linspace(lower_limit - 1, upper_limit + 1, 1000)
        y_values = equation_func(x_values)

        plt.plot(x_values, y_values)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the Function')
        plt.grid(True)

        plot_path = 'static/plot.png'
        plt.savefig(plot_path)

        plt.close()

        return plot_path

    elif equation_type == 'system':
        system_equation_choice = request.form['system_equation']
        initial_guess_x = float(request.form['system_initial_guess_x'])
        initial_guess_y = float(request.form['system_initial_guess_y'])
        epsilon = float(request.form['epsilon'])

        equation_func_x, equation_func_y = get_system_equation_function(system_equation_choice)

        x_values = np.linspace(initial_guess_x - 1, initial_guess_x + 1, 1000)
        y_values_1 = equation_func_x(x_values, initial_guess_y)
        y_values_2 = equation_func_y(x_values, initial_guess_y)

        plt.plot(x_values, y_values_1, label='Equation 1')
        plt.plot(x_values, y_values_2, label='Equation 2')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the System of Equations')
        plt.grid(True)
        plt.legend()

        plot_path = 'static/plot.png'
        plt.savefig(plot_path)

        plt.close()

        return plot_path


if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True)
