import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = [] # Min-Heap (Smallest priority = Highest Priority)
    
    # 1. Insert Operation
    def insert(self, value, priority):
        # Format: (priority, value) # Insert element with its priority
        heapq.heappush(self.heap, (priority, value))
        print(f"Inserted: {value} (Priority: {priority})")
    
    # 2. Dequeue / Extract (Remove highest priority element)
    def dequeue(self): # Remove and return the element with highest priority
        if not self.heap:
            print("Priority Queue is Empty! Underflow.")
            return None
        
        priority, value = heapq.heappop(self.heap)
        print(f"Dequeued: {value} (Priority: {priority})")
        return value
    
    # 3. Peek (View highest priority element without removing)
    
    def peek(self): # Return highest priority element without removing it
        if not self.heap:
            print("Priority Queue is Empty!")
            return None
        return self.heap[0][1] # Return only value
    
    # 4. Check if empty
    def is_empty(self):
        return len(self.heap) == 0
    
    # 5. Get current size
    def size(self):
        return len(self.heap)
    
    # 6. Display all elements
    def display(self):
        if not self.heap:
            print("Priority Queue is Empty!")
            return
        print("Priority Queue Elements (Priority, Value):")
        for priority, value in sorted(self.heap):   # Sorted for better view
            print(f"({priority}, {value})", end=" ")
        print()


# ======= Example Usage 

pq = PriorityQueue()
    
pq.insert("Task A", 3)
pq.insert("Task B", 1)
pq.insert("Task C", 5)
pq.insert("Task D", 2)
pq.insert("Task E", 4)

print("\nCurrent Size:", pq.size())
pq.display()

print("\n--- Performing Dequeue ---")
pq.dequeue()
pq.dequeue()
    
pq.display()
    
print("\nFront Element (Peek):", pq.peek())