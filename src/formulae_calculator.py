import parser
import calculator
from view import *


formula = []
variables = {}
result = 0

def main():
    global view
    view = TkView(FormulaInputObserver, VariableInputObserver)
    view.open_window()


def take_variable_input():
    view.create_variable_input(variables)


def display_result():
    view.display_result(str(calculator.calculate_formula(formula)))


class FormulaInputObserver:
    def notify(input_formula_string):
        global formula, variables, view
        formula, variables = parser.parse(input_formula_string)
        take_variable_input()


class VariableInputObserver:
    def notify(variable_substitutions):
        parser.substitute_variables(formula, variables, variable_substitutions)
        display_result()


main()
