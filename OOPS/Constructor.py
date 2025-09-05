
# In Python, a constructor is a special method that is called automatically when an object is created from a class. Its main role is to initialize the object by setting up its attributes or state.

#The method __new__ is the constructor that creates a new instance of the class while __init__ is the initializer that sets up the instance’s attributes after creation. These methods work together to manage object creation and initialization.
class Constructors:
     def __init__(self): # Emty Constructors
          print("Nasim")
     
     def __init__(self): # Constructors
          print("Samima")
obj=Constructors()

# Differences Between __init__ and __new__
# Types of Constructors -> 1) Default Constructor 2) Parameterized Constructor

# 1) Default Constructor

class A:
     name = "Nasim"
     age = "23"
     def __init__(self):
          home="Kolkata"
          print(self.name," ",home)
     def Show(self):
          print(self.age)

obj=A()
obj.Show()


class Car:
    def __init__(self):

        #Initialize the Car with default attributes
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

# Creating an instance using the default constructor
car = Car()
print(car.make)
print(car.model)
print(car.year)


class B:
     name3 = "Samima"
     def __init__(self,age,name,home):
          home="Kolkata"
          print(age,name,home,self.name3)
     def Show(self):
          print(self.name3)

obj=A(23,"Nasimo",None)
obj.Show()

class Car:
    def __init__(self, make, model, year):
      
        #Initialize the Car with specific attributes.
        self.make = make
        self.model = model
        self.year = year

# Creating an instance using the parameterized constructor
car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)
