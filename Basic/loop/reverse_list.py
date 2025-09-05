# Method 1: Using reversed() function with for loop
def reverse_list1(lst):
    print("Method 1: Using reversed()")
    for item in reversed(lst):
        print(item, end=" ")
    print()

# Method 2: Using range with negative step
def reverse_list2(lst):
    print("Method 2: Using range with negative step")
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end=" ")
    print()

# Method 3: Using while loop
def reverse_list3(lst):
    print("Method 3: Using while loop")
    index = len(lst) - 1
    while index >= 0:
        print(lst[index], end=" ")
        index -= 1
    print()

# Method 4: Using list slicing
def reverse_list4(lst):
    print("Method 4: Using list slicing")
    for item in lst[::-1]:
        print(item, end=" ")
    print()

# Test the methods with different types of lists
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
print("-" * 40)

reverse_list1(numbers)
reverse_list2(numbers)
reverse_list3(numbers)
reverse_list4(numbers)

# Test with a list of strings
fruits = ["apple", "banana", "orange", "mango"]
print("\nOriginal list:", fruits)
print("-" * 40)

reverse_list1(fruits)
reverse_list2(fruits)
reverse_list3(fruits)
reverse_list4(fruits)

# Note: If you want to actually reverse the list (not just print in reverse)
# You can use:
# 1. list.reverse() - modifies the original list
# 2. reversed_list = list(reversed(original_list)) - creates a new list
# 3. reversed_list = original_list[::-1] - creates a new list



