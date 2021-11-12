import parser
import calculator

def main():

    input_string = "x"

    formula, variables = parser.parse(input_string)
    print(formula)
    print(variables)

    substitutions = {"x": "2"}

    parser.substitute_variables(formula, variables, substitutions)
    print(formula)

    print(calculator.calculate_formula(formula))

main()
