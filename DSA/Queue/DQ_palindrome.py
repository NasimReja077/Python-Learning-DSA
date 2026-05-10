# Write a Python program to check if a string is a palindrome using a Deque.

from collections import deque

def is_palindrome(string):
    # Insert all characters into deque
    dq = deque(string.lower())   # convert to lowercase for comparison

    while len(dq) > 1:
        front_char = dq.popleft()  # delete from front
        rear_char  = dq.pop()      # delete from rear
        if front_char != rear_char:
            return False           # mismatch found

    return True                     # all matched → palindrome

# Test
words = ["radar", "level", "hello", "madam", "python"]
for w in words:
    result = "Palindrome" if is_palindrome(w) else "Not Palindrome"
    print(f"{w:10} → {result}")

# Output:
# radar      → Palindrome
# level      → Palindrome
# hello      → Not Palindrome
# madam      → Palindrome
# python     → Not Palindrome