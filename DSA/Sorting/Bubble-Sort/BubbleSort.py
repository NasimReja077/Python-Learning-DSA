# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)   # total number of elements

    # Outer loop for number of passes
    for i in range(n - 1):
        
        # Inner loop for comparison
        for j in range(0, n - 1 - i):

            # Swap if current element is greater than next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# -------- Example Usage --------
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:", arr)

bubble_sort(arr)

print("Sorted Array:", arr)




"""
def bubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-1-i):
            if(a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]

a = [64,32,25,45,40,51,2]
bubbleSort(a)
print(a) 
"""