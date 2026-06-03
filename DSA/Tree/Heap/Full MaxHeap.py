class MaxHeap:
    def __init__(self):
        self.heap = []

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
        largest = i
        l = self.left(i)
        r = self.right(i)

        if l < n and self.heap[l] > self.heap[largest]:
            largest = l
        if r < n and self.heap[r] > self.heap[largest]:
            largest = r
            
        # if largest is not the current index (i), we need to swap and heapify again to maintain the max heap property    
        if largest != i: # i mins curent root node index. ex- i=0 | largest = 1 | So we will swap arr[0] with arr[1]
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    # ==================== INSERT ====================
    def insert(self, val):
        self.heap.append(val) # Append the new value to the end of the heap
        i = len(self.heap) - 1 # Get the index of the newly added value
        # i is index for newly added value, we will compare it with its parent and swap if it's greater (for Max Heap) # self.heap is parent node # - 1 because we want to get the index of the parent node, which is one less than the index of the current node (i) 

        # Bubble Up
        # We compare the newly added value with its parent and swap if it's greater (for Max Heap)
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]: # If parent is smaller than the current node, we swap them and move up the tree until we find the correct position for the new value or we reach the root node 
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i] # Swap the current node with its parent 
            i = self.parent(i) # Move up to the parent's index for the next iteration

    # ==================== SEARCH ====================
    def search(self, val):
        """Linear Search - O(n)"""
        return val in self.heap

    # ==================== DELETE (Any Value) ====================
    def delete(self, val):
        if not self.heap:
            return False
        try:
            i = self.heap.index(val) # .index(val) is used find index value to delete # Find index of value to be deleted
            # Replace with last element
            self.heap[i] = self.heap[-1] # self.heap[-1] is the last element in the heap, we replace the value to be deleted with the last element and then remove the last element from the heap
            self.heap.pop()

            if i < len(self.heap):
                self.heapify(i)
            return True
        except ValueError:
            return False

    # ==================== EXTRACT MAX  ====================
    def extract_max(self):
        if not self.heap:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1] # Replace the root of the heap (the maximum value) with the last element in the heap
        self.heap.pop()
        self.heapify(0) # Heapify from the root to restore the max heap property after extracting the maximum value ,why 0? because we want to start heapifying from the root node (index 0) after replacing it with the last element, to ensure that the max heap property is maintained throughout the heap.
        return max_val

    # ==================== BUILD HEAP / BOTTOM-UP ====================
    def build_heap(self, arr):
        self.heap = arr[:] # Copy the input array to the heap , arr[:] shallow copy of the input array,This is important to avoid modifying OG array outside the class when we perform heap operations.
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1): # n//2-1 is last non-leaf node index, -1 because we want to include the last non-leaf node in the loop, -1 is for reverse order
            self.heapify(i)

    def print_heap(self):
        print(self.heap)

# Example Usage
max_heap = MaxHeap()

max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(50)
max_heap.insert(30)
max_heap.insert(40)
max_heap.insert(70)
max_heap.insert(60)
max_heap.insert(25)
max_heap.print_heap() # Should print a max heap
# Time Complexity:O(n) for building the heap, O(log n) for inserting a new element, O(n) for searching an element, O(n) for deleting an element, and O(log n) for extracting the maximum element.
# Space Complexity: O(n) for storing the heap elements.
print(max_heap.extract_max())  # Should return 50
max_heap.print_heap()  # Should print the heap after extracting max
print(max_heap.search(30))  # Should return True
print(max_heap.delete(20))  # Should return True
max_heap.print_heap()  # Should print the heap after deletion


max_heap.build_heap([3, 9, 2, 1, 4, 5])
print("Max Heap:", max_heap.heap)

print("Extracted Max:", max_heap.extract_max())
print("Max Heap after extraction:", max_heap.heap)
max_heap.insert(10)
print("Max Heap after inserting 10:", max_heap.heap)
print("Search for 4:", max_heap.search(4))
