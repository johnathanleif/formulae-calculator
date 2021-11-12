
class Operand:
    """ Operand types.
        NEW: Not yet defined.
        NUM: A number.
        VAR: A variable.
    """
    NEW = -1
    NUM = 0
    VAR = 1


OPERATORS = {'+','-','*','/','(',')','^','%'}

def parse(input_formula):
    """ Parse input string.
        Identify variables, replace multiplied variables and brackets with
        expanded operations (e.g 2x becomes 2 * x, 2(x+y) becomes 2*(x+y), etc.)
        and replace non-python syntax with python syntax.
        Params:
            input_formula: the inputted formula string
        Return:
            formula in list form holding serparated operands and operators in given order
    """
    formula = []
    variables = {}
    operand = ""
    operand_type = Operand.NEW

    for c in input_formula:
        if c == ' ':        #ignore spaces
            pass
        elif c in OPERATORS:
            _append_operand_to_formula(formula, c, operand, operand_type, variables)
 
            if c == '^':        #replace power operator with python syntax
                formula.append("**")
            else:
                formula.append(c)
            
            #start new operand
            operand = ""
            operand_type = Operand.NEW

        else:
            if operand_type is Operand.NEW:
                if _is_number(c):
                    operand_type = Operand.NUM
                else:
                    operand_type = Operand.VAR

                operand += c

            elif operand_type is Operand.NUM:
                if not _is_number(c) and c != '.':      #if number was start of multiplied variable
                    #append leading number with multiplication operator 
                    formula.append(operand)
                    formula.append('*')
                    
                    #change operand to variable
                    operand_type = Operand.VAR
                    operand = c
                else:
                    operand += c
            
            elif operand_type is Operand.VAR:
                operand += c

    if operand_type is not Operand.NEW:      #append final operand
        _append_operand_to_formula(formula, '', operand, operand_type, variables)

    return formula, variables


def _is_number(c):
    return '0' <= c and c <= '9'


def _append_operand_to_formula(formula, operator, operand, operand_type, variables):
    if operand_type is Operand.VAR:     #if var: add to set with position
        if operand in variables:
            variables[operand].add({len(formula)})
        else:
            variables[operand] = {len(formula)}
                    
    formula.append(operand)     #append operand

    if operator == '(' and operand_type is not Operand.NEW or formula[-1] == ')':       #if operator is open bracket following a operand or close bracket 
        formula.append('*')      #require multiplication operator after operand
        

def substitute_variables(formula, variables, substitutions):
    """ Substitute variables in formula with inputted numbers.
        Parameters:
            formula: formula as list of ordered, seperated operands and operators
            variables: variables mapped to indicies in formula list
            substitutions: variables mapped to numeric substitution
        Return:
            the altered formula
    """
    for sub in substitutions:
        for pos in variables[sub]:
            formula[pos] = substitutions[sub]

    return formula

