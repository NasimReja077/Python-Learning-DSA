class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        # Check if the queue is full
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")
        # Check if the queue is empty
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        # Normal insertion
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

    def dequeue(self):
        # Check if the queue is empty
        if (self.front == -1):
            print("queue is empty")
            
        # Check if there is only one element left
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        # Normal removal
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size
            
    def display(self):
         if self.front == -1:
              print("Queue is empty")
              return
         
         print("Queue elements:", end=" ")
         # Logic: Start at front, stop after printing the rear element
         temp = self.front
         while True:
              print(self.items[temp], end=" ")
              if temp == self.rear:
                   break
              temp = (temp + 1) % self.size
         print()
          
cq = CircularQueue(5)

# Fill the queue
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

# Perform operations
cq.dequeue()      # Removes 10
cq.enqueue(60)    # Adds 60 to the position where 10 was
cq.dequeue()      # Removes 20
cq.dequeue()      # Removes 30
cq.dequeue()      # Removes 40
cq.dequeue()      # Removes 50
cq.dequeue()      # Removes 60
cq.dequeue()      # Attempt to dequeue from empty queue

cq.display()      # Display the remaining elements in the queue
cq.enqueue(70)
cq.enqueue(80)
cq.display()
