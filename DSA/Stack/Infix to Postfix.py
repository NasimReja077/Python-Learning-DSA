def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0

def is_operand(ch):
    return ch.isalnum()  # letters or digits

def infix_to_postfix(expression):
    stack = []
    output = []

    for token in expression:
        if is_operand(token):
            output.append(token)          # Case A: operand → output

        elif token == '(':
            stack.append(token)           # Case B: ( → push

        elif token == ')':                # Case C: ) → pop till (
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()                   # discard '('

        else:                             # Case D: operator
            # For ^ (right-associative), use strict >
            # For others (left-associative), use >=
            while (stack and stack[-1] != '(' and
                   ((token != '^' and precedence(stack[-1]) >= precedence(token)) or
                    (token == '^' and precedence(stack[-1]) > precedence(token)))):
                output.append(stack.pop())
            stack.append(token)

    while stack:                          # pop remaining
        output.append(stack.pop())

    return ' '.join(output)

# Test
print(infix_to_postfix("(A+B)*C-(D-E)*(F+G^H)"))
# Output: A B + C * D E - F G H ^ + * -

print(infix_to_postfix("A+B*C"))
# Output: A B C * +