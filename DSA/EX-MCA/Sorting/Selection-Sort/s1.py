# ---------------- SELECTION SORT PROGRAM ----------------

# Function to perform Selection Sort
def selection_sort(arr):
    n = len(arr)  # Get the length of the array

    # Traverse through all array elements
    for i in range(n - 1):

        # Assume the current index has the minimum value
        min_index = i

        # Find the index of the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ---------------- MAIN PROGRAM ----------------

# Taking input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("\nOriginal List:", numbers)

# Calling selection sort function
selection_sort(numbers)

print("Sorted List:", numbers)
