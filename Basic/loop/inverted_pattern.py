# Method 1: Using nested for loops
def pattern1():
    rows = 5
    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()  # New line after each row

# Method 2: Using range in reverse with string formatting
def pattern2():
    rows = 5
    for i in range(rows, 0, -1):
        print(" ".join(map(str, range(i, 0, -1))))

# Method 3: Using list comprehension
def pattern3():
    rows = 5
    for i in range(rows, 0, -1):
        print(*range(i, 0, -1))

print("Pattern using Method 1:")
pattern1()

print("\nPattern using Method 2:")
pattern2()

print("\nPattern using Method 3:")
pattern3()

# All methods will produce:
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 
