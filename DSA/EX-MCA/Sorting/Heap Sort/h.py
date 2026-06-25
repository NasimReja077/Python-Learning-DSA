# arr = array
# n = heap size
# i = current root node index

def heapify(arr, n, i):
    """Heapify a subtree rooted at index i"""
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child
    right = 2 * i + 2    # Right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]   # Swap
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    """Main Heap Sort Function"""
    n = len(arr)
    
    # Step 1: Build Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call heapify on reduced heap
        heapify(arr, i, 0)   # Note: heap size is now 'i'
    
    return arr


# Example Usage
arr = [64, 32, 25, 12, 22, 11, 90]
print("Original Array:", arr)
heap_sort(arr)
print("Sorted Array:", arr)