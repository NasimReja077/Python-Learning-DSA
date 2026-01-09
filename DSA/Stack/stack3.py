class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    # i) Push operation
    def push(self, value):
        if len(self.stack) == self.size:
            print("Stack Overflow! Cannot push.")
        else:
            self.stack.append(value)
            print(value, "pushed into stack")

    # ii) Pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow! Nothing to pop.")
        else:
            removed = self.stack.pop()
            print(removed, "popped from stack")

    # iii) Display operation
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            for item in reversed(self.stack):
                print(item)


# --------- Example Usage ---------
s = Stack(5)

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()
