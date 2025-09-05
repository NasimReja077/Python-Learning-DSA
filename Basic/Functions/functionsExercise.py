# Create a function in Python
# def demo (name, age):
#      print(name, age)
# demo("Ben", 25)


# Create a function with variable length of arguments

# def func1(*args):
#   for arg in args:
#     print(arg)

# # Example calls to the function with different numbers of arguments
# func1(10, 20)
# func1("hello", 3.14, True)
# func1(1, 2, 3, 4, 5)
# func1() # Calling with no arguments


# Return multiple values from a function
# def calculate(a, b):
#     sum = a + b
#     product = a * b
    
#     # return multiple values separead by comama
#     return sum, product

# # get result in tuple format

# res = calculate(40, 50)
# print(res)  # Output: (90, 2000)


# def calculate(a, b):
#      return a+b , a-b

# add, sub = calculate(40, 20)
# print(add, sub)


# # Create a function with a default argument
# def show_employee(name, age=20): #< 
#      print("Name:", name, "Salary:", age)
     
# show_employee("Ben", 30)
# show_employee("Jessa")
# # show_employee(35, "Bob")


# Create an inner function

# outer function
# def outer_fun(a, b):
#     square = a ** 2

#     # inner function
#     def addition(a, b):
#         return a + b

#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5

# result = outer_fun(5, 10)
# print(result)



# Create a recursive function
# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num - 1)
#     else:
#         return 0

# res = addition(10)
# print(res)  # Output: 55 (10+9+8+7+6+5+4+3+2+1)


# Assign a different name to function and call it through the new name

# def display_student(name, age):
#     print(name, age)

# # call using original name
# display_student("Emma", 26)

# # assign new name
# showStudent = display_student
# # call using new name
# showStudent("Emma", 26)


# Generate a Python list of all the even numbers between 4 to 30
# print(list(range(4,31,2)))

# Find the largest item from list
# x =[2, 3, 4, 5, 10, 6]
# print(max(x))
# print(min(x))


# Call Function using both positional and keyword arguments

# def describe_pet(animal_type, pet_name):
#   print(f"\nI have a {animal_type} named {pet_name}.")

# # Calling the function using positional arguments
# describe_pet('hamster', 'Harry')
# describe_pet('dog', 'Lucy')

# # Calling the function using keyword arguments
# describe_pet(animal_type='cat', pet_name='Whiskers')
# describe_pet(pet_name='Buddy', animal_type='goldfish')

# Create a function with keyword arguments

# def print_info(**kwargs):
#      if kwargs:
#           print("\n ------ Information-------")
#           for key, value in kwargs.items():
#                print(f"{key}: {value}")
#      else:
#           print("\nNo information provided.")

# print_info(name="Ben", age=25, city="New York")
# print_info(job="Engineer", salary=70000)
# print_info(country="USA", state="California", zip_code="90001")


# Modifies global variable
# global_var = 10
# def modify_global_var():
#      global global_var
#      global_var = 20
#      print("Inside function:", global_var)
     
# modify_global_var()
# print("Outside function:", global_var)


# Write a recursive function to calculate the factorial

def fun_rec(n):
     if n < 0:
          raise ValueError("Input must be a non-negative integer.")
     elif n == 0:
          return 1
     else:
          return n * fun_rec(n - 1)
     
number = 5
result = fun_rec(number)
print(f"The factorial of {number} is {result}")



def apply_operation(func, x, y):
  """
  Applies a given function to two numbers.

  Args:
    func: The function to apply (should take two arguments).
    x: The first number.
    y: The second number.

  Returns:
    The result of calling func(x, y).
  """
  return func(x, y)

# Demonstrate with addition using a regular function
def add(a, b):
  return a + b

result_add = apply_operation(add, 5, 3)
print(f"Result of addition: {result_add}")

# Demonstrate with subtraction using a lambda function
subtract = lambda a, b: a - b
result_subtract = apply_operation(subtract, 10, 4)
print(f"Result of subtraction: {result_subtract}")

# Demonstrate with multiplication using another lambda function
multiply = lambda a, b: a * b
result_multiply = apply_operation(multiply, 2, 6)
print(f"Result of multiplication: {result_multiply}")
     