'''
List Methods
Let's look at different list methods in Python:

append(): Adds an element to the end of the list.
copy(): Returns a shallow copy of the list.
clear(): Removes all elements from the list.
count(): Returns the number of times a specified element appears in the list.
extend(): Adds elements from another list to the end of the current list.
index(): Returns the index of the first occurrence of a specified element.
insert(): Inserts an element at a specified position.
pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
remove(): Removes the first occurrence of a specified element.
reverse(): Reverses the order of the elements in the list.
sort(): Sorts the list in ascending order (by default).
'''


# append() method in Python is used to add a single item to the end of list. This method modifies the original list and does not return a new list. Let's look at an example to better understand this.

a = [2, 5, 6, 7]

# Use append() to add the element 8 to the end of the list
a.append(8)
print(a)

# Syntax of append() method
# list.append(element)

# Appending Elements of Different Types
a = [1, "Hellow", 3.25]
a.append(True)
print(a)


# Appending List to a List
a = [1,2,3]
a.append([4,5,6])
print(a)


# using Loop
a=[]
for i in range(5):
     a.append(i)
print(a)


# a = [1, 2, 3]
# a.append([4, 5])  
# print(a)  

# b = [1, 2, 3]
# b.extend([4, 5])  
# print(b)

# [1, 2, 3, [4, 5]]
# [1, 2, 3, 4, 5]

# Explanation:

# append([4,5]) adds [4,5] as a single element, creating a nested list ([1, 2, 3, [4, 5]]).
# extend([4,5]) adds each element separately, resulting in [1, 2, 3, 4, 5].

# Deep Copy and Shallow Copy in Python
'''
Deep copy in Python
A deep copy creates a new compound object before inserting copies of the items found in the original into it in a recursive manner.
It will first construct a new collection object and then recursively populate it with copies of the child objects found in the original. It means that any changes made to a copy of the object do not reflect in the original object. 
Syntax of Python Deepcopy
copy.deepcopy()
'''
import copy
a = [[1,2,3],[4,5,6]]
b = copy.deepcopy(a)
b[0][1] =90
print(b)
print(a)

'''
copy.deepcopy() method creates a completely independent copy of the original object, including all nested elements. Changes made to deep_copied do not affect the original list a.
nested elements of the original list a are recursively duplicated to ensure that even deeply nested objects are entirely independent in the copied list.
'''

'''
Shallow copy in Python
A shallow copy creates a new object but retains references to the objects contained within the original. It only copies the top-level structure without duplicating nested elements.
Changes made to a copy of an object do reflect in the original object. In python, this is implemented using the "copy.copy()" function. 
Syntax of Python Shallowcopy
copy.copy()
'''

import copy
a = [[1,2,3],[4,5,6]] 
# Creating a shallow copy of the nested list 'original'
print("Befor copy a :",a) 
b = copy.copy(a)
# Modifying an element in the shallow-copied list
b[0][0] = 50
print("After copy a :",a) # also chang
# Printing the original and shallow-copied lists
print("copy a to b : ",b)
'''
Explanation:

A shallow copy only copies the outer structure, retaining references to the nested objects. In this case, the inner lists are shared between original and shallow_copied.
As a result, changes to the nested elements in shallow_copied (e.g., modifying shallow_copied[0][0]) are also reflected in original.
'''
#----------------
# Python List clear() Method

# clear() method in Python is used to remove all elements from a list, effectively making it an empty list. This method does not delete the list itself but clears its content. It is a simple and efficient way to reset a list without reassigning it to a new empty list.

# Example:

a = [1, 2, 3]
# Clear all elements from the list 'a'
a.clear()
print(a) # []

# 1. Clearing a list of strings
# clear() method can be used to remove all elements from a list of strings, leaving it empty. This is helpful when we want to reuse the list later without creating a new reference.

a = ["Geeks", "for", "Geeks"]

# Clear all elements from the list 'a'
a.clear()
print(a)

# Clearing a nested list:
a = [[1, 2], [3, 4], [5, 6]]

# Clear all elements from the list 'a'
a.clear()
print(a)

# Reusing a List:
a = [10, 20, 30, 50]
a.clear()
print("Befor: ",a)
a.append(45)
print("after: ",a)

# Memory Optimization
a = [i for i in range(1_000_000)]

# Clear all elements from the list 'a'
a.clear()
print(a)

# List count() method
a = [1, 2, 3, 1, 2, 1, 4]

c = a.count(1)
print(c)

#  Lits Containing Different Datatypes
a = [1, 'GfG', 3.14, 'GfG', 1, True]

c1 = a.count('GfG')
c2 = a.count(1)

