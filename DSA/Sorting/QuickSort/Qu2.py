# ---------------- QUICK SORT PROGRAM ----------------

# Function to partition the array
def partition(arr, low, high):
    pivot = arr[high]   # Choosing last element as pivot
    i = low - 1         # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        # Find pivot position
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ---------------- MAIN PROGRAM ----------------

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("\nOriginal List:", numbers)

quick_sort(numbers, 0, len(numbers) - 1)

print("Sorted List:", numbers)
