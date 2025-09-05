# 
# def fun():
#      print("Hello")

# fun()


# Even Odd
# def evenOdd(x):
#      if (x % 2 == 0):
#           return "Even"
#      else: 
#           return "Odd"
     
# print(evenOdd(10))
# print(evenOdd(5))

# Default Arguments
# def myfun(x, y=50):
#      print("x:", x)
#      print("y:", y)

# myfun(10)  # y will take the default value of 50
# myfun(10, 20)  # y will take the value of 20


# Keyword Arguments
# def studen(fname, lname):
#      print(fname, lname)     
# studen(lname="Doe", fname="John")  # Using keyword arguments
# studen(fname="Jane", lname="Smith")  # Using keyword arguments


# Positional Arguments
# def nameAge(name, age):
#      print("Hi I am", name)
#      print("My age is", age)
#      print("Nice to meet you!")
     
# print("Case-1:")
# nameAge("Nasim", 23)

# print("\nCase-2:")
# nameAge(25, "bob")

#----------------####------------
# Arbitrary Keyword  Arguments
# In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
# Example 1: Variable length non-keywords argument

# Arbitrary Keyword  Arguments
# def myFun(*argv):
#      for arg in argv:
#           print(arg)
# myFun("Hello", "Welcome", "to", "Python")


# Here's what's happening:

# def myFun(*argv):
# The asterisk * before the parameter argv makes it an arbitrary argument parameter
# This means the function can accept any number of positional arguments
# All arguments are packed into a tuple named argv
# for arg in argv:

# This loop iterates through each argument stored in the argv tuple
# Each argument is assigned to arg in each iteration
# print(arg):

# Prints each argument on a new line
# myFun("Hello", "Welcome", "to", "Python"):

# This calls the function with 4 string arguments
# These arguments are packed into the argv tuple
# When executed, it prints each word on a new line

# This is a powerful feature in Python that allows you to write functions that can handle a variable number of arguments. It's commonly used when you don't know in advance how many arguments will be passed to your function.

# Note: The name argv is just a convention (meaning "argument values"), you could use any valid variable name like *args which is another common convention.

# Example 2: Variable length keyword arguments
# def myFun(**kwargs):
#      for key, value in kwargs.items():
#           print("%s == %s" % (key, value))
# myFun(first='Geeks', mid='for', last='Geeks')


# def myFun(**kwargs):

# The double asterisk ** before kwargs allows the function to accept any number of keyword arguments
# These arguments are packed into a dictionary named kwargs
# Each argument will be a key-value pair in this dictionary
# for key, value in kwargs.items():

# kwargs.items() returns an iterable of the dictionary's key-value pairs
# The loop unpacks each pair into key and value variables
# print("%s == %s" % (key, value)):

# Prints each key-value pair using string formatting
# %s is replaced by the corresponding values in the parentheses
# myFun(first='Geeks', mid='for', last='Geeks'):

# Calls the function with three keyword arguments
# Creates a dictionary like: {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}

# Output:

# This is useful when:

# You need to pass a varying number of named arguments to a function
# You're writing a wrapper function that needs to pass through all keyword arguments to another function
# You don't know in advance what keyword arguments might be needed
# Note: The name kwargs is a convention (meaning "keyword arguments"), but you could use any valid variable name. However, the double asterisk ** is required syntax.

# --------------------#############------------
# Docstring
# The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.

# The below syntax can be used to print out the docstring of a function.
# Syntax: print(function_name.__doc__)

# # Example
# def evenOdd(x):
#     """Function to check if the number is even or odd"""
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")
# print(evenOdd.__doc__)


# # Closure in Python
# A closure is a function object that has access to variables in its lexical scope, even when the function is executed outside that scope.

# def f1():
#     s = 'I love GeeksforGeeks'
#     def f2():
#         print(s)
#     f2()
# f1()



# Anonymous Functions in Python
# In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

# def cube(x):  # with a normal function # without lambda
#      return x*x*x
# cube_1 = lambda x: x*x*x # with a lambda function
# print(cube(5))
# print(cube_1(5))


