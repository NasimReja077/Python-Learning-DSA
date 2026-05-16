class InputRestrictedDeque:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Only this insertion is allowed
    def insert_rear(self, value):
        if self.is_full():
            print("Deque Overflow! Cannot insert at rear.")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.deque[self.rear] = value
        print(value, "inserted at rear.")

    # Deletion from both ends allowed
    def delete_front(self):
        if self.is_empty():
            print("Deque Underflow! Nothing to delete at front.")
            return None

        removed = self.deque[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(removed, "deleted from front.")
        return removed

    def delete_rear(self):
        if self.is_empty():
            print("Deque Underflow! Nothing to delete at rear.")
            return None

        removed = self.deque[self.rear]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size

        print(removed, "deleted from rear.")
        return removed

    def display(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        print("Deque elements (front to rear): ", end="")
        i = self.front
        while True:
            print(self.deque[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()