print(c1)
print(c2)

# Count occurrence of sub-list in list of Lists
a = [1, [2, 3], 1, [2, 3], 1]

c = a.count([2, 3])
print(c)

# Extend() Method
# Last Updated : 23 Jul, 2025
# In Python, extend() method is used to add items from one list to the end of another list. This method modifies the original list by appending all items from the given iterable.

# Using extend() method is easy and efficient way to merge two lists or add multiple elements at once.

# Let’s look at a simple example of the extend() method.

a = [1,2,3]
b = [4,5]
a.extend(b)
print(a)


# Using extend() with Different Iterables
# The extend() method can work with various types of iterables such as: Lists, Tuples, Sets and Strings (each character will be added separately)

# Example:

# Using a tuple
a = [1, 2, 3]
b = (4, 5)
a.extend(b)
print(a) 

# Using a set
a = [1, 2, 3]
b = {4, 5}
a.extend(b)
print(a)  

# Using a string
a = ['a', 'b']
b = "cd"
a.extend(b)
print(a)

# https://www.geeksforgeeks.org/python/extending-list-python-5-different-ways/
# https://www.geeksforgeeks.org/python/append-extend-python/
# https://www.geeksforgeeks.org/python/difference-between-append-extend-and-insert-in-python/
#----------------------------
# List insert() Method
# creating a list
fruit = ["banana","cherry","grape"]
fruit.insert(1,"apple")
print(fruit)

# List insert() Method Syntax
# list_name.insert(index, element)

# Parameters:
# index: the index at which the element has to be inserted.
# element: the element to be inserted in the list.

# making a list
score = [43,45,99,76]
#inserting a new score at third position
score.insert(2, 45)
#printing new list
print(score)

#  Inserting a Tuple into the List
# Here we are inserting a tuple in a list using the insert() function in Python.

list1 = [ 1, 2, 3, 4, 5, 6 ]
# tuple of numbers
num_tuple = (4, 5, 6)
# inserting a tuple to the list
list1.insert(2, num_tuple)
print(list1)


# Inserting a dictionary to a list in Python
my_list = [{'name': 'Alice', 'age': 30}, 
           {'name': 'Bob', 'age': 25}]
new_dict = {'name': 'Charlie', 'age': 40}

my_list.append(new_dict)

print(my_list)

# List remove() Method
a = ['a', 'b', 'c']
a.remove("b")
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [2, 4, 6]

for item in b:
    if item in a:
        a.remove(item)

print(a)

# List Reverse()
a = [1, 2, 3, 4, 1, 2, 6] 

a.reverse() 

print(a)

# Slicing Approach
a = [1, 2, 3, 4, 5]

res = a[::-1]
print(res)


'''
 List sort() Method
Last Updated : 11 Jul, 2025
The sort() method in Python is a built-in function that allows us to sort the elements of a list in ascending or descending order and it modifies the list in place which means there is no new list created. This method is useful when working with lists where we need to arranged the elements in a specific order, whether numerically or alphabetically.

Below is a simple example that use sort() method to arrange a list of integer values in ascending order.
'''

a = [5,2,6,8,9,3,1]
a.sort()
print("sort eliment is ",a)



# Syntax of sort() method
# list_name.sort(key=None, reverse=False)

# Parameter:

# key (Optional): This is an optional parameter that allows we to specify a function to be used for sorting. For example, we can use the len() function to sort a list of strings based on their length.
# reverse (Optional): This is an optional Boolean parameter. By default, it is set to False to sort in ascending order. If we set reverse=True, the list will be sorted in descending order.
# Return:

# Python list sort() returns none.


# Sorting List in descending order
# To sort a list in descending order, we need to set the reverse parameter to True.

a = [5, 2, 9, 1, 5, 6]
a.sort(reverse=True)# Sorting in Descending Order
print("list in descending order: ",a)

# using key parameter
a = ["apple", "banana", "kiwi", "cherry"]

# The key=len tells the sort() method
# to use length of each string during sorting
a.sort(key=len)
print(a)


# Sorting with a Custom Function

a = [(1, 3), (2, 2), (3, 1)]
def fun(val):
    return val[1]
a.sort(key=fun)
print(a)



a = ["apple", "banana", "kiwi", "cherry"]

a.sort(key=lambda x: x[-1])
print(a)


# Case Insensitive Sort
# By default, the sort() method is case sensitive, resulting in all capital letters being sorted before lowercase letters. To perform a case insensitive sort, we can use the str.lower function as the key.

a = ["Banana", "apple", "Grape", "pear"]
a.sort(key=str.lower)
print(a)
