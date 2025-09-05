# Loop 25 Python Loop Coding Questions

# 1. Print numbers from 1 to 10 using a for loop:
# for num in range (1, 11):
#      print(num)
     
     
# Calculate the sum of numbers from 1 to 10 using a for loop:
# sum_number = 0
# for num in range(1, 11):
#      sum_number += num
# print(sum_number)

#Print the elements of a list using a for loop:
# my_list = [1,2,3,4,5]
# for element in my_list: 
#      print(element)


# Calculate the product of elements in a list using a for loop:
# my_list = [2,3,4,5]
# product = 1
# for num in my_list:
#      product *= num
# print(product)

# Print even numbers from 1 to 10 using a for loop:
# for num in range(2, 11, 2):
#      print(num)

# Explanation of Python CodeStep-by-Step BreakdownFor Loop with range():range(2, 11, 2): Generates a sequence of numbers starting at 2, stopping before 11, with a step size of 2.Start: 2 (the first number in the sequence).
# Stop: 11 (exclusive, so the sequence stops at 10).
# Step: 2 (increments by 2, giving even numbers: 2, 4, 6, 8, 10).

# The loop variable num takes each value in the sequence: 2, 4, 6, 8, 10.

# Body:print(num): Prints the current value of num on a new line.
# The loop iterates 5 times, printing:2 (when num = 2)
# 4 (when num = 4)
# 6 (when num = 6)
# 8 (when num = 8)
# 10 (when num = 10)

# Output:Each number is printed on a new line due to print()’s default behavior:

# 2
# 4
# 6
# 8
# 10

# Syntax of range()python

# range(start, stop, step)



# Print numbers in reverse from 10 to 1 using a for loop:
# for num in range (10, 0, -1):
#      print(num)
# for num in range (12, -2, -1):
#      print(num)

# Print characters of a string using a for loop:
# my_string = "Nasim"
# for char in my_string:
#      print(char)


# Find the largest number in a list using a for loop:
# my_list = [3, 9, 1, 6, 2, 8]
# largest = my_list[0]
# for num in my_list:
#      if num > largest:
#           largest = num
# print(largest)

# Find the average of numbers in a list using a for loop:
# my_list = [4,7,9,2,5]
# total = 0
# for num in my_list:
#      total+= num
# average = total/len(my_list)
# print (average)


# Print all uppercase letters in a string using a for loop:
# my_string = "Hello World"
# for char in my_string:
#     if char.isupper():
#         print(char)


# Count the number of vowels in a string using a for loop:
# my_string = "Hello World"
# vow = "aeiouAEIOU"
# count = 0
# for char in my_string:
#     if char in vow:
#         count += 1
# print(count)

# Print a multiplication table for a given number using a for loop:
# for i in range(7):
#     for j in range(i+1):
#         print(" * ", end=" ")
#     print()

# Print a right-angled triangle pattern using nested loops
# for i in range(1, 8):
#     for j in range(1, i+1):
#         print(" * ", end=" ")
#     print()
    
# Print a multiplication table for the given number
# num = int (input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "*", i, "=", num * i)

## Calculate the factorial of a number using a while loop:
# num = int ( input("Enter a number: "))
# factoreal = 1
# while num > 0:
#     factoreal *= num
#     num -= 1
# print(factoreal)

# Find the index of a specific element in a list using a while loop
# def find_element_index():
#     list = [3,9,2,1,4,7,5]
#     target = 7
#     index = 0
#     while index < len(list):
#         if list[index] == target:
#             print(f"Element {target} found at index {index}")
#             break
#         index += 1
#     else:
#         index = -1
#         print(f"Element {target} not found in the list, index: {index}")
# find_element_index()


# num = int(input("Enter a number: "))
# sum_of_number = 0
# while num <= 100:
#     sum_of_number += num
#     num += 1
# print("The sum of numbers from the given number to 100 is:", sum_of_number)

# Let's break down what happens step by step when input is 5:
# First iteration (num = 5):

# sum_of_number = 0 + 5 = 5
# num becomes 6
# Second iteration (num = 6):

# sum_of_number = 5 + 6 = 11
# num becomes 7
# This continues until num = 100:

