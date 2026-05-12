class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None


def check_brackets(expression):
    stk = Stack() # Create an instance of the stack class to use for checking brackets
    opening = "({["
    closing = ")}]"
    matching = {')': '(', '}': '{', ']': '['} # Dictionary to map closing brackets to their corresponding opening brackets

    for char in expression:
        if char in opening:
            stk.push(char)
        
        elif char in closing:
            if stk.is_empty() or stk.pop() != matching[char]:
                return "Non-Matching!"
    
    if stk.is_empty():
        return "Matching!"
    else:
        return "Non-Matching!"


# Test Cases
print(check_brackets("(A+B)+C"))          # Matching!
print(check_brackets("(A+B)+C)"))         # Non-Matching!
print(check_brackets("((A+B)+C+(E*F)"))   # Non-Matching!