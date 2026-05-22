def counting_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Find the maximum element
    max_val = max(arr)
    
    # Step 2: Create count array of size max_val + 1
    count = [0] * (max_val + 1)
    
    # Step 3: Count frequency of each element
    for num in arr:
        count[num] += 1
    
    # Step 4: Reconstruct the sorted array
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
    
    return arr


# ============== Example Usage ==============
arr = [64, 32, 25, 12, 22, 11, 90, 25, 12]
print("Original Array:", arr)

counting_sort(arr)
print("Sorted Array:", arr)


'''
Time Complexity AnalysisCase
Time Complexity
Explanation
Best
O(n + k)
Where k = range of input
Average
O(n + k)
Linear
Worst
O(n + k)
Linear

If k (maximum value) is not too large, we say Time Complexity ≈ O(n)

Space Complexity: O(n + k)
'''
