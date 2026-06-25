def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()   # split by space

    for token in tokens:
        if token.lstrip('-').isdigit():  # operand (number)
            stack.append(int(token))

        else:                            # operator
            op2 = stack.pop()            # second operand (popped first)
            op1 = stack.pop()            # first operand (popped second)

            if   token == '+': stack.append(op1 + op2)
            elif token == '-': stack.append(op1 - op2)
            elif token == '*': stack.append(op1 * op2)
            elif token == '/': stack.append(int(op1 / op2))
            elif token == '^': stack.append(op1 ** op2)

    return stack[0]   # final answer

# Test
print(evaluate_postfix("5 1 2 + 4 * + 3 -"))   # 14
print(evaluate_postfix("7 3 + 5 *"))            # 50
print(evaluate_postfix("8 2 3 ^ / 2 3 * +"))   # 7


# def evaluate_postfix(postfix):
#     stack = []
#     for token in postfix.split():   # assuming space separated
#         if token.isdigit():
#             stack.append(int(token))
#         else:
#             b = stack.pop()
#             a = stack.pop()
#             if token == '+': stack.append(a + b)
#             elif token == '-': stack.append(a - b)
#             elif token == '*': stack.append(a * b)
#             elif token == '/': stack.append(a / b)
#             elif token == '^': stack.append(a ** b)
#     return stack.pop()
