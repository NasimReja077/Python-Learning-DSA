def isBalanced(expr):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in expr:
        # Opening bracket
        if char in '({[':
            stack.append(char)
        
        # Closing bracket
        elif char in ')}]':
            if not stack: #Extra closing #No matching opening bracket
                return False
            top = stack.pop() # Remove top opening bracket
            if top != brackets[char]: # Mismatched bracket
                return False
 # If stack is empty, all brackets matched
    return len(stack) == 0   # True if stack empty

# print(isBalanced("((A+B)+C)"))        # True
# print(isBalanced("(A+B)+C)"))         # False
# print(isBalanced("{(A+B)*[C-D]}"))    # True

# Test Cases
expressions = [
    "(A+B)+C",
    "(A+B+C)",
    "((A+B)+C)",
    "(A+B+C",
    "(A+B+[C*{D}])",
    "{[()]}",
    "{[(])}"
]

for exp in expressions:
    if isBalanced(exp):
        print(exp, "-> Matching!")
    else:
        print(exp, "-> Non-Matching!")