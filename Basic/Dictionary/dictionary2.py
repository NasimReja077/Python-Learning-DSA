person = {"name": "Asha", "age": 28, "city": "Kolkata"}

# Creating dictionaries
d1 = {"key1": 1, "key2": 2}
d2 = dict(x=10, y=20) # using dict()
d3 = dict([
     ("p", 100), 
     ("q", 200)
]) # from sequence of pairs
d4 = {} # empty dict

# Accessing values
name = person["name"]     # KeyError if not found # output: KeyError
# name = person.get("name", "unknown") # default value if missing
age = person.get("age")   # returns None if not found
city = person.get("city", "Unknown")  # default value if missing
country = person.get("country", "India")
print(name, age, city, country)

if "age" in person:
     print("Age is present")
if "country" not in person:
     print("Country is not present")
     

# Adding / Updating / Deleting
d = {}
d["a"] = 1                # add
d["a"] = 2                # update

d.update({"b": 3, "c": 4})  # merge/update with another dict
d.update(d2)               # d2 keys overwrite

val = d.pop("b")          # remove key and return value (KeyError if missing)
val = d.pop("z", None)    # safe pop with default
item = d.popitem()        # remove & return last inserted (since 3.7)
d.clear()                 # remove all items
# del d["a"]                # delete specific key (KeyError if missing)

# Merging
d_new = {**d1, **d2}     # d2 keys overwrite d1
d_new = d1 | d2          # Python 3.9+ dict union, d2 keys overwrite d1 #
d1 |= d2                # in-place union, d2 keys overwrite d1 #
d_new = dict(d1)  # shallow copy of d1
d_new = d1.copy()  # shallow copy of d1


# setdefault
d.setdefault("K", []).append(1) # if K not present, set to [] then append || set default then update

# Iteration
for key in d:               # iterate keys
    print(key, d[key])
for k in d.keys():          # keys view
    pass
for v in d.values():        # values view
    pass
for k, v in d.items():      # items view
    print(k, v)

# keys(), values(), items() return view objects (dynamic, reflect changes to dict).

# In Python, append() is a built-in method primarily used with lists to add a single element to the end of the list. This method modifies the original list in-place and does not return a new list.


# Common dictionary methods (summary)

# d.keys() — view of keys
# d.values() — view of values
# d.items() — view of (key, value) pairs
# d.get(key, default=None) — safe access
# d.setdefault(key, default) — set default if missing & return value
# d.update(other) — merge from other mapping/iterable
# d.pop(key, default) — remove key and return value
# d.popitem() — remove & return (key, value) pair (LIFO since 3.7)
# d.clear() — empty the dict
# d.copy() — shallow copy
# dict.fromkeys(iterable, value=None) — create dict from keys
# d.items(), d.keys(), d.values() — mapping views
# d | other — merge dicts (3.9+)

# Performance notes
# Average-case lookup, insert, delete: O(1) (hash table).
# Worst-case can be worse (hash collisions) but Python manages resizing/rehashing.
# Use dict for fast membership/lookup by key. For ordered operations, remember insertion order is preserved, but dict is not a sorted mapping — use sorted() if needed.

# Dictionary Comprehensions
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(squares)


# Nested DictionariesDictionaries can contain other dictionaries or complex data structures.python
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nested_dict["person1"]["name"])  # Output: Alice

# Merge Two Dictionaries
def merge_dicts(dict1, dict2):
     result = dict1.copy()  # start with keys and values of dict1
     result.update(dict2) 
     return result

dict1 = {"a" : 1, "b" : 2}
dict2 = {"b" : 3, "c" : 4}
print(merge_dicts(dict1, dict2)) # Output: {'a': 1, 'b': 3, 'c': 4}

