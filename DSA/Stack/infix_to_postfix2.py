def infix_to_postfix(expr):
    stack = []
    output = []
    precedence = {'^':3, '*':2, '/':2, '+':1, '-':1}
    
    for token in expr:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and \
                  precedence.get(stack[-1],0) >= precedence.get(token,0):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    return ''.join(output)


print(infix_to_postfix("A+B"))          # AB+
print(infix_to_postfix("A+B*C"))        # ABC*+
print(infix_to_postfix("(A+B)*C"))      # AB+C*
print(infix_to_postfix("A*(B+C)"))      # ABC+*
print(infix_to_postfix("(A+B)*(C-D)"))  # AB+CD-*
print(infix_to_postfix("A+B*C-D"))      # ABC*+D-
print(infix_to_postfix("A*(B+C)/D"))    # ABC+*D/
print(infix_to_postfix("((A+B)+C)"))    # AB+C+
print(infix_to_postfix("A+B+C"))        # AB+C+