class PriorityQueue:
    def __init__(self):
        self.queue = []          # List to store (priority, value) pairs
    
    # 1. Insert Operation
    def insert(self, value, priority):
        """Insert element with priority (Unsorted)"""
        self.queue.append((priority, value))
        print(f"Inserted: {value} (Priority: {priority})")
    
    # 2. Dequeue - Remove highest priority element (Smallest priority number)
    def dequeue(self):
        
        """Remove and return element with highest priority"""
        
        if not self.queue:
            print("Priority Queue is Empty! Underflow.")
            return None
        
        # Find the element with minimum priority (highest priority)
        min_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] < self.queue[min_index][0]:
                min_index = i
        
        # Remove and return the highest priority element
        priority, value = self.queue.pop(min_index)
        print(f"Dequeued: {value} (Priority: {priority})")
        return value
    
    # 3. Peek - View highest priority element without removing
    def peek(self):
        
        """Return highest priority element without removing"""
        
        if not self.queue:
            print("Priority Queue is Empty!")
            return None
        
        # Find minimum priority
        min_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] < self.queue[min_index][0]:
                min_index = i
        return self.queue[min_index][1]
    
    # 4. Check if empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # 5. Get size
    def size(self):
        return len(self.queue)
    
    # 6. Display
    def display(self):
        if not self.queue:
            print("Priority Queue is Empty!")
            return
        print("Priority Queue Elements (Priority, Value):")
        for priority, value in self.queue:
            print(f"({priority}, {value})", end=" ")
        print()


# ===================== Example Usage =====================

pq = PriorityQueue()

pq.insert("Task A", 3)
pq.insert("Task B", 1)
pq.insert("Task C", 5)
pq.insert("Task D", 2)
pq.insert("Task E", 4)

print("\nCurrent Size:", pq.size())
pq.display()

print("\n--- Dequeue Operations ---")
pq.dequeue()
pq.dequeue()

pq.display()
print("Front Element (Peek):", pq.peek())