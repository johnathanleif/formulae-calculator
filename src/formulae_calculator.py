from parser import parse

def main():

    input_string = "x + y"

    formula, variables = parse(input_string)
    print(formula)


main()
