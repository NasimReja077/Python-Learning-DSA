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