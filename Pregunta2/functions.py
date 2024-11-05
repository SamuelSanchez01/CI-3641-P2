def evaluatePrefix(expression):
    """
    Function that evaluate prefix notation

    Same code as postfix but inverts the expression
    """
    stack = []
    operators = set(['+', '-', '*', '/'])
    expression = expression.split()[::-1]  #Invert
    hasOperator = False

    for token in expression:
        if token not in operators:
            stack.append(int(token))
        else:
            hasOperator = True
            number1 = stack.pop()
            number2 = stack.pop()
            if token == '+':
                result = number1 + number2
            elif token == '-':
                result = number1 - number2
            elif token == '*':
                result = number1 * number2
            elif token == '/':
                result = number1 // number2 
            stack.append(result)

    #Case: no operators
    if not hasOperator:
        return " ".join(reversed(expression))
    return stack.pop()

def evaluatePostfix(expression):
    """
    Function that evaluate post fix notation
    """
    #variables
    stack = []
    operators = set(['+', '-', '*', '/'])
    expression = expression.split()
    hasOperator = False
    #all tokens
    for token in expression:
        #append num
        if token not in operators:
            stack.append(int(token))
        #proccess operator
        else:
            hasOperator = True
            number2 = stack.pop()
            number1 = stack.pop()
            if token == '+':
                result = number1 + number2
            elif token == '-':
                result = number1 - number2
            elif token == '*':
                result = number1 * number2
            elif token == '/':
                result = number1 // number2
            stack.append(result)

    #Case: no operators
    if not hasOperator:
        return " ".join(expression)
    return stack.pop()

def showPrefix(expression):
    """
    Function that shows prefix notation operations

    Same code as postfix but inverts the expression
    """
    stack = []
    operators = set(['+', '-', '*', '/'])
    operatorPrecedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    hasOperator = False
    expression = expression.split()[::-1]
    for token in expression:
        #if the token is operator
        if token in operators:
            hasOperator = True
            #if we dont have enough nums returns None
            if len(stack) < 2:
                return None
            #get operators
            number1, operator1 = stack.pop()
            number2, operator2 = stack.pop()

            #add parenthesis if neccesary
            if operator1 and operatorPrecedence[operator1] < operatorPrecedence[token]:
                number1 = f"({number1})"
            #add parenthesis if neccesary
            if operator2 and operatorPrecedence[operator2] <= operatorPrecedence[token]:
                number2 = f"({number2})"
            #add to the stack
            stack.append((f"{number1} {token} {number2}", token))
        #if num
        else:
            #add num
            stack.append((token, ""))

    #case no operator
    if not hasOperator:
        return " ".join(reversed(expression))
    
    #case more than 1 element stack
    if len(stack) != 1:
        return None

    # Return the expression in infix notation
    return stack[-1][0]

def showPostfix(expression):
    """
    Function that shows postfix notation operations

    Same code as prefix but without invert the expression
    """
    stack = []
    operators = set(['+', '-', '*', '/'])
    operatorPrecedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    hasOperator = False

    expression = expression.split()
    for token in expression:
        if token in operators:
            hasOperator = True
            if len(stack) < 2:
                return None
            number2, operator2 = stack.pop()
            number1, operator1 = stack.pop()
            if operator1 and operatorPrecedence[operator1] < operatorPrecedence[token]:
                number1 = f"({number1})"
            if operator2 and operatorPrecedence[operator2] <= operatorPrecedence[token]:
                number2 = f"({number2})"
            stack.append((f"{number1} {token} {number2}", token))
        else:
            stack.append((token, ""))

    #Case: no operators
    if not hasOperator:
        return " ".join(expression)

    #
    if len(stack) != 1:
        return None
    #Return
    return stack[-1][0]