import itertools

# Implementation of a classic algorithm designed to check system specification consistency [ [1] ]
# 
# [1]: https://ieeexplore-ieee-org.proxy.library.carleton.ca/document/10485497 "A Quantum Algorithm for System Specifications Verification"


# Table 1. Truth table example for a consistent system with 3 variables and 2 function oracles (F1 = !X0 X2, F2 = !X0 !X1)
# | X0 | X1 | X2 | F1  | F2  | Bool |
# |----|----|----|----|----|----|
# |  0 |  0 |  0 |  0  |  1  | False |
# |  0 |  0 |  1 |  1  |  1  | True |
# |  0 |  1 |  0 |  0  |  0  | False |
# |  0 |  1 |  1 |  1  |  0  | False |
# |  1 |  0 |  0 |  0  |  0  | False |
# |  1 |  0 |  1 |  0  |  0  | False |
# |  1 |  1 |  0 |  0  |  0  | False |
# |  1 |  1 |  1 |  0  |  0  | False |
# 
# Table 2. Truth table example for an inconsistent system with 3 variables and 2 function oracles (F1 = X0 !X2, F2 = !X0 !X1)
# | X0 | X1 | X2 | F1  | F2  | Bool |
# |----|----|----|----|----|----|
# |  0 |  0 |  0 |  0  |  1  | False |
# |  0 |  0 |  1 |  0  |  1  | False |
# |  0 |  1 |  0 |  0  |  0  | False |
# |  0 |  1 |  1 |  0  |  0  | False |
# |  1 |  0 |  0 |  1  |  0  | False |
# |  1 |  0 |  1 |  0  |  0  | False |
# |  1 |  1 |  0 |  1  |  0  | False |
# |  1 |  1 |  1 |  0  |  0  | False |



def evaluate_specification_term(term, variable_values):
    """
    Function: evaluate_specification_term
    Params: term (string like "0x1" representing a specification pattern),
            variable_values (list of binary values for variables [X0,X1,...])
    Return: bool - True if values match term pattern, False otherwise
    """

    for var_value, term_char in zip(variable_values, term):
        if term_char not in ('x', str(var_value)):
            return False
    return True

def check_specification_consistency(n, terms):
    """
    Function: check_specification_consistency
    Params: n (number of variables),
            terms (list of specification terms)
    Return: bool - True if system is consistent, False otherwise
    
    Implements the classical truth table method according to the article's 4 steps:
    1. Terms represent Boolean functions 
    2. Generates full 2^n truth table
    3. Evaluates all terms against each row
    4. Returns True if any row satisfies all terms simultaneously
    
    """
    
    for variable_values in itertools.product([0, 1], repeat=n):
        all_terms_satisfied = True
        for term in terms:
            if not evaluate_specification_term(term, variable_values):
                all_terms_satisfied = False
                break
        if all_terms_satisfied:
            return True
    
    return False


# Table 1 (consistent system)
print("Table 1 (consistent):", check_specification_consistency(3, ["0x1", "00x"]))  
print("Table 1 (consistent):", check_specification_consistency(5, ["0x1x1", "x01x1", "00xxx","0x11x","xx1x1"]))  

# Table 2 (inconsistent system)
print("Table 2 (inconsistent):", check_specification_consistency(3, ["1x0", "00x"])) 
print("Table 2 (inconsistent):", check_specification_consistency(3, ["011", "00x"])) 

