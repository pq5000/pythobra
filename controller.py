class EquationController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.solve_button.clicked.connect(self.handle_solve)

    def handle_solve(self):
        eq_text = self.view.get_equation_text()

        if not eq_text:
            self.view.show_error("Skriv en ligning")
            return

        success = self.model.set_equation(eq_text)
        if not success:
            self.view.show_error("Kunne ikke forstå")
            return

        solutions = self.model.solve_equation()
        self.view.set_solutions(solutions)

        x_data, y_data = self.model.get_plot_data()
        self.view.plot_equation(x_data, y_data)
