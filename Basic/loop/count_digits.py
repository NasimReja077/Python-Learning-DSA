# Method 1: Convert to string and use len()
def count_digits_str(number):
    return len(str(abs(number)))  # abs() handles negative numbers

# Method 2: Using mathematical way (division method)
def count_digits_math(number):
    number = abs(number)  # Handle negative numbers Uses abs() to handle negative numbers
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

# Method 3: Using logarithm
import math
def count_digits_log(number):
    number = abs(number)  # Handle negative numbers
    if number == 0:
        return 1
    return math.floor(math.log10(number) + 1)

# Test all methods
test_numbers = [12345, -9876, 0, 7, 1000000]

print("Testing different methods to count digits:")
print("-" * 40)

for num in test_numbers:
    print(f"\nNumber: {num}")
    print(f"String method: {count_digits_str(num)} digits")
    print(f"Math method: {count_digits_math(num)} digits")
    print(f"Log method: {count_digits_log(num)} digits")

# Example of user input
if __name__ == "__main__":
    try:
        number = int(input("\nEnter a number to count its digits: "))
        print(f"The number {number} has {count_digits_str(number)} digits")
    except ValueError:
        print("Please enter a valid integer")
