# Top Pointer - Fixed Array Implementation

class Stack:
    def __init__(self, size=10):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    # Push Operation
    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow! Cannot push", value)
            return
        self.top += 1
        self.stack[self.top] = value
        print(value, "pushed into stack")

    # Pop Operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow! Nothing to pop.")
            return None
        item = self.stack[self.top]
        self.top -= 1
        print(item, "popped from stack")
        return item

    # Peek Operation
    def peek(self):
        if self.top == -1:
            print("Stack is empty.")
            return None
        print("Top element is:", self.stack[self.top])
        return self.stack[self.top]

    # Display Operation
    def display(self):
        if self.top == -1:
            print("Stack is empty.")
            return
        print("Stack elements (Top to Bottom):")
        for i in range(self.top, -1, -1): # -1, -1 means we are going in reverse order from top to bottom
            print(self.stack[i])

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1
   
s = Stack(5)
s.is_empty()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.is_empty()
s.is_full()
s.display()
s.pop()
s.pop()
s.display()
s.peek()
s.display()