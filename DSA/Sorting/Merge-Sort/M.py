# Function to perform Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2       # Find the middle point
        left = arr[:mid]          # Left half
        right = arr[mid:]         # Right half

        # Recursive call on both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# -------- Example Usage --------
arr = [38, 27, 43, 3, 9, 82, 10]

print("Original Array:", arr)
merge_sort(arr)
print("Sorted Array:", arr)
