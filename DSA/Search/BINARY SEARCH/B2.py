# ====================== BINARY SEARCH ======================
def binary(array, target):
    # Initialize pointers to the start and end of the array
    left, right = 0, len(array) - 1
    
    # Loop continues as long as the search space is valid
    while left <= right:
        # Find the middle index using floor division
        mid = (left + right) // 2
        
        # Check if the target is found at the middle index
        if array[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif array[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
            
    # Return -1 if the target element is not present in the array
    return -1


# ------------------- Example Usage -------------------
# The input array MUST be sorted for binary search to work
sample_array = [10, 20, 30, 40, 50]
search_target = 40

# Execute the function
result_index = binary(sample_array, search_target)

# Display the result
if result_index != -1:
    print(f"Success: Element {search_target} found at index {result_index}.")
else:
    print(f"Result: Element {search_target} is not in the array.")
















# def binary(array, target):
#     left, right = 0, len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1