class Deque:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    # i) Insertion from rear end
    def insert_rear(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Deque Overflow! Cannot insert at rear.")
            return

        if self.front == -1:  # empty deque
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.deque[self.rear] = value
        print(value, "inserted at rear.")

    # ii) Insertion from front end
    def insert_front(self, value):
        if (self.front - 1 + self.size) % self.size == self.rear:
            print("Deque Overflow! Cannot insert at front.")
            return

        if self.front == -1:  # empty deque
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size

        self.deque[self.front] = value
        print(value, "inserted at front.")

    # iii) Deletion from front end
    def delete_front(self):
        if self.front == -1:
            print("Deque Underflow! Nothing to delete at front.")
            return

        removed = self.deque[self.front]
        self.deque[self.front] = None

        if self.front == self.rear:  # only one element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(removed, "deleted from front.")

    # iv) Deletion from rear end
    def delete_rear(self):
        if self.rear == -1:
            print("Deque Underflow! Nothing to delete at rear.")
            return

        removed = self.deque[self.rear]
        self.deque[self.rear] = None

        if self.front == self.rear:  # only one element
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size

        print(removed, "deleted from rear.")

    # v) Display the Deque
    def display(self):
        if self.front == -1:
            print("Deque is empty.")
            return

        print("Deque elements (front to rear):")
        i = self.front
        while True:
            print(self.deque[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
# ---------- Example Usage ----------
if __name__ == "__main__":
    deque = Deque(5)

    deque.insert_rear(10)
    deque.insert_rear(20)
    deque.insert_front(5)
    deque.display()

    deque.delete_front()
    deque.display()

    deque.delete_rear()
    deque.display()
    
    
