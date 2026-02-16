# ---------------- BUBBLE SORT PROGRAM ----------------

# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)  # Length of the array

    # Traverse through all elements
    for i in range(n - 1):

        # Flag to check if swapping happens
        swapped = False

        # Last i elements are already sorted
        for j in range(n - 1 - i):

            # Compare adjacent elements
            if arr[j] > arr[j + 1]:

                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        # If no swapping happens, array is already sorted
        if not swapped:
            break

    return arr


# ---------------- MAIN PROGRAM ----------------

# Taking input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("\nOriginal List:", numbers)

# Calling bubble sort function
bubble_sort(numbers)

print("Sorted List:", numbers)
