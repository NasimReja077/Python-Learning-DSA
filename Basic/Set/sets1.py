'''What is a Set in Python?
A Set in Python is an unordered, mutable, and collection of unique elements.

Unordered → No index, so order of elements is not guaranteed.
Mutable → You can add or remove elements after creation.
Unique elements → No duplicates allowed.
Uses curly braces {} or the set() constructor.


Set Characteristics:
Property	   ->  Description
Unordered	   ->  Items have no index
Unique	   ->  Duplicate items automatically removed
Mutable	   ->  You can add or remove items
Immutable elements ->  You can’t add lists/dicts as set items

'''
# Creating Sets
# (a) Using Curly Braces {}:
fruits = {"apple", "banana", "cherry"}
print(fruits)

# (b) Using set() constructor:
numbers = set([1, 2, 3, 4])
print(numbers)

# Empty Set Caution:
a = {}       # ❌ This creates an empty DICTIONARY
b = set()    # ✅ This creates an empty SET

e = set() # Donnt use s = {} as it will create an empty dictionary

s = {1, 55, 3, 55, 22, 5, 3, 40, 2, "Nasim", "Reja"}
print(s) # {1, 2, 3, 'Reja', 5, 40, 'Nasim', 22, 55} 
print(type(s)) # <class 'set'>

# Properties of Sets
# 1. Sets are unordered => Element`s order doesn`t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in a set, but we can add new items
# 4. Sets cannot contain duplicate values`
# 5. Set items are immutable, but we can remove and add items

# Operations on Sets
b={1,8,2,3}

# len(s),s.remove(3),s.pop(),s.clear(),s.union({10,11,12}),s.intersection({1,2,3}),

# s.add(5),  s.union({10,11,12}), s.update({20,21,22}), s.difference({1,2,3}), s.intersection({1,2,3}), s.issubset({1,2,3}), s.issuperset({1,2,3}), s.isdisjoint({1,2,3}), s.copy()

print(b, type(b))
b.add(566)
print(b, type(b))
b.remove(1)
print(b, type(b))

s1={1, 45, 6, 55, 75}
s2={7, 8, 6, 54, 75}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))


# Accessing Set Items

# You cannot access items using index like a list. But you can loop through a set:
for item in {"Apple, Cat, Ball"}:
     print(item)
     
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

# Add Elements
# add() -> Add a single element
fruits = {"apple", "banana"}
fruits.add("Orange")
print(fruits)

# update() → Add multiple elements
vegetables = {"carrot", "broccoli"}
vegetables.update(["cauliflower", "spinach", "potato"])
print(vegetables)


# Removing Elements from a Set
fruits2 = {"apple", "banana", "cherry", "mango", "orange"}
fruits2.remove("banana") # remove specific item, if item not found it will raise an error
print(fruits2)

fruits2.discard("Kiwi")
print(fruits2) # remove specific item, if item not found it will not raise an error
fruits2.discard("apple")
print(fruits2)

fruits2.pop() # removes a random item
print(fruits2)

fruits2.clear() # removes all items, makes it empty set
print(fruits2)

# Delete Entire Set
del fruits2
print(fruits2)


# Set Operations
# Python sets support mathematical set operations.

# Operation	               Method / Operator	                  Example
# Union	           -        set1.union(set2) or `set1 |         -     set2`
# Intersection	     -  set1.intersection(set2) or set1 & set2	- Common elements
# Difference	       -    set1.difference(set2) or set1 - set2	- Elements in set1 but not in set2
# Symmetric Difference	-    set1.symmetric_difference(set2) or set1 ^ set2	- Elements in either set but not both



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union → {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection → {3, 4}
print(A - B)   # Difference → {1, 2}
print(A ^ B)   # Symmetric Difference → {1, 2, 5, 6}


print(A.issubset(B))       # False
print(A.issuperset(B))     # False
print(A.isdisjoint(B))     # False


# Frozen Set (Immutable Set)
#    A frozen set is an immutable version of a set.
#    You can’t modify it after creation.


Z = frozenset ([1, 2, 3])
print(Z)
# A.add(4)


# Set Comprehension
# You can create sets using set comprehension (like list comprehension).

squared = {x**2 for x in range(6)}
print(squared)



'''
Set Methods (Full List)
Method	Description
add()	Add one element
update()	Add multiple elements
remove()	Remove an element (error if not found)
discard()	Remove an element (no error)
pop()	Remove random element
clear()	Empty the set
union()	Combine two sets
intersection()	Common elements
difference()	Elements in one but not the other
symmetric_difference()	Non-common elements
issubset()	Check if a set is a subset
issuperset()	Check if a set is a superset
isdisjoint()	Check if sets have no common items
copy()	Returns a shallow copy of set
'''