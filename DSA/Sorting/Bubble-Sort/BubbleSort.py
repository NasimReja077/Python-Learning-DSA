# # Function to perform Bubble Sort
# def bubble_sort(arr):
#     n = len(arr)   # total number of elements

#     # Outer loop for number of passes
#     for i in range(n - 1):
        
#         # Inner loop for comparison
#         for j in range(0, n - 1 - i):

#             # Swap if current element is greater than next element
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#     return arr


# # -------- Example Usage --------
# arr = [64, 34, 25, 12, 22, 11, 90]

# print("Original Array:", arr)

# bubble_sort(arr)

# print("Sorted Array:", arr)





def bubbleSort(arr):
    n = len(arr) # total number of elements

    # Outer loop for number of passes
    for i in range(n): # This controls the number of passes.
        
        # Inner loop for comparison
        for j in range(0, n-1-i): # This avoids checking already sorted elements at the end. // j = Current element.
            
            # Swap if current element is greater than next element
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [64,32,25,45,40,51,2]
print("Original Array:", arr)
bubbleSort(arr)
print("Sorted Array:", arr)
# print(arr) 
