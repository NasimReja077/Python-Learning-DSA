# Practical Questions (Practice Problems)

# Create and Access
# Create a tuple with 5 elements of different data types.
# Access the second and last elements using indexing.
# Slice the tuple to get elements from index 1 to 3.

my_tuple = (10, 3.25, "Nasim", True, [1,2])

print("--- Create and Access ---")
print(f"Original tuple: {my_tuple}")
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[1:4])
print("-" * 25)


# Tuple Unpacking:
# Write a function that returns a tuple of three values (e.g., name, age, city).
# Unpack the returned tuple into three variables and print them.

# my_tuple = (1, 2, 3, 4, 5)
# first, *middle, last = my_tuple
# print(first, middle, last)  # Output: 1 [2, 3, 4] 5

def userInfo():
     return ("Nasim",30, "Kolkata")

print("--- Tuple Unpacking ---")
name, age, city = userInfo()
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print("-" * 25)

# Nested Tuples:
# Create a tuple containing two nested tuples, each with three numbers.
# Access the second element of the second nested tuple.

nested_tuple = ((1, 2, 3), (4, 5, 6))

print("--- Nested Tuples ---")
print(f"Nested tuple: {nested_tuple}")
element = nested_tuple[1][1]
print(f"The second element of the second nested tuple is: {element}")
print("-" * 25)

# Count and Index:
# Create a tuple with some duplicate elements (e.g., (1, 2, 2, 3, 1)).
# Use count() to find how many times 2 appears.
# Use index() to find the first occurrence of 1.
count_index_tuple = (1, 2, 2, 3, 1)

print("--- Count and Index ---")
print(f"Tuple for count and index: {count_index_tuple}")

# Use count() to find how many times 2 appears.
count_of_2 = count_index_tuple.count(2)
print(f"The number 2 appears {count_of_2} time(s).")

# Use index() to find the first occurrence of 1.
index_of_1 = count_index_tuple.index(1)
print(f"The first occurrence of 1 is at index: {index_of_1}")
print("-" * 25)

# --- Tuple as Dictionary Key ---

# Tuple as Dictionary Key:
# Create a dictionary with tuples as keys (e.g., coordinates) and strings as values (e.g., location names).
# Retrieve a value using a tuple key.
locations = {
    (40.7128, -74.0060): "New York City",
    (34.0522, -118.2437): "Los Angeles",
    (51.5074, 0.1278): "London"
}

print("--- Tuple as Dictionary Key ---")
print(f"Dictionary with tuple keys: {locations}")

# Retrieve a value using a tuple key.
nyc_location = locations[(40.7128, -74.0060)]
print(f"The location at (40.7128, -74.0060) is: {nyc_location}")
print("-" * 25)

# --- Extended Unpacking ---

# Extended Unpacking:
# Given a tuple (1, 2, 3, 4, 5), use extended unpacking to assign the first element to a, the last to b, and the rest to rest.
# Print a, rest, and b.

# Given a tuple (1, 2, 3, 4, 5), use extended unpacking.
extended_tuple = (1, 2, 3, 4, 5)

print("--- Extended Unpacking ---")
print(f"Original tuple for extended unpacking: {extended_tuple}")

# Assign the first element to 'a', the last to 'b', and the rest to a list 'rest'.
a, *rest, b = extended_tuple

# Print the results.
print(f"First element (a): {a}")
print(f"Rest of the elements (*rest): {rest}")
print(f"Last element (b): {b}")
print("-" * 25)

# --


# Write a function to find the second-largest element in a tuple of numbers
def second_largest(tup):
    if len(tup) < 2:
        return None
    sorted_tup = sorted(tup, reverse=True)
    return sorted_tup[1]

my_tuple = (5, 2, 8, 1, 9)
print(second_largest(my_tuple))

# Given a tuple of strings, return a new tuple with strings longer than 3 characters

def filter_log_Str(tup):
     return tuple(i for i in tup if len(i)>3)
my_tuple = my_tuple = ("cat", "dog", "apple", "hi")
print(filter_log_Str(my_tuple))

# Write a function to merge two tuples and remove duplicates
def merg_tuples(tup1, tup2):
     return tuple(set(tup1 + tup2))
tuple1 = (2,1,3,5)
tuple2 = (2,4,6,5,1)
print(merg_tuples(tuple1,tuple2))







