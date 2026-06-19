def heapify(arr, n, i):
    largest = i # i is current root node
    left = 2 * i + 1 # Left child formula - 2*i + 1 (For any node i)
    right = 2 * i + 2 # Left child formula - 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left    
    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) 
        
def heap_sort(arr):
    n = len(arr)
     # Step 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i) # why n, i ? -> n is heap size and i is current root node index. We are building max heap from last parent to root. So we will call heapify for each parent node starting from last parent to root.
    
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # why 0, i ? -> 0 is root node index and i is last element index. We are swapping root with last element. So we will call heapify for reduced heap after swap. So we need to pass reduced heap size and root index to heapify.
    return arr

# Example Usage
arr = [64, 32, 25, 12, 22, 11, 90]
print("Original Array:", arr)
heap_sort(arr)
print("Sorted Array:", arr)