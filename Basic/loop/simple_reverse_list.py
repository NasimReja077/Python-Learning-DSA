# Method 1: Using for loop with range
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
print("Reverse using for loop with range:")
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i], end=" ")
print()  # New line

# Method 2: Another way using for loop with list slicing
print("\nReverse using for loop with slicing:")
for item in numbers[::-1]:
    print(item, end=" ")
print()

# Example with a different list
fruits = ["apple", "banana", "orange", "grape", "mango"]
print("\nOriginal list:", fruits)
print("Reverse using for loop:")
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i], end=" ")
print()

"""
Let's break down the first method:

range(len(numbers)-1, -1, -1) means:
- Start: len(numbers)-1 (last index of list)
- Stop: -1 (go until before index 0)
- Step: -1 (count backwards)

For numbers = [1, 2, 3, 4, 5]:
- First iteration: i = 4, prints numbers[4] = 5
- Second iteration: i = 3, prints numbers[3] = 4
- Third iteration: i = 2, prints numbers[2] = 3
- Fourth iteration: i = 1, prints numbers[1] = 2
- Fifth iteration: i = 0, prints numbers[0] = 1
"""
