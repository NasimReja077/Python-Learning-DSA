def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # element mil gaya

    return -1   # element nahi mila


# Example
numbers = [10, 25, 30, 45, 50]
key = 30

result = linear_search(numbers, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
