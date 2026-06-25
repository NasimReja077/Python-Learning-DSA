# Selection Sort Program

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):

        # Assume the current position holds the minimum element
        min_index = i

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n): # range(start, stop)
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# -------- Main Program --------
numbers = [64, 25, 12, 22, 11]

print("Original Array:", numbers)

selection_sort(numbers)

print("Sorted Array:", numbers)

#================================================================================================
#================================================================================================

"""
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Taking input
arr = list(map(int, input("Enter elements separated by space: ").split()))

sorted_array = selection_sort(arr)

print("Sorted Array:", sorted_array)

"""