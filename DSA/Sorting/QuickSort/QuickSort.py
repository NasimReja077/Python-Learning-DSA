def QuickSort(arr, l, r):
    if( l < r ):
        p = partition(arr, l, r)

        QuickSort(arr, l, p-1) # why p-1
        QuickSort(arr, p+1, r)

def partition(arr, l, r):
    pivot = arr[l] # Selects the first element as pivot (common but not the safest choice).
    i = l + 1 #  Left pointer starts just after pivot.
    j = r # Right pointer starts at the end

    while True:
        while( i <= j and arr[i] < pivot): # Move i to the right until we find an element ≥ pivot (or i > j).
            i = i + 1
        
        while( i <= j and arr[j] > pivot): # Move j to the left until we find an element ≤ pivot (or i > j).
            j = j - 1
        
        # If i is still left of j, swap the two misplaced elements.
        # If i >= j, pointers have crossed → break the loop.

        if( i < j ):
            # Swap arr[i] and arr[j] to correct their positions relative to the pivot.
            arr[i], arr[j] = arr[j], arr[i] 
        else:
            break
    
    arr[l], arr[j] = arr[j], arr[l] # Finally, swap the pivot (at position l) with element at j.
    # why l and j ? -> l is the index of pivot and j is the index of last element in left partition. 
    # So we will swap pivot with last element in left partition. So pivot will be in correct position.
    return j

arr = [23, 45, 12, 65, 34, 10, 3]
QuickSort(arr, 0, len(arr)-1)
print("QuickSort: ", arr)