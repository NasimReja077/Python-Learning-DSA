# Insertion Sort Program

def insertion_sort(arr):
    n = len(arr)   # length of array

    # Traverse from 1 to n-1
    for i in range(1, n):

        key = arr[i]     # Element to be inserted
        j = i - 1        # Index of previous element

        # Move elements of arr[0..i-1] 
        # that are greater than key 
        # to one position ahead
        # j >= 0 because we need to check all elements before key.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element one position to the right
            j = j-1 # Move to the previous elemennt

        arr[j + 1] = key   # Insert key at correct position # 

    return arr


# -------- Example Usage --------
arr = [64, 32, 25, 12, 22, 11, 2]

print("Original Array:", arr)
insertion_sort(arr)
print("Sorted Array:", arr)
