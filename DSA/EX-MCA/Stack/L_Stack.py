# -------- Node Class --------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# -------- Stack Class --------
class Stack:
    def __init__(self):
        self.top = None   # Top pointer of stack

    # Push Operation
    def push(self, value):
        new_node = Node(value)     # Create new node
        new_node.next = self.top   # Link to previous top
        self.top = new_node        # Update top
        print(value, "pushed into stack")

    # Pop Operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow! Nothing to pop.")
        else:
            popped = self.top.data
            self.top = self.top.next   # Move top to next node
            print(popped, "popped from stack")

    # Display Operation
    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
                
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data
    
    def isEmpty(self):
        return self.top is None


# -------- Example Usage --------
s = Stack()

print("Stack is Empty:", s.isEmpty())

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()

print("Top element is:", s.peek())
print("Popped element:", s.pop())