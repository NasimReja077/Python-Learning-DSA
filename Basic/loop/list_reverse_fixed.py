# Create original list
list1 = [10, 20, 30, 40, 50]

# Save original list using copy
before_reverse = list1.copy()

# Create a new list to store reversed elements
reversed_list = []

# Add elements in reverse order
for i in range(len(list1)-1, -1, -1):
    reversed_list.append(list1[i])

# OR to modify the original list, we can do:
list1.reverse()  # This actually reverses the list in-place

# Print both versions
print("Original list:", before_reverse)
print("Reversed list:", reversed_list)
print("Original list after reverse():", list1)

"""
Output will be:
Original list: [10, 20, 30, 40, 50]
Reversed list: [50, 40, 30, 20, 10]
Original list after reverse(): [50, 40, 30, 20, 10]
"""
