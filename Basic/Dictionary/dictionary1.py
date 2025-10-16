"""
What is a Dictionary?
> A dictionary (dict) is an unordered (in older Python), mutable collection of key → value pairs.

Keys map to values.
Keys must be hashable (immutable types like int, str, tuple are typical).
Values can be any object.
Since Python 3.7, dictionaries preserve insertion order (this was an implementation detail in 3.6 and a language guarantee from 3.7 onward).

Example:
person = {"name": "Asha", "age": 28, "city": "Kolkata"}

"""


# A dictionary is a collection which is:
# it is unordered
# it is mutable
# it is indexed
# Can not contain duplicate keys.
# it is written with curly brackets, and has keys and values

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


# Keys must be hashable
# Allowed as keys: int, str, float, tuple (if containing hashable items), frozenset.
# Not allowed: list, dict, set (because they are mutable and unhashable).

chai_types = {"Massala":  "Spicy", "Ginger": "Zesty", "Green":"Mind"}
# print(chai_types)

# get the value for key
print(chai_types.get("Ginger")) #Zesty

print(chai_types["Massala"]) #Spicy

chai_types["Ginger"] = "Fresh" #update the value for key
print(chai_types) # {'Massala': 'Spicy', 'Ginger': 'Fresh', 'Green': 'Mind'}

for chai in chai_types:
     print(chai)
     # Massala
     # Ginger
     # Green

for chai in chai_types.values():
     print(chai)
     # Spicy
     # Fresh
     # Mind

for chai, taste in chai_types.items(): 
     print(chai, "is", taste)
     # Massala is Spicy
     # Ginger is Fresh
     # Green is Mind
     

for chai in chai_types: 
     print(chai, chai_types[chai]);
     # Massala Spicy
     # Ginger Fresh
     # Green Mind
     

for key, value in chai_types.items():
     print(key, value)
     # Massala Spicy
     # Ginger Fresh
     # Green Mind
     
if "Massala" in chai_types:
     print("Ok, Naw I will be Eatting Coffie")
     
print(len(chai_types)) #OP: 3

# add new key-value pair
chai_types["Earl Grey"] = "Citrusy"
print(chai_types) # {'Massala': 'Spicy', 'Ginger': 'Fresh', 'Green': 'Mind', 'Earl Grey': 'Citrusy'}

chai_types.pop("Green")
print(chai_types)
# {'Massala': 'Spicy', 'Ginger': 'Fresh', 'Green': 'Mind', 'Earl Grey': 'Citrusy'}
# {'Massala': 'Spicy', 'Ginger': 'Fresh', 'Earl Grey': 'Citrusy'}

chai_types.popitem() #removes the last inserted item
print(chai_types) # {'Massala': 'Spicy', 'Ginger': 'Fresh'}

# remove key-value pair
del chai_types["Massala"]
print(chai_types) # {'Ginger': 'Fresh'}
del chai_types["Ginger"]
print(chai_types) # {}

chai_types.clear() #removes all items
print(chai_types) # {}

chai_types_copy = chai_types.copy()
print(chai_types_copy)
# {}{}{}

tea_shop = {
     "Chai": {"Masala" : "Spicy", "Black": "Strong"},
     "Coffee": {"Espresso": "Bold", "Latte": "Milky"},
     "Juice": {"Orange": "Citrusy", "Apple": "Sweet"}
}
print(tea_shop)
# {'Chai': {'Masala': 'Spicy', 'Black': 'Strong'}, 'Coffee': {'Espresso': 'Bold', 'Latte': 'Milky'}, 'Juice': {'Orange': 'Citrusy', 'Apple': 'Sweet'}}

print(tea_shop["Coffee"]) # {'Espresso': 'Bold', 'Latte': 'Milky'}
print(tea_shop["Coffee"]["Latte"]) # Milky

squared_num = {x: x**2 for x in range(8)} #(1,8)
print(squared_num) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}


keys = ["Cat", "Cow", "Crow"]
print(keys) # ['Cat', 'Cow', 'Crow']

default_value = "Animal"
animal_dict = dict.fromkeys(keys, default_value)
print(animal_dict) # {'Cat': 'Animal', 'Cow': 'Animal', 'Crow': 'Animal'}

new_dict = dict.fromkeys(keys, keys)
print(new_dict) #{'Cat': ['Cat', 'Cow', 'Crow'], 'Cow': ['Cat', 'Cow', 'Crow'], 'Crow': ['Cat', 'Cow', 'Crow']}

#==========================
marks = { # collection 
     "Nasim": 99,
     "Reja": 90,
     "Harry": 55
}
# print(marks, type(marks))
print(marks.items())
print(marks.keys())
print(marks.values)

marks.update({"Harry": 85, "Rony": 65})
print(marks)


print(marks.get("Nasim2")) # print None  | because there is no key like Nasim2
print(marks["Nasim2"]) # return error    | because there is no key like Nasim2


# using key vale are bouth associate and get list type vale , Lest of key vale pear
# https://www.youtube.com/watch?v=v9bOWjwdTlg
# https://www.youtube.com/watch?v=UrsmFxEIp5k&t=21519s&sttick=0
# https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
# https://x.com/i/grok?conversation=1978692423036371049
# https://x.com/i/grok?conversation=1964034485613195311
