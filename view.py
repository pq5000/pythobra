from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class EquationView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pythobra")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        input_layout = QHBoxLayout()
        self.equation_label = QLabel("Ligning: (løses for x):")
        self.equation_input = QLineEdit()
        input_layout.addWidget(self.equation_label)
        input_layout.addWidget(self.equation_input)

        self.solve_button = QPushButton("Løs og plot")

        self.solution_label = QLabel("Løsninger: ")

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        layout.addLayout(input_layout)
        layout.addWidget(self.solve_button)
        layout.addWidget(self.solution_label)
        layout.addWidget(self.canvas)

    def get_equation_text(self):
        return self.equation_input.text()

    def set_solutions(self, solutions):
        if len(solutions) == 0:
            self.solution_label.setText("Kunne ikke finde nogen løsninger!")
        else:
            sol_text = ", ".join([str(s) for s in solutions])
            self.solution_label.setText(f"Løsninger: {sol_text}")

    def plot_equation(self, x_data, y_data):
        self.ax.clear()

        self.ax.plot(x_data, y_data)
        self.ax.axhline(y=0, color='r', linestyle='--')
        self.ax.axvline(x=0, color='r', linestyle='--')
        self.ax.grid(True)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.canvas.draw()


    def show_error(self, message):
        self.solution_label.setText(f"Error: {message}")
