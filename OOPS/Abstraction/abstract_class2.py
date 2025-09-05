from abc import ABC,abstractmethod
 
class Animal(ABC):
     
    #concrete method
    def sleep(self):
        print("I am going to sleep in a while")
 
    @abstractmethod
    def sound(self):
         print("This function is for defining the sound by any animal")
         pass
 
class Snake(Animal):
    def sound(self):
        print("I can hiss")
 
class Dog(Animal):
    def sound(self):
        print("I can bark")
 
class Lion(Animal):
    def sound(self):
        print("I can roar")
       
class Cat(Animal):
    def sound(self):
        print("I can meow")

c = Cat()
c.sleep()
c.sound()
 
c = Snake()
c.sound()


# from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

# Creating an object of Circle
circle = Circle(5)
print(circle.area())  # Output: 78.5