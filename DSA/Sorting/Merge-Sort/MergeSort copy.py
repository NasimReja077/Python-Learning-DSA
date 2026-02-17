def Divide(arr, l, r): # l is left index and r is right index of the sub-array of arr to be sorted, initially, l = 0 and r = n-1 where n is the size of the array.
    if (l < r): # Base case: If the left index is less than the right index, we need to sort, otherwise, the array is already sorted, so we return.
        m = (l + r) // 2 # Find the middle point to divide the array into two halves, we can also use m = l + (r - l) // 2 to avoid overflow when l and r are large.
        Divide(arr, l, m) # Recursively call Divide on the left half of the array, which is from index l to m.
        Divide(arr, m + 1, r) # Recursively call Divide on the right half of the array, which is from index m + 1 to r.
        merge(arr, l, m, r) # After the two halves are sorted, we need to merge them together, so we call the merge function with the original array and the left, middle, and right indices.

# Function to merge two halves of the array, the first half is from index l to m and the second half is from index m + 1 to r.
def merge(arr, l, m, r): # We need to create temporary arrays to hold the two halves of the array, and then we will merge them back into the original array. 
    s1 = m - l + 1 # Size of the first half of the array, which is from index l to m, so the size is m - l + 1.
    s2 = r - m # Size of the second half of the array, which is from index m + 1 to r, so the size is r - m.

    L_list = [0] * s1 # Create a temporary array to hold the first half of the array, we initialize it with zeros and the size is s1.
    R_list = [0] * s2 # Create a temporary array to hold the second half of the array, we initialize it with zeros and the size is s2.

# why use for loop i, j here? because we need to copy the elements of the two halves of the array into the temporary arrays L_list and R_list, we will use for loops to iterate through the elements of the original array and copy them into the temporary arrays, we will start from index l and go to index m for the first half, and we will start from index m + 1 and go to index r for the second half.

    for i in range(s1): # Copy the elements of the first half of the array into the temporary array L_list, we start from index l and go to index m, so we use l + i to get the correct index in the original array.
        L_list[i] = arr[l + i] # Copy the element at index l + i from the original array into the temporary array L_list at index i.
    
    for j in range(s2): # Copy the elements of the second half of the array into the temporary array R_list, we start from index m + 1 and go to index r, so we use m + 1 + j to get the correct index in the original array.
        R_list[j] = arr[m + 1 + j] # Copy the element at index m + 1 + j from the original array into the temporary array R_list at index j.

    i = j = 0 # Initialize the indices for the temporary arrays L_list and R_list, we will use these indices to keep track of the current position in the temporary arrays while merging them back into the original array.
    k = l # Initialize the index for the original array, we will use this index to keep track of the current position in the original array while merging the two halves back together.

     # Merge the two halves of the array back together, we will compare the elements of the two temporary arrays and copy the smaller element into the original array, we will continue this process until we have copied all the elements from both temporary arrays back into the original array.
    while (i < s1 and j < s2): # We will continue this process until we have copied all the elements from both temporary arrays back into the original array, so we will check if we have reached the end of either temporary array, if we have reached the end of one temporary array, we will copy the remaining elements from the other temporary array into the original array.
        if (L_list[i] < R_list[j]):
            arr[k] = L_list[i] # Copy the element at index i from the temporary array L_list into the original array at index k, because it is smaller than the element at index j from the temporary array R_list.
            i = i + 1
            k = k + 1
        else:
            arr[k] = R_list[j]
            j = j + 1
            k = k + 1

     # Copy the remaining elements of the temporary array L_list, if there are any, into the original array, we will continue this process until we have copied all the elements from the temporary array L_list back into the original array.
     # why use while loop here? because we need to check if there are any remaining elements in the temporary array L_list, if there are, we need to copy them into the original array, we will continue this process until we have copied all the elements from the temporary array L_list back into the original array.
    while (i < s1): 
        arr[k] = L_list[i]
        i = i + 1
        k = k + 1
     # Copy the remaining elements of the temporary array R_list, if there are any, into the original array, we will continue this process until we have copied all the elements from the temporary array R_list back into the original array.
    while (j < s2):
        arr[k] = R_list[j]
        j = j + 1
        k = k + 1

# Driver code
arr = [21, 45, 24, 89, 7, 5, 10]
Divide(arr, 0, len(arr) - 1)
print(arr)