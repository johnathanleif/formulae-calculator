
class Sequence:
    NEW = -1
    NUMBER = 0
    VAR = 1


OPERATORS = {'+','-','*','/','(',')','^','%'}

def parse(input_str):
    """ Parse input string.
        Identify variables and replace multiplied variables and brackets with
        expanded operations e.g 2x becomes 2 * x, 2(x+y) becomes 2*(x+y), etc.
        Return formula string following python syntax for use with eval()
        and set of variables with string start and end positions
    """

    formula = []
    variables = {}
    sequence = ""
    seq_type = Sequence.NEW

    for c in input_str:
        if c == ' ':        #ignore spaces
            pass
        elif c in OPERATORS:
            append_sequence_to_formula(formula, c, sequence, seq_type, variables)
 
            if c == '^':        #replace power operator with python syntax
                formula.append("**")
            else:
                formula.append(c)
            
            #start new sequence
            sequence = ""
            seq_type = Sequence.NEW

        else:
            if seq_type is Sequence.NEW:
                if is_number(c):
                    seq_type = Sequence.NUMBER
                else:
                    seq_type = Sequence.VAR

                sequence += c

            elif seq_type is Sequence.NUMBER:
                if not is_number(c) and c != '.':      #if number was start of multiplied variable
                    #append leading number with multiplication operator 
                    formula.append(sequence)
                    formula.append('*')
                    
                    #change sequence to variable
                    seq_type = Sequence.VAR
                    sequence = c
                else:
                    sequence += c
            
            elif seq_type is Sequence.VAR:
                sequence += c

    if len(formula) > 1 and formula[-1] != ')':      #append final sequence
        append_sequence_to_formula(formula, '', sequence, seq_type, variables)

    return formula, variables


def is_number(c):
    return '0' <= c and c <= '9'


def append_sequence_to_formula(formula, operator, sequence, seq_type, variables):
    if seq_type is Sequence.VAR:     #if var: add to set with position
        if sequence in variables:
            variables[sequence].add({len(formula)})
        else:
            variables[sequence] = {len(formula)}
                    
    formula.append(sequence)     #append sequence

    if operator == '(' and seq_type is not Sequence.NEW or formula[-1] == ')':       #if operator is open bracket following a sequence or close bracket 
        formula.append('*')      #require multiplication operator after sequence
        

def substitute_variables(formula, variables, substitutions):
    for sub in substitutions:
        for pos in variables[sub]:
            formula[pos] = substitutions[sub]

    return formula