# Pass by Reference and Pass by Value
# In Python, all arguments are passed by reference. This means that when you pass a variable to a function, you are passing a reference to the object, not a copy of the object.
# However, the behavior can seem like "pass by value" for immutable objects (like integers, strings, and tuples) because you cannot change the original object.

# Recursive Functions in Python
# A recursive function is a function that calls itself in order to solve a problem.
# This technique is often used to solve problems that can be broken down into smaller, similar subproblems.

# # Example: Factorial Function
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# # Test the recursive function
# print(factorial(5))  # Output: 120


# def calculator(a, b):
#      add = a+b
#      return add
# res = calculator(5, 10)
# print("Addition : ", res)


# Global Variable

# global_var = 100
# def function1():
#      print("Value in 1st function: ", global_var)   

# def function2():
#     # Modify global variable
#     # function will treat it as a local variable
#     global_var = 555
#     print("Value in 2nd function :", global_var)

# def function3():
#     print("Value in 3rd function: ", global_var)
# function1()
# function2()
# function3()



# x = 5
# def function1():
#      print("Value in 1st function: ", x)
# def function2():
#      global x # Modify global variable using global keyword
#      x = 100
#      print("Value in 2nd function: ", x)
# def function3():
#     print("Value in 3rd function: ", x)
# function1()
# function2()
# function3()


# def outer_function():
#      x = 100
     
#      def inner_function():
#           nonlocal x  # local variable now acts as global variable
#           x = 700
#           print("Value in inner function: ", x)
          
#      inner_function()
#      print("Value in outer function: ", x)
     
# outer_function()

# In Python, nonlocal is the keyword used to declare a variable that acts as a global variable for a inner function (i.e., function within another function).


# def add(a, b):
#      print(a - b)
# add(10, 5)
# add(20, 10)


# def message(name, surname):
#     print("Hello", name, surname)

# message(name="John", surname="Wilson")
# message(surname="Ault", name="Kelly")



# def message(first_nm, last_nm):
#     print("Hello..!", first_nm, last_nm)

# # correct use
# message("John", "Wilson")
# message("John", last_nm="Wilson")

# # Error
# # SyntaxError: positional argument follows keyword argument
# message(first_nm="John", "Wilson")



# # function with default argument
# def message(name="Guest"):
#     print("Hello", name)

# # calling function with argument
# message("John")

# # calling function without argument
# message()


# # function with default argument
# def message(name="Guest"):
#     print("Hello", name)
# # calling function with argument
# message("John")
# # calling function without argument
# message()
# # Hello John
# # Hello Guest

# def addition(*numbers):
#      total = 0
#      for no in numbers:
#           total = total + no
#      print("Sum is:", total)
# addition()
# addition(10, 5, 2, 3, 4)
# addition(20, 5.6, 30)


def factorial(no):
     if no == 0:
          return 1
     else:
          return no * factorial(no - 1)
print("factorial of a number is: ",factorial(5))

def even_numbers(nums):
    even_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

num_list = [10, 5, 12, 78, 6, 1, 7, 9]
ans = even_numbers(num_list)
print("Even numbers are:", ans)


num_list = [10, 5, 12, 75, 50]
even_nos = list(filter(lambda x: x % 2 == 0, num_list))
print("Even numbers are:", even_nos)


# Syntax of filter() function:
# filter(function, sequence)
l = [-10, 5, 12, -78, 6, -1, -7, 9]
positive_nos = list(filter(lambda x: x > 0, l))
print("Positive numbers are: ", positive_nos)


# map() function in Python
# In Python, the map() function is used to apply some functionality for every element present in the given sequence and generate a new series with a required modification.

# Syntax of map() function:
# map(function,sequence)

list1 = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x*x, list1))
print("Squared numbers are: ", squared)



# reduce() function in Python
# In Python, the reduce() function is used to minimize sequence elements into a single value by applying the specified condition.

# The reduce() function is present in the functools module; hence, we need to import it using the import statement before using it.
# Syntax of reduce() function:
# reduce(function, sequence)


# from functools import reduce
# list1 = [10, 15, 20, 30]
# add = reduce(lambda x, y: x+y, list1)
# print("Addition of all list elements is : ", add)


