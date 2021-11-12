from parser import *
from calculator import *
<<<<<<< HEAD
=======
from view import *


formula = []
variables = {}
result = 0
>>>>>>> dev-ui

def main():
    global view
    view = TkView(FormulaInputObserver, VariableInputObserver)
    view.open_window()


def take_variable_input():
    view.create_variable_input(variables)


def display_result():
    view.display_result(str(calculate("".join(formula))))

<<<<<<< HEAD
    input_string = "x"

    formula, variables = parse(input_string)
    print(formula)
    print(variables)

    substitutions = {"x": "2"}

    substitute_variables(formula, variables, substitutions)
    print(formula)

    print(calculate_formula(formula))
=======

class FormulaInputObserver:
    def notify(input_formula_string):
        global formula, variables
        formula, variables = parse(input_formula_string)
        take_variable_input()


class VariableInputObserver:
    def notify(variable_substitutions):
        substitute_variables(formula, variables, variable_substitutions)
        display_result()

>>>>>>> dev-ui

main()
