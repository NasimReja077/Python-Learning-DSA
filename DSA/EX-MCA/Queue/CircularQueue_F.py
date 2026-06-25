class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        
        
    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front
            # self.rear == self.size - 1
    
    def get_size(self):
        if self.is_empty():
            return 0
        if self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.size - self.front + self.rear + 1

    # Insertion (Enqueue)
    def enqueue(self, value):
        # Check if queue is full
        if self.is_full():
            print("Queue is Full! Insertion not possible.")
            return

        # If queue is empty
        if self.is_empty():
            self.front = 0
            self.rear = 0
            # self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            # self.queue[self.rear] = value
        
        self.queue[self.rear] = value
        print(value, "inserted into circular queue")
        return True

    # Deletion (Dequeue)
    def dequeue(self):
        if self.is_empty():
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
        return removed
        
    # Peek (View front element without removing)
    def peek(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        return self.queue[self.front]


    # Display operation
    def display(self):
        if self.is_empty:
            print("Queue is Empty!")
            return

        print("Circular Queue Elements:", end="")
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