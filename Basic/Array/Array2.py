# import array as arr
# a = arr.array('d', [1.1,3.5,4.5])
# print(a)

# import array as ar
# a= ar.array('i',[5, 4, 6, 8, 10])
# print("First element:", a[0])
# print("Second elemnt:", a[1])
# print("List element:", a[-1])


# import array as arr
# Nu_list = [2, 5, 62, 5, 42, 52, 48, 5]
# Nu_array = arr.array('i', Nu_list)
# print(Nu_array[2:5]) # 3rd to 5th
# print(Nu_array[:-5]) # beginning to 4th
# print(Nu_array[5:])  # 6th to end
# print(Nu_array[:])   # beginning to end 

import array as arr
numbers = arr.array('i', [1, 2, 3, 5, 7, 20])
# Changing first element
numbers[0] = 10
print(numbers)
# changing 3rd to 5th element
numbers[2:5] = arr.array('i',[7,3,9])
print(numbers)


# import array as arr
# numbers = arr.array('i', [1, 2, 3])
# numbers.append(4)
# print(numbers)     # Output: array('i', [1, 2, 3, 4])
# # extend() appends iterable to the end of the array
# numbers.extend([5, 6, 7])
# print(numbers)     # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

# import array as arr
# odd = arr.array('i', [1, 3, 5])
# even = arr.array('i', [2, 4, 6])
# numbers = arr.array('i')   # creating empty array of integer
# numbers = odd + even
# print(numbers)


# import array as arr
# number = arr.array('i', [1, 2, 3, 3, 10, 11, 12, 12, 13])

# del number[2]  # removing third element
# print(number)  # Output: array('i', [1, 2, 3, 4])

# number.remove(12)
# print(number)   # Output: array('i', [10, 11, 12, 13])

# print(number.pop(2))   # Output: 12
# print(number)   # Output: array('i', [10, 11, 13])




# # Searching Element
# import array
# arr = array.array('i', [1, 2, 3, 1, 2, 5])
# # index of 1st occurrence of 2
# print(arr.index(2))
# # index of 1st occurrence of 1
# print(arr.index(1))



# import array as arr
# # creating array
# a = arr.array('i', [1, 2, 3])
# # iterating and printing each item
# for i in range(0, 3):
#     print(a[i], end=" ")


# Important Functions -https://www.geeksforgeeks.org/array-in-python-set-2-important-functions/