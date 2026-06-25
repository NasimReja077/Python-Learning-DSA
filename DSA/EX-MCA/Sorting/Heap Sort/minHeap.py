def min_heapify(arr, n, i):
    smallest = i          # Assume current node is smallest
    left = 2 * i + 1      # Left child
    right = 2 * i + 2     # Right child

    # If left child is smaller than root
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # If right child is smaller than smallest
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not root, swap and continue
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)   # Recur for affected subtree


def build_min_heap(arr):
    n = len(arr)
    
    # Start from the last non-leaf node and go up to root
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)
    
    return arr


# ================== Example Usage ==================
arr = [64, 32, 25, 12, 22, 11, 90]

print("Original Array:", arr)
build_min_heap(arr)
print("Min Heap:", arr)