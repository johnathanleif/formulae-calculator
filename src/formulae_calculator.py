import parser
import calculator
import view

def main():

    input_string = "x + yz"

    formula, variables = parser.parse(input_string)
    print(formula)
    print(variables)

    substitutions = {"x": "2", "yz": "3"}

    parser.substitute_variables(formula, variables, substitutions)
    print(formula)

    print(calculator.calculate_formula(formula))

    view.open_window()

main()
