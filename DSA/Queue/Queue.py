class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Insertion operation
    def enqueue(self, value):
        if self.rear == self.size - 1:
            print("Queue Overflow! Cannot insert.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value
            print(value, "inserted into queue")

    # Deletion operation
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow! Nothing to delete.")
        else:
            deleted_value = self.queue[self.front]
            self.front += 1
            print(deleted_value, "deleted from queue")

    # Display operation
    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Queue elements:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


# Example usage
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
