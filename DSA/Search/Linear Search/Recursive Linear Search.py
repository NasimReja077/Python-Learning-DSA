def recursive_linear_search(arr, target, index=0):

    # Base Case 1: Agar list khatam ho gayi
    if index >= len(arr):
        return -1

    # Base Case 2: Agar element mil gaya
    if arr[index] == target:
        return index

    # Recursive Call
    return recursive_linear_search(arr, target, index + 1)


# Example
numbers = [5, 12, 7, 20, 15]
key = 20

result = recursive_linear_search(numbers, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


"""
Algorithm (Recursive Linear Search)

Function ko list, target aur index (default = 0) ke saath call karo

Agar index list ki length ke barabar ho jaye → return -1

Agar arr[index] == target → index return karo

Warna function ko dobara call karo with index + 1

End
     
| Case       | Complexity |
| ---------- | ---------- |
| Best Case  | O(1)       |
| Worst Case | O(n)       |

"""