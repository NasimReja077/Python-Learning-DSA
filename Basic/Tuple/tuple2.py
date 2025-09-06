# Creating TuplesTuples can be created in several ways:
# Using Parentheses:

my_tuple = (1, 2, 3)

# Without Parentheses (Tuple Packing):

my_tuple = 1, 2, 3

# Single-Element Tuple (requires a trailing comma):

single_tuple = (42,)  # Without comma, (42) is just an integer

# Empty Tuple:python

empty_tuple = ()

# Using the tuple() Constructor:

my_tuple = tuple([1, 2, 3])  # Converts a list to a tuple

# Accessing Tuple ElementsIndexing: Access elements using their index.

my_tuple = (10, 20, 30)
print(my_tuple[0])  # Output: 10
print(my_tuple[-1])  # Output: 30 (negative indexing)

# Slicing: Extract a range of elements.

print(my_tuple[1:3])  # Output: (20, 30)

# Unpacking: Assign tuple elements to variables.

a, b, c = my_tuple
print(a, b, c)  # Output: 10 20 30

# Immutability in Detail

# Tuples are immutable, meaning you cannot modify their elements directly:

# my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Error: TypeError: 'tuple' object does not support item assignment

# However, if a tuple contains a mutable object (e.g., a list), you can modify the contents of that object:

my_tuple = (1, [2, 3], 4)
my_tuple[1][0] = 20  # Modifies the list inside the tuple
print(my_tuple)  # Output: (1, [20, 3], 4)

#------------------------------
# Common Tuple OperationsLength: Get the number of elements using len().

my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

# Concatenation: Combine tuples using +

tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4)

# Repetition: Repeat a tuple using *

print(tuple1 * 2)  # Output: (1, 2, 1, 2)

# Membership Testing: Check if an element exists using in. 
print(2 in my_tuple)  # Output: True



# Counting Elements: Use count() to count occurrences of an element.
my_tuple = (1,2,6,7,1,2,8,2)
print("Counting Elements:",my_tuple.count(2))

# Finding Index: Use index() to get the index of an element.
print(my_tuple.index(7))

# Tuple Packing and Unpacking
# Packing: Creating a tuple by grouping values.

my_tuple = 1, 2, 3  # Packing

# Unpacking: Assigning tuple elements to variables.

a, b, c = my_tuple  # Unpacking
print(a, b, c)  # Output: 1 2 3

# Extended Unpacking: Using * to capture multiple elements.

my_tuple = (1, 2, 3, 4, 5)
first, *middle, last = my_tuple
print(first, middle, last)  # Output: 1 [2, 3, 4] 5


# Nested Tuples
# Tuples can contain other tuples, enabling complex data structures:

nested_tuple = (1, (2, 3), 4)
print(nested_tuple[1])  # Output: (2, 3)
print(nested_tuple[1][0])  # Output: 2

# Performance and Memory Considerations

# Tuples are faster than lists for iteration and access because they are immutable, reducing overhead.
# Tuples use less memory than lists:

import sys
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
print(sys.getsizeof(my_tuple))  # Output: Smaller size 64
print(sys.getsizeof(my_list))   # Output: Larger size 88



# Tuple MethodsTuples have only two built-in methods due to their immutability:

# count(x): Returns the number of times x appears in the tuple.
# index(x): Returns the index of the first occurrence of x.


# Tuple Operations

'''
Tuple Methods in PythonSince tuples are immutable, they don’t support methods that modify their contents (like append, remove, or pop, which are available for lists). The two available methods are:

> count(x)
> index(x[, start[, end]])

count(x)Description: Returns the number of times a specified element x appears in the tuple.
Syntax: tuple.count(x)
Parameters:x: The element to count (can be of any data type).

Return Value: An integer representing the number of occurrences of x.
Use Case: Useful when you need to know how many times a specific value appears in a tuple.
Time Complexity: O(n), where n is the length of the tuple, as it scans the entire tuple.

my_tuple = (1, 2, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 3
print(my_tuple.count(5))  # Output: 0 (element not found)

Example 2: Counting Complex Elementspython

my_tuple = ("apple", "banana", "apple", (1, 2), "apple")
print(my_tuple.count("apple"))  # Output: 3
print(my_tuple.count((1, 2)))   # Output: 1


Edge CasesEmpty Tuple:python

empty_tuple = ()
print(empty_tuple.count(1))  # Output: 0

Non-Existent Element:python

my_tuple = (1, 2, 3)
print(my_tuple.count(4))  # Output: 0

Case Sensitivity for Strings:python

my_tuple = ("Apple", "apple")
print(my_tuple.count("apple"))  # Output: 1 (case-sensitive)

Practical NotesThe count() method is case-sensitive for strings and exact-match for other types.
It works with any data type (integers, strings, tuples, etc.), as long as the element is present in the tuple.
If you need to count elements conditionally (e.g., strings longer than 3 characters), you’d need to use a loop or comprehension, as count() only matches exact values.

'''

'''
index(x[, start[, end]])Description: Returns the index of the first occurrence of a specified element x in the tuple. Raises a ValueError if the element is not found.
Syntax: tuple.index(x[, start[, end]])
Parameters:x: The element to find.
start (optional): The index to start searching from (inclusive).
end (optional): The index to stop searching at (exclusive).

Return Value: An integer representing the index of the first occurrence of x.
Use Case: Useful for finding the position of an element in a tuple.
Time Complexity: O(n), where n is the length of the tuple (or the slice being searched).

Example 1: Basic Usagepython

my_tuple = (10, 20, 30, 20, 40)
print(my_tuple.index(20))  # Output: 1 (first occurrence)

Example 2: Using start and endpython

my_tuple = (10, 20, 30, 20, 40)
print(my_tuple.index(20, 2))      # Output: 3 (starts searching from index 2)
print(my_tuple.index(20, 2, 4))   # Output: 3 (searches between index 2 and 3)

Example 3: Complex Elementspython

my_tuple = ("apple", "banana", (1, 2), "apple")
print(my_tuple.index((1, 2)))  # Output: 2

Edge CasesElement Not Found:python

my_tuple = (1, 2, 3)
print(my_tuple.index(4))  # Raises ValueError: tuple.index(x): x not in tuple

Empty Tuple:python

empty_tuple = ()
print(empty_tuple.index(1))  # Raises ValueError

Invalid start or end Indices:python

my_tuple = (1, 2, 3)
print(my_tuple.index(2, 5))  # Raises ValueError (index out of range)

Practical NotesThe index() method only returns the first occurrence. To find all occurrences, you’d need to iterate over the tuple.
Use start and end parameters to narrow the search range, which can be useful for large tuples or nested data.
Always handle potential ValueError exceptions using try-except when the element might not exist.

Example with Exception Handlingpython

my_tuple = (1, 2, 3)
try:
    print(my_tuple.index(4))
except ValueError:
    print("Element not found")  # Output: Element not found

Limitations of Tuple MethodsOnly Two Methods: Due to immutability, tuples lack methods like append(), remove(), or sort() that are available for lists.
No Modification: You cannot add, remove, or change elements, so methods are limited to querying (counting or finding indices).
Workarounds: For more complex operations (e.g., filtering, sorting), convert the tuple to a list, perform the operation, and convert back to a tuple if needed:python

my_tuple = (3, 1, 2)
sorted_tuple = tuple(sorted(my_tuple))  # Output: (1, 2, 3)


'''