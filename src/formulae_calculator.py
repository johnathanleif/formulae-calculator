from parser import *
from calculator import *

def main():

    input_string = "x"

    formula, variables = parse(input_string)
    print(formula)
    print(variables)

    substitutions = {"x": "2"}

    substitute_variables(formula, variables, substitutions)
    print(formula)

    print(calculate_formula(formula))

main()
