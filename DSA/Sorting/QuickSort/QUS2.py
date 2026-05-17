def QuickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)

        QuickSort(arr, l, p - 1)
        QuickSort(arr, p + 1, r)


def partition(arr, l, r):

    pivot = arr[r]   # Last element as pivot

    i = l            # Left pointer
    j = r - 1        # Right pointer

    while True:

        # Move i right until element > pivot
        while i <= j and arr[i] < pivot:
            i += 1

        # Move j left until element < pivot
        while i <= j and arr[j] > pivot:
            j -= 1

        # Swap misplaced elements
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    # Put pivot in correct position
    arr[i], arr[r] = arr[r], arr[i]

    return i


arr = [23, 45, 12, 65, 34, 10, 3]

QuickSort(arr, 0, len(arr) - 1)

print(arr)