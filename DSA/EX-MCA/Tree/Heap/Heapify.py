def heapify(arr, n, i):
    """Maintains Max Heap property for subtree rooted at index i"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and recurse
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
        
        
# Heapify Algorithm (Min Heap)python

def heapify(self, i):
    """Maintains Min Heap Property"""
    n = len(self.heap)
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and self.heap[left] < self.heap[smallest]:
        smallest = left

    # Check right child
    if right < n and self.heap[right] < self.heap[smallest]:
        smallest = right

    # If smallest is not root, swap and recurse
    if smallest != i:
        self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
        self.heapify(smallest)
