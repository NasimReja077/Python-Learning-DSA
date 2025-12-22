class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to store stack elements

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Get the number of elements in the stack.

        Returns:
            int: Number of elements in the stack.
        """
        return len(self.stack)

    def push(self, item):
        """
        Add an element to the top of the stack.

        Args:
            item: The element to be added to the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the topmost element from the stack.

        Returns:
            The topmost element of the stack, or "Stack is empty" if the stack is empty.
        """
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def top(self):
        """
        Get the topmost element of the stack without removing it.

        Returns:
            The topmost element of the stack, or "Stack is empty" if the stack is empty.
        """
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]


# Example usage:

stack = Stack()  # Create an instance of the Stack class

print(stack.isEmpty())  # Output: True

stack.push(10)  # Pushing element 10
stack.push(20)  # Pushing element 20

print(stack.size())  # Output: 2

print(stack.top())  # Output: 20

print(stack.pop())  # Output: 20

print(stack.isEmpty())  # Output: False