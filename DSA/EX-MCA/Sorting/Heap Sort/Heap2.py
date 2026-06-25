def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    
    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # Swap max element to end
        heapify(arr, i, 0)                # Heapify reduced heap
    
    return arr


# Example Usage
if __name__ == "__main__":
    arr = [64, 32, 25, 12, 22, 11, 90]
    print("Original Array:", arr)
    
    sorted_arr = heap_sort(arr)
    print("Sorted Array :", sorted_arr)