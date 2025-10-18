# Creating Strings
str1 = "Nasim Reja"
str2 = "Hellow world"
print(str1)
print(str2)

# Using Quotes:Single quotes: 'Hello'
# Double quotes: "Hello"
# Use single quotes inside double quotes or vice versa for nested strings: "He said, 'Hello'" or 'He said, "Hello"'

# Triple Quotes:Used for multiline strings or docstrings.
# Multiline Strings
str3 = """This is a multiline string.
It can span multiple lines.
You can include line breaks and tabs."""
print(str3)

# Using str() Constructor:
num = 102
s = str(num)
print(s)


# String Indexing
str4 = "Python"
print(str4[0])  # Output: P
print(str4[3])  # Output: h
print(str4[-1]) # Output: n


# String Properties
# Immutable: You cannot change a string’s content after creation. For example:

s = "Hello"
# s[0] = 'h'  # This will raise TypeError: 'str' object does not support item assignment

# Indexed
s = "Python"
print(s[0])   # Output: P
print(s[-1])  # Output: n

s = "Hello"
print(len(s))

# Concatenation
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)


# Repetition
N = "LIFI"
print(N * 3)

# Membership Testing
# Check if a substring exists using in or not in.
s = "Hello, World!"
print("World" in s)    # Output: True
print("Python" in s)   # Output: False

# Slicing
s = "Pyhthon Knolg"
print(s[0:6])
# print([7:])
print(s[::-1])

# Common String Methods
# Case Conversion

s = "hello world"
print(s.upper())      # Output: HELLO WORLD
print(s.lower())      # Output: hello world
print(s.title())      # Output: Hello World
print(s.capitalize()) # Output: Hello world

# Searching and Replacing
s = "Hello, World!"
print(s.find("World"))    # Output: 7
print(s.index("World"))   # Output: 7
print(s.replace("World", "Python"))  # Output: Hello, Python!
print(s.count("l"))       # Output: 3

# Stripping Whitespace
a = "  Hello  "
print(a.strip())   # Output: Hello
print(a.lstrip())  # Output: Hello  
print(a.rstrip())  # Output:   Hello

# Splitting and Joining
b = "apple,banana,orange"
print(b.split(","))  # Output: ['apple', 'banana', 'orange']
words = ['Hello', 'World']
print(" ".join(words))  # Output: Hello World

# Checking String Content
O = "Nasim123"
print(O.isalpha())    # Output: False
print(O.isalnum())    # Output: True
print(O.startswith("Na"))  # Output: True
print(O.endswith("123"))   # Output: True

# Formatting Strings
name = "Nasim"
print("Hello,")

# Using % operator (old style):python

name = "Alice"
print("Hello, %s!" % name)  # Output: Hello, Alice!

# Using str.format():python

print("Hello, {}!".format(name))  # Output: Hello, Alice!

# Using f-strings (Python 3.6+):python

print(f"Hello, {name}!")  # Output: Hello, Alice!

# Using str.join() for concatenation:python

print(" ".join(["Hello", name + "!"]))  # Output: Hello Alice!

