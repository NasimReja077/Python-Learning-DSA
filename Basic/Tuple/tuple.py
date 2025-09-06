'''
A tuple in Python is an immutable ordered collection of elements.

Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
Tuples can hold elements of different data types.
The main characteristics of tuples are being ordered , heterogeneous and immutable.
'''

tup = ()
print(tup)

tup = ("Nasim", "Reja")
print(tup)

#using list
li = [1,2,3,4,5]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)


# Creating a Tuple with Mixed Datatypes.

tup = (5, "Nasimo", 7, "Raju")
print(tup)

tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print("Mixed Datatypes Tuple : " , tup3)

# Creating a Tuple with repetition
tup1 = ("Nasimo", ) * 3
print("repetition",tup1)

# Creating a Tuple with the use of loop
tup = ("Nasim")
n = 5
for i in range(int(n)):
     tup = (tup,)
     # print(tup)
     
'''
Python Tuple Basic Operations
Below are the Python tuple operations.

Accessing of Python Tuples
Concatenation of Tuples
Slicing of Tuple
Deleting a Tuple

'''

# Accessing of Python Tuples
tup = tuple("NasimReja")

print(tup) # ('N', 'a', 's', 'i', 'm', 'R', 'e', 'j', 'a')
print(tup[0])

print(tup[1:4])
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

# Concatenation of Tuples

tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')

tup3 = tup1 + tup2
print(tup3)

# Slicing of Tuple

tup = tuple('GEEKSFORGEEKS')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])


# Define a tuple
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slice from index 2 to 5
s1 = tup[2:6]
print(s1)  

# Slice from the beginning to index 3
s2 = tup[:4]
print(s2)  

# Slice from index 5 to the end
s3 = tup[5:]
print(s3)  

# Slice the entire tuple
s4 = tup[:]
print(s4)


# Deleting a Tuple
tup1 = (0,1,3,5,6)
print("Befor delting:",tup1)
del tup1
# print("After delting:",tup1)


# List Slicing Using del Keyword

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete second element of 'a'
del a[1]
  
# check if the second element in 'a' is deleted
print(a)
  
# slice 'a' from index 3 to 5
del a[3:5]
  
# check if the elements from index 3 to 5 in 'a' is deleted
print(a)


# Deleting Dictionary and Removing key-value Pairs
d = {"small": "big", "black": "white", "up": "down"}
  
# delete key-value pair with key "black" from my_dict1
del d["black"]
  
# check if the  key-value pair with key "black" from d1 is deleted
print(d)



# Tuple Unpacking with Asterisk (*)
# In Python, the " * " operator can be used in tuple unpacking to grab multiple items into a list. This is useful when you want to extract just a few specific elements and collect the rest together.

tup = (1,2,3,4,5,6)
a,*b,c = tup
print(a)
print(b)
print(c)
