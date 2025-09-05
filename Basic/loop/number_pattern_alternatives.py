# Method 1: Using while loops
def pattern_while():
    row = 5
    i = 1
    while i <= row:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print("")
        i += 1

# Method 2: Using list comprehension
def pattern_list_comp():
    row = 5
    for i in range(1, row + 1):
        print(*range(1, i + 1))

# Method 3: Using string multiplication
def pattern_string():
    row = 5
    for i in range(1, row + 1):
        print(" ".join(map(str, range(1, i + 1))))

# Method 4: Using format string
def pattern_format():
    row = 5
    for i in range(1, row + 1):
        line = " ".join(str(x) for x in range(1, i + 1))
        print(f"{line}")

# Try each method
print("Method 1: Using while loops")
pattern_while()
print("\nMethod 2: Using list comprehension")
pattern_list_comp()
print("\nMethod 3: Using string multiplication")
pattern_string()
print("\nMethod 4: Using format string")
pattern_format()
