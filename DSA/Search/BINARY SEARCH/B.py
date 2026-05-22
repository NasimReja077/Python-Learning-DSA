# ====================== BINARY SEARCH ======================
def binary_search(arr, key):
    """
    Binary Search Function (Array must be sorted)
    Returns index of key if found, else -1
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid                    # Element found
        elif arr[mid] < key:
            low = mid + 1                 # Search in right half
        else:
            high = mid - 1                # Search in left half
    
    return -1                             # Element not found


# ------------------- Example Usage -------------------
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 89]   # Sorted Array
key = 23

result = binary_search(arr, key)

if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the array")