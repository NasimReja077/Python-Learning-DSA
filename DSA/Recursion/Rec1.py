# Print Numbers (1 to 5)
def print_numbers(n):
    if n > 5:        # Base case
        return
    print(n)
    print_numbers(n + 1)   # Recursive call

print_numbers(1)


age = int(input("Enter your age: "))

if age < 13:
    print("You are a child 👶")
elif age < 18:
    print("You are a teenager 😎")
elif age < 60:
    print("You are an adult 💼")
else:
    print("You are a senior citizen 👴")


def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))


def sum_n(n):
    if n == 0:      # Base case
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


