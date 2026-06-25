# ====================== BINARY SEARCH ======================
def binary_search(arr, target):
    # n = len(arr)
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid                    # Element found
        elif arr[mid] < target:
            left = mid + 1                 # Search in right half
        else:
            right = mid - 1                # Search in left half
    
    return -1                             # Element not found


# ------------------- Example Usage -------------------
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 89]   # Sorted Array
target = 23

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")