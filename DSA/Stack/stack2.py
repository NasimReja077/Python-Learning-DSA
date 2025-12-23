class Node:
    """Represents an individual node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class Stack:
    """Implements a stack data structure using a linked list."""
    def __init__(self):
        self.head = None  # Points to the top of the stack (head of the list)
        self.size = 0

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.head is None

    def push(self, data):
        """Adds a new element to the top of the stack (insertion at the head)."""
        new_node = Node(data)
        if self.head:
            new_node.next = self.head  # Link the new node to the old head
        self.head = new_node  # Update the head to the new node
        self.size += 1
        print(f"Pushed: {data}")

    def pop(self):
        """Removes and returns the top element from the stack (deletion from the head)."""
        if self.is_empty():
            return "Stack is empty"
        popped_node_data = self.head.data
        self.head = self.head.next  # Move the head to the next node
        self.size -= 1
        return f"Popped: {popped_node_data}"

    def peek(self):
        """Returns the top element without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return f"Top element: {self.head.data}"

    def display(self):
        """Prints the current stack elements from top to bottom."""
        current = self.head
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack (top -> bottom): ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
        # Create a stack instance
my_stack = Stack()

# Perform operations
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

my_stack.display() # Output: Stack (top -> bottom): 30 -> 20 -> 10 -> None

print(my_stack.peek()) # Output: Top element: 30

print(my_stack.pop()) # Output: Popped: 30
print(my_stack.pop()) # Output: Popped: 20

my_stack.display() # Output: Stack (top -> bottom): 10 -> None

print(my_stack.is_empty()) # Output: False

print(my_stack.pop()) # Output: Popped: 10
print(my_stack.pop()) # Output: Stack is empty
