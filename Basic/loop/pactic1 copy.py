# Write a Python program to swap the values of two variables without using a temporary variable

# a = 5
# b = 10
# a,b = b,a
# print(f"a = {a}, b = {b} ")

# -------------------------------

# Question: Type ConversionWrite a program that takes a string input representing a number (e.g., "123") and converts it to an integer, float, and complex number. Handle potential errors if the input is not a valid number.
# Example Input: "123"
# Example Output: Integer: 123, Float: 123.0, Complex: (123+0j)
# Hint: Use int(), float(), complex(), and a try-except block.

# try: 
#      user_input = input("Enter a number: ")
#      num = int(user_input)
#      result = num * 2 
#      print(f"Double of {num} is {result}")
# except ValueError: 
#      print("Error: Pleese enter a valid integer.")


# age = 25  # Integer
# price = 19.99  # Float
# name = "Alice"  # String
# is_student = True  # Boolean

# print(f"Type of age: {type(age)}")
# print(f"Type of price: {type(price)}")
# print(f"Type of name: {type(name)}")
# print(f"Type of is_student: {type(is_student)}")
     
# ====================================
# Question: String ManipulationCreate a program that takes a user’s full name as a string and prints:The name in uppercase.
# The length of the name.
# The first and last characters.

# Example Input: "John Doe"
# Example Output: Uppercase: JOHN DOE, Length: 8, First: J, Last: e

# text = input("Enter a string: ")
# print(f"Uppercase: {text.upper()}")
# print(f"Lowercase: {text.lower()}")
# print(f"Length: {len(text)}")
# if "World" in text:
#     print("The string contains 'World'.")
# else:
#     print("The string does not contain 'World'.")

# =========================================================

# Question: Data Type IdentificationWrite a program that defines variables of different types (e.g., integer, float, string, list, dictionary) and uses the type() function to print their data types.
# Example Output: 
# Variable 42 is of type <class 'int'>
# Variable 3.14 is of type <class 'float'>
# Variable hello is of type <class 'str'>


# try: 
#      score = float(input("Enter a score (0-100):"))
#      if 0 <= score <= 100:
#           if score >= 90:
#                grade = "A"
#           elif score >= 80:
#                grade = "B"
#           elif score >= 70:
#                grade = "C"
#           elif score >= 60:
#                grade = "D"
#           else:
#                grade = "F"
#           print(f"Your grade is {grade}")
#      else: 
#           print("Eroor: Score must be between 0 and 100.")
# except ValueError:
#      print("Error: Please a valid numbr")


# try:
#     num = int(input("Enter an integer: "))
    
#     if num > 0:
#         sign = "positive"
#     elif num < 0:
#         sign = "negative"
#     else:
#         sign = "zero"
    
#     if num % 2 == 0:
#         parity = "even"
#     else:
#         parity = "odd"
    
#     # Special case for zero, which is even but we avoid "zero and even" phrasing
#     if sign == "zero":
#         print(f"The number {num} is zero.")
#     else:
#         print(f"The number {num} is {sign} and {parity}.")
# except ValueError:
#     print("Error: Please enter a valid integer.")


# Question: Leap Year Checker

# try:
#     year = int(input("Enter a year: "))
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
# except ValueError:
#     print("Error: Please enter a valid integer.")



# Question: Factorial Calculator
n = int(input("Enter a positive integer: "))
if n< 0:
     print("Error")
else:
     factorial = 1
     counter = n
     while counter > 0:
          factorial *= counter
          counter -= 1
     print(f"The factoreal of {n} is {factorial}")
# Question: Fibonacci Sequence




