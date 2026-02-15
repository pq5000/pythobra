import sys
from PySide6.QtWidgets import QApplication
from model import EquationModel
from view import EquationView
from controller import EquationController

def main():
    app = QApplication(sys.argv)

    model = EquationModel()
    view = EquationView()
    controller = EquationController(model, view)

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
