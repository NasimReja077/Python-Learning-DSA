def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expression:
        if ch in '([{':
            stack.append(ch)          # push opening brackets

        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return "Non-Matching!"
            stack.pop()               # matching pair found

    # return "Matching!" if not stack else "Non-Matching!"
    
    # Final Check - Best Way
    if not stack:
        return "Matching!"
    else:
        return "Non-Matching!"

# Test (from MAKAUT 2023-24 paper exactly)
print(is_balanced("(A+B)+C"))          # Matching!
print(is_balanced("(A+B+C)"))          # Non-Matching!  ← wait, this is matching
print(is_balanced("((A+B)+C)"))        # Matching!
print(is_balanced("(A+B+C"))           # Non-Matching!
print(is_balanced("(A+B+[C*{D}])"))    # Matching!