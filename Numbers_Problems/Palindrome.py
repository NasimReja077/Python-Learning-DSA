n = int(input("Enter Your Number: "))  # Take input
sum = 0
temp = n  # Store original number

while n > 0:
    remainder = n % 10  # Extract last digit
    sum = sum * 10 + remainder  # Reverse number logic
    n = n // 10  # Remove last digit

if temp == sum:
    print(temp, "is a Palindrome number.")
else:
    print(temp, "is not a Palindrome number.")
