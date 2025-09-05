# In object-oriented-based Python programming, Polymorphism means the same function name is being used for different types.Each function is differentiated based on its data type and number of arguments. So, each function has a different signature. This allows developers to write clean, readable, and resilient codes.
Friends = ['Roy', 'Nasim', 'Reja']
City = 'Kolkata'
#calculate length
print(len(Friends))
print(len(City))


print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))



# Ex-2
mystr = 'Programming'
print('Length of string:', len(mystr))

mylist = [1, 2, 3, 4, 5]
print('Length of list:', len(mylist))

mydict = {1: 'One', 2: 'Two'}
print('Length of dict:', len(mydict))


#EX-3
class Tiger():
     def nature(self):
          print("I am a Tiger and I am dangerous.")
     def food(self):
          print("meate")
     def color(self):
          print("Tigers are orange with black strips.")
class Elephant():
     def nature(self):
          print("I am an Elephant and I am calm and harmless")
     def food(self):
          print("Vagitable")
     def color(self):
          print("Elephants are grayish black")

tiger = Tiger()
elephant = Elephant()

for animal in (tiger, elephant):
     animal.nature()
     animal.food()
     
     


class Boy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

    def gender(self):
        print("M")

class Girl:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

    def gender(self):
        print("F")

boy1 = Boy("Sam", 20)
girl1 = Girl("Mona", 26)

for person in (boy1, girl1):
    person.gender()
    person.info()
    person.gender()