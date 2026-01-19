class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Insertion (Enqueue)
    def enqueue(self, value):
        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full! Insertion not possible.")
            return

        # If queue is empty
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
        
        print(value, "inserted into circular queue")

    # Deletion (Dequeue)
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty! Deletion not possible.")
            return

        removed = self.queue[self.front]
        self.queue[self.front] = None  # optional

        # If only one element exists
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(removed, "deleted from circular queue")

    # Display operation
    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
            return

        print("Circular Queue Elements:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# ---------- Example Usage ----------

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)   # Queue full here
cq.display()

cq.dequeue()
cq.dequeue()
cq.display()

cq.enqueue(60)
cq.enqueue(70)
cq.display()
cq.enqueue(80)  # Queue full here