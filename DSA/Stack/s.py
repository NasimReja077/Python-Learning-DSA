class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [] # using list as dynamic array
    
    # i) Push operation
    def push(self, value):
        if len(self.stack) == self.size:
            print("Stack Overflow! Cannot push.", value)
        else:
            self.stack.append(value)
            print(value, "pushed into stack")

    # ii) Pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow! Nothing to pop.")
            return None
        else:
            removed = self.stack.pop()
            print(removed, "popped from stack")
            return removed

     # iii) Peek operation
    def peek(self):
         if len(self.stack) == 0:
              print("Stack is empty.")
              return None
         else:
              Top_element = self.stack[-1] # -1 index gives the last element in the list , Which is the top of the stack.
              print("Top_element is:", Top_element)
              return Top_element  # Return top element
              
      # iv) Length operation        
    def length(self):
        current_size = len(self.stack)
        print("Current stack size is:", current_size)
        return current_size
         
     # v) Is Empty Operation
    def is_empty(self):
         if len(self.stack) == 0:
              print("Stack is empty.")
              return True
         else:
              print("Stack is not empty.")
              return False

    # vi) is full operation
    def is_full(self):
        if len(self.stack) == self.size:
            print("Stack is Full.")
            return True
        else:
            print("Stack is not Full.")
            return False

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

s.is_empty()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)          # This will show Overflow

s.is_empty()
s.is_full()
s.display()

s.pop()
s.pop()
s.display()

s.peek()
s.length()
s.display()