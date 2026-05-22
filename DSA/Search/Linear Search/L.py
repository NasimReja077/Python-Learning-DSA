# ====================== LINEAR SEARCH ======================
def linear_search(arr, key):
    """
    Linear Search Function
    Returns index of key if found, else -1
    """
    for i in range(len(arr)):
        if arr[i] == key:
            return i          # Element found
    return -1                 # Element not found


# ------------------- Example Usage -------------------
arr = [64, 25, 12, 22, 11, 45, 90, 77, 33]
key = 22

result = linear_search(arr, key)

if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the array")