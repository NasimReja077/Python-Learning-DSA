# arr = array
# n = heap size
# i = current root node index

def heapify(arr, n, i):
    largest = i # Initially assume current root node is largest. Ex- i = 0 | Lar=0 | arr[0] = 64 
    left = 2 * i + 1 # Left child formula - 2*i + 1 (For any node i)
    right = 2 * i + 2 # Right child formula - 2*i + 2

    # Check if left child exists and is greater than root
    # Check left child
    # This has TWO checks.
    # left < n Why? -> To avoid going outside array.
    # Example: If: |left = 10 | n = 7 | 10 < 7 = False -> So index doesn't exist.
    
    # arr[left] > arr[largest] | Why? -> To see if left child is bigger. then we will update largest to left. Ex- Left = 32 | Lar = 64 | then compar - 32 > 64 -> False | So Largest remains 0. | Left = 90 | lar = 64 then compar - 90 > 64 -> True | so Lar = left | Now Lar becomes 1. | So we will update Largest to Left.
    # tree look like this:
    #          64
    #        /    \
    #      32     25
    #     / \    / \
    #    12  22 11  90
     
    #       90
    #       /  \
    #     32    25
    #   /    /  \   /
    # 12   22  11  64
    
     
    # arr[left] = 90 | arr[largest] = 25
    # 90 > 25 | True.
    # So: largest = left | -> Now 90 becomes largest.
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check right child
    
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    # If root isn't biggest, swap.
    # largest != i mens Largest is not root then we will swap. with top element. Ex- Largest = 90 | i = 0 | So we will swap 90 with 64. | After swap: 90 becomes root and 64 becomes left child.
    if largest != i: # i mins curent root node index. ex- i=0 | largest = 1 | So we will swap arr[0] with arr[1]
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) # why largest ? -> after swap, largest becomes new root. So we need to heapify from largest index.


def heap_sort(arr):
    n = len(arr)
    
    # Step 1: Build Max Heap
    # Why n // 2 - 1 ?
    # Leaf nodes don't need heapify.Only parent nodes need heapify.
    # Formula for last parent: n // 2 - 1
    # For n = 7:
    # 7//2 -1 | = 3 -1 | = 2 | -> So last parent index = 2.
    # Indexes: -> 0,1,2 = parents 
    #          -> 3,4,5,6 = leaves
    # So loop starts from: -> i = 2
    # Why go backward? -> range(2, -1, -1) | 2,1,0 | We fix bottom parents first. | Then upper parents.
    # Why -1, -1 ? -> To go backward. | If we do range(0, n//2 - 1) | 0,1 | We will only fix upper parents. | So we will end up with an incorrect heap.
    # range(start, stop, step)
    # this loop use for building max heap. So we will start from last parent and go up to root. | So we will fix bottom parents first. | Then upper parents.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Step 2: Extract elements one by one
    # n-1 why because we are swapping root with last element. So after first swap, last element is in correct position. So we will reduce heap size by 1.
    # this loop is for sorting. So we will swap root with last element. Then we will heapify reduced heap. So we will fix heap after every swap.
    for i in range(n - 1, 0, -1): # n-1 is the last index, 0 is the first index, -1 to go backward
        arr[0], arr[i] = arr[i], arr[0]   # Swap root with last
        heapify(arr, i, 0) # Heapify reduced heap # 0 because we need to heapify from root after swap
    
    return arr


# Example Usage
arr = [64, 32, 25, 12, 22, 11, 90]
print("Original Array:", arr)
heap_sort(arr)
print("Sorted Array:", arr)