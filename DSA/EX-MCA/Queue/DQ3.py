from collections import deque

class Deque:
    def __init__(self, size):
        self.deque = deque(maxlen=size)   # Built-in efficient Deque
    
    def insert_front(self, item):
        self.deque.appendleft(item)
    
    def insert_rear(self, item):
        self.deque.append(item)
    
    def delete_front(self):
        if self.deque:
            return self.deque.popleft()
        return None
    
    def delete_rear(self):
        if self.deque:
            return self.deque.pop()
        return None
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def display(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        # Convert to list just for clean presentation
        print("Deque elements (front to rear):", list(self.deque))
        
# Create a Deque with a maximum size of 3
dq = Deque(3)

# Test insertions
dq.insert_rear(10)   # [10]
dq.insert_rear(20)   # [10, 20]
dq.insert_front(5)   # [5, 10, 20]
dq.display()
# Test overflow constraint
dq.insert_rear(40)   # Fails safely because size is capped at 3
# Test deletions
dq.delete_front()    # Removes 5 -> [10, 20]
dq.delete_rear()     # Removes 20 -> [10]
dq.display()