# Creating a List
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)

# Using list() Constructor
a = list((1,2,3,"Apple", 5.6))
print(a)
b = list("OMG")
print(b)


# Creating List with Repeated Elements
# We can use the multiplication operator * to create a list with repeated items.

a = [2]*5
b = [5]*3
print(a)
print(b)


# Accessing List Elements
a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1])
print(a[1:4])   # elements from index 1 to 3


'''
Adding Elements into List
We can add elements to a list using the following methods:

append(): Adds an element at the end of the list.
extend(): Adds multiple elements to the end of the list.
insert(): Adds an element at a specific position.
clear(): removes all items.
'''

a = []

a.append(10)  
print("After append(10):", a)  

a.insert(2, 5) # position, element
print("After insert(0, 5):", a) 

a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 

a.clear()
# print("After clear():", a)

# Updating Elements into List
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)
a[2] = 100
print(a)


'''
Removing Elements from List
We can remove elements from a list using:

remove(): Removes the first occurrence of an element.
pop(): Removes the element at a specific index or the last element if no index is specified.
del statement: Deletes an element at a specified index.
'''
a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  
print("After del a[0]:", a)

# Iterating Over Lists
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)

# Nested Lists
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][1])

# List Comprehension
# List comprehension is a concise way to create lists using a single line of code. It is useful for applying an operation or filter to items in an iterable, such as a list or range.

# Example: Creating a list of squares using list comprehension.

squares = [x**2 for x in range(1, 6)]
print(squares)

# Output
# [1, 4, 9, 16, 25]

# Explanation:
# for x in range(1, 6): loops through each number from 1 to 5 (excluding 6).
# x**2: squares each number x.
# [ ]: collects all the squared numbers into a new list

# https://www.geeksforgeeks.org/python/python-list-comprehension/
# https://www.geeksforgeeks.org/python/iterate-over-a-list-in-python/
