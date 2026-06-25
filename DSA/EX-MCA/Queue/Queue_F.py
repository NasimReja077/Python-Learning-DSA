class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size # Creates Array size 5. [None, None, ..]
        self.front = -1
        self.rear = -1
        
# Front points to the first element.
# -1 means queue is empty.

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.size - 1
        
    # Insertion operation
    def enqueue(self, value):
        if self.is_full(): # if self.rear == self.size - 1:
            print("Queue Overflow! Cannot insert.")
        else:
            if self.front == -1:   # First element
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value
            print(value, "inserted into queue")

    # Deletion operation
    def dequeue(self):
        # if self.front == -1 or self.front > self.rear:
        if self.is_empty() or self.front > self.rear:
            print("Queue Underflow! Nothing to delete.")
        else:
            deleted_value = self.queue[self.front]
            self.front += 1
            print(deleted_value, "deleted from queue")
            # Optional: Reset when queue becomes empty
            if self.front > self.rear:
                self.front = self.rear = -1

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front]

    # Display operation
    def display(self):
        if self.is_empty() or self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Queue elements: ", end="")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# ===================== Example Usage =====================
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
q.enqueue(40)
q.peek()
q.display()