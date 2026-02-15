import sympy as sp
import numpy as np

class EquationModel:
    def __init__(self):
        self.x = sp.Symbol('x')
        self.equation = None
        self.solutions = []

    def set_equation(self, eq_string):
        try:
            self.equation = sp.sympify(eq_string)
            return True
        except:
            return False

    def solve_equation(self):
        if self.equation is None:
            return []
        try:
            self.solutions = sp.solve(self.equation, self.x)
            return self.solutions
        except:
            return []

    def get_plot_data(self, x_range=(-10, 10), num_points=500):
        if self.equation is None:
            return None, None

        try:
            func = sp.lambdify(self.x, self.equation, 'numpy')
            x_vals = np.linspace(x_range[0], x_range[1], num_points)
            y_vals = func(x_vals)
            return x_vals, y_vals
        except:
            return None, None
