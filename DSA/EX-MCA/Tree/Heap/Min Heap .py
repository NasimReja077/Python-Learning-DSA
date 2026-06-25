class MinHeap:
    def __init__(self):
        self.heap = [] # Initialize empty heap as a list

    # Helper Functions
    def parent(self, i): 
        return (i - 1) // 2

    def left(self, i): 
        return 2 * i + 1

    def right(self, i): 
        return 2 * i + 2

    # ==================== HEAPIFY ====================
    def heapify(self, i):
        n = len(self.heap)
        smallest = i
        l = self.left(i)
        r = self.right(i)

        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    # ==================== INSERT ====================
    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # Bubble Up
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # ==================== SEARCH ====================
    def search(self, val):
        """Linear Search - O(n)"""
        return val in self.heap

    # ==================== DELETE (Any Value) ====================
    def delete(self, val):
        """
        Delete any value from Min Heap
        """
        if not self.heap:
            return False
        
        try:
            i = self.heap.index(val)          # Find index of value
            # Replace with last element
            self.heap[i] = self.heap[-1]
            self.heap.pop()                   # Remove last element

            # Heapify from the replaced position
            if i < len(self.heap):
                self.heapify(i)
            return True
        except ValueError:
            return False                     # Value not found

    # ==================== EXTRACT MIN ====================
    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return min_val
        
    # ==================== BUILD MIN Heap / BOTTOM-UP ====================
    
    def build_heap(self, arr):
        self.heap = arr[:] # Copy the input array to the heap
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1): # Start from last non-leaf node and heapify each node
            self.heapify(i)
            
    def print_heap(self):
        print(self.heap)
        
        
min_h = MinHeap()
min_h.insert(50)
min_h.insert(30)
min_h.insert(40)
min_h.insert(10)
min_h.insert(70)

min_h.print_heap()
print("Extract Min:", min_h.extract_min())
min_h.print_heap()

print("Search 40:", min_h.search(40))
print("Delete 30:", min_h.delete(30))
min_h.print_heap()