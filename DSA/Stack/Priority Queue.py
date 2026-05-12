class PriorityQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Insert operation
    def enqueue(self, value):
        if self.rear == self.size - 1:
            print("Queue Overflow!")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = value

        print(value, "inserted")

    # Delete highest priority element
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow!")
            return

        max_index = self.front

        # Find highest priority
        for i in range(self.front, self.rear + 1):
            if self.queue[i] > self.queue[max_index]:
                max_index = i

        deleted = self.queue[max_index]

        # Shift elements left
        for i in range(max_index, self.rear):
            self.queue[i] = self.queue[i + 1]

        self.queue[self.rear] = None
        self.rear -= 1

        if self.front > self.rear:
            self.front = -1
            self.rear = -1

        print(deleted, "deleted (highest priority)")

    # Display operation
    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Priority Queue Elements:")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


# Example
pq = PriorityQueue(5)

pq.enqueue(10)
pq.enqueue(40)
pq.enqueue(20)
pq.enqueue(50)
pq.enqueue(30)

pq.display()

pq.dequeue()
pq.display()