# Adding each number from 5 to 100
# 5 + 6 + 7 + ... + 98 + 99 + 100
# Final calculation:

# It adds ALL numbers from 5 to 100 inclusive
# The sum will be 5050 - (1 + 2 + 3 + 4) = 5050 - 10 = 5040

# ---------------
# Find prime numbers between 2 and 50
# for num in range(2, 51):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")


# Print numbers divisible by 3 or 5 between 1 and 20
# for num in range(1, 21):
#     if num % 3 == 0 or num % 5 == 0:
#         print(num, end=" ")

# Create a list of squares using list comprehension
# squares = [num**2 for num in range(1, 7)]
# print(squares)

# Fibonacci using while loop
# a, b = 0, 1       # Initialize first two numbers (a=0, b=1)
# count = 0         # Initialize counter
# while count < 10: # Loop 10 times
#     print(a, end=" ")  # Print current number
#     a, b = b, a+b      # Magic happens here! Simultaneously:
#                        # - New a becomes old b
#                        # - New b becomes old a + old b
#     count += 1         # Increment counter

# Output: 0 1 1 2 3 5 8 13 21 34

# # Fibonacci using for loop
# a, b = 0, 1
# for _ in range(10):    # Loop 10 times
#     print(a, end=" ")  # Print current number
#     a, b = b, a + b    # Same logic as while loop version

# Output: 0 1 1 2 3 5 8 13 21 34

# Find common elements between two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common_elements = []
# for element in list1:
#     if element in list2:
#         common_elements.append(element)
# print("Common elements:", common_elements)



# my_list = [1, 4, 6, 8, 10, -3, 5, 7]
# index = 0
# while index < len(my_list):
#     if my_list[index] < 0:
#         my_list[index] = 0
#     index += 1
# print("Updated list:", my_list)


# Print numbers in a list until a negative number is encountered using a while loop:
# my_list = [1, 4, 6, 8, 10, -3, 5, 7]
# index = 0
# while my_list[index] >= 0:
#      print(my_list[index])
#      index += 1

# Print numbers from 1 to 5, except 5 using a for loop and continue statement:
# for num in range(1, 7):
#      if num == 5:
#           continue
#      print(num, end=" ")
    
#   
# for num in range(1, 12):
#      print(num, end=" ")
#      if num == 6:
#           break

# for num in range(1, 11):
     
#      if num % 2 == 0:
#           continue
#      print (num, end=" ")
# else:
#         print("\nAll even numbers skipped.")


# pattern printing
# def new_func():
#     row = 5
#     for i in range(1, row+1, 1):
#          for j in range(1, i+1):
#               print(j, end=" ")
#          print("")
# new_func()

# 1: Start value (starts from 1)
# row+1: End value (6 in this case, as range stops before this number)
# 1: Step value (increment by 1)
     
  
# Display numbers from a list using a loop        
# num = [12, 75, 150, 180, 145, 525, 50]
# for i in num: 
#      if i>500:
#           break
#      elif i > 150:
#           continue
#      elif i % 5 == 0:
#           print(i, end=" ")
#      else:
#           print("Not divisible by 5")


# Count the total number of digits in a number
# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10
#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)


# Inverted pattern
# row = 7
# for i in range( row, 0, -1): # start, > end> step
#      for j in range(i, 0, -1):
#           print(j, end=" ")
#      print()

# or

# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()


# Reverse the list
# list1 = [10, 20, 30, 40, 50]
# for i in range(len(list1)-1 ,-1, -1):
#      print(list1[i], end=" ")


# list1 = [10, 20, 30, 40, 50]
# # reverse list
# new_list = reversed(list1)
# # iterate reversed list
# for item in new_list:
#     print(item)

# list1 = [10, 20, 30, 40, 50]
# # get list size
# # len(list1) -1: because index start with 0
# # iterate list in reverse order
# # star from last item to first
# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i]) 

# Display a message “Done” after the successful execution of the for loop
# for i in range(5):
#     print(i)
# else:
#     print("Done!")

# Print all prime numbers within a range
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)
            
#  https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# https://www.linkedin.com/pulse/25-python-loop-coding-questions-mrityunjay-pathak/