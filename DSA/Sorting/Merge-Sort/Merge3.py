def merge_sort(arr):
    if len(arr) > 1:
        # 1. Divide: Find the middle and split using slicing
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # 2. Conquer: Recursive calls
        merge_sort(L)
        merge_sort(R)

        # 3. Combine: Merge the sorted halves
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check for any remaining elements
        arr[k:] = L[i:] if i < len(L) else R[j:]

# Driver code
arr = [21, 45, 24, 89, 7, 5, 10]
merge_sort(arr)
print(arr)