def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # element mil gaya

    return -1   # element nahi mila


# Example
numbers = [10, 25, 30, 45, 50]
key = 30

result = linear_search(numbers, key) # linear_search function ko call kar ke result variable me store kar liya.

if result != -1: # != -1 means element found
    print("Element found at index:", result)
else:
    print("Element not found")
