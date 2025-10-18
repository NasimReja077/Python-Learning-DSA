# What is Exception Handling?

# Exception Handling is a way to handle runtime errors gracefully — instead of crashing the program, you can control what happens when an error occurs.

# Basic Example of Exception Handling
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
     # Code to handle the exception
     print("Error: Cannot divide by zero.")
else:
     # Code to execute if no exception occurs
     print("Result:", result)
finally:
     # Code that will always execute
     print("Execution completed.")
# In this example:
# - The code inside the try block attempts to divide 10 by 0, which raises a ZeroDivisionError.
# - The except block catches the ZeroDivisionError and prints an error message.
# - The else block would execute if no exception occurred (not in this case).
# - The finally block always executes, regardless of whether an exception occurred or not.

# You can handle multiple exceptions by specifying multiple except blocks:
try:
     value = int(input("Enter a number: "))
     result = 10 / value
except ValueError:
     print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
     print("Error: Cannot divide by zero.")
else:
     print("Result:", result)
finally:
     print("Execution completed.")
# This code handles both ValueError (if the input is not an integer) and ZeroDivisionError (if the input is zero).

# else: → Runs only if no error occurs.
# finally: → Runs no matter what, even if there’s an error (useful for closing files).
# Raising Custom Exceptions
x = int(input("Enter a Age:"))
if x < 0:
     raise ValueError("Age cannnot be negative")
else:
     print("Valid age")

# Program to divide two numbers with complete exception handling
try:
     a = int(input("Enter 1st Number:"))
     b = int(input("Enter 2nd Number:"))
     print("Result:", a/b)
except ValueError:
     print("Enter Only Integer")
except ZeroDivisionError:
     print("Division by zero is not allowed")
else:
     print("Division successful")
finally:
     print("Program ended")

# Raising an Exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return f"Age {age} is valid."
try:
    print(check_age(16))
except ValueError as e:
    print(f"Error: {e}")
    
def read_file(filename):
    try:
        with open(filename, 'r') as file:  # Using 'with' ensures automatic file closure
            content = file.read()
            print("File contents:", content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

read_file("nonexistent.txt")
# You can also use a generic except block to catch any exception: