class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Insert element with priority
    def enqueue(self, value, priority):
        self.queue.append((value, priority))
        print(value, "inserted with priority", priority)

    # Delete highest priority element
    def dequeue(self):
        if len(self.queue) == 0:
            print("Priority Queue is Empty")
            return

        highest_index = 0

        # Find highest priority element
        for i in range(1, len(self.queue)):
            if self.queue[i][1] > self.queue[highest_index][1]:
                highest_index = i

        removed = self.queue.pop(highest_index)
        print(removed[0], "deleted")

    # Display queue
    def display(self):
        if len(self.queue) == 0:
            print("Priority Queue is Empty")
            return

        print("Elements (Value, Priority):")
        for item in self.queue:
            print(item)


# Example
pq = PriorityQueue()

pq.enqueue(10, 2)
pq.enqueue(20, 1)
pq.enqueue(30, 3)
pq.enqueue(40, 5)

pq.display()

pq.dequeue()
pq.display()

pq.dequeue()
pq.display()