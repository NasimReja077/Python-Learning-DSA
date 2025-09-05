# username = "nasim"
# def func():
#      username = "reja" # when local valu not funt then use global valu // nasim // nasim
#      print(username)
# print(username) # Global valu
# func() # local valu

# --------------------
x = 15 # Global value
def fun(y):
     z = x + y
     return z
result = fun(5) # colling funtion
# print(result)


# -------------------
a = 20
def func():
     global a
     a = 10
func()
# print(a)

# -----------

# Python program to demonstrate
# nonlocal keyword

print("Value of a using nonlocal is : ", end="")


def outer():
    a = 5

    def inner():
        nonlocal a
        a = 10
    inner()
    print(a)


outer()

# demonstrating without non local
# inner loop not changing the value of outer a
# prints 5
print("Value of a without using nonlocal is : ", end="")


def outer():
    a = 5

    def inner():
        a = 10
    inner()
    print(a)


outer()
# --------------

# i = 5
# def fu1():
#      i = 20
#      def fu2():
#           print(i)
#      fu2()
# fu1()

# ---------closure-----------

i = 5
def fu1():
     i = 10
     def fu2():
          print(i) # funtion dafenation 
     return fu2 # return f2 rafarenche
myResult = fu1()
myResult() # exgecut using () # store mamore rafarenche # store

'''
1st call f1
then i deacre
then call f2 defenation
rerun full dafenation 
ten result exgequt

'''


def chaiCode(num):
     def actual(x):
          return x ** num
     return actual

f = chaiCode(2)
g = chaiCode(3)

print(f(3))
print(f(3))


def outer_function(x):
    # Outer function: takes 'x' and defines inner_function
    def inner_function(y):
        return x + y  # 'x' is remembered from outer_function
    return inner_function  # Returns inner function (closure)

# Create a closure with x = 10
closure = outer_function(10)

# Call the closure with different values of 'y'
print(closure(5)) 
print(closure(20))

# Explanation:

# outer_function(10) returns inner_function, but with x fixed at 10.
# This returned inner_function still has access to x even though outer_function has finished running.
# When you call closure(5), it adds x = 10 and y = 5.


# Example 3: This example shows how a closure can be used for string formatting, outer function stores a prefix and inner function automatically attaches that prefix to any given text.

def pre(p):
    # Outer function stores prefix
    def add(t):
        # Inner function uses stored prefix
        return p + " " + t
    return add  # Return closure

# Create a closure that always prefixes with "Hello"
h = pre("Hello")
print(h("World"))
print(h("Python"))

# Explanation:

# def pre(p): Defines outer function that takes a prefix p.
# def add(t): Defines inner function that takes some text t.
# return p + " " + t: Joins the prefix p with text t.
# h = pre("Hello"): Calls outer function with "Hello". Now h becomes a closure that remembers "Hello".
