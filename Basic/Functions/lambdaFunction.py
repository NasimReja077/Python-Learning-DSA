# Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 

# # String Manipulation
# s1 = "NasimREja"
# s2 = lambda func: func.upper()
# print(s2(s1))

# # Number Classification
# n = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
# print(n(5))
# print(n(-5))
# print(n(0))


# List of Lambda Functions
# list = [lambda arg=num: arg * 10 for num in range(1, 5)]
# for num in list:
#     print(num())

# Explanation -
# [
#     lambda arg=1: arg * 10,
#     lambda arg=2: arg * 10,
#     lambda arg=3: arg * 10,
#     lambda arg=4: arg * 10
# ]


# Example: Perform addition and multiplication in a single line
# calc = lambda x, y: (x + y, x * y)
# res = calc(3, 4)
# print(res)


n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))


# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))
