# class Box1:
#      def __init__(self):
#           self.str1 = "A Class"
#           print("Box1")
# class Box2(Box1):
#      def __init__(self):
#           self.str2 = "B Class"
#           print(Box2)
# class Box3(Box2):
#      def __init__(self):
#           self.str3 = "C Class"
#           print(Box3)
     

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Rectangle(Shape):
    def __init__(self, length, width):  # Corrected parameter name 'Width' to 'width' for consistency
        self.width = width
        self.length = length
    
    def area(self):
        print(f"The Area of Rectangle is {self.length * self.width}")

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def area(self):
        print(f"The Area of Square is {self.length ** 2}")  # Corrected "Rectangle" to "Square"

# Creating objects of the class
Rect = Rectangle(3, 5)
my_sqre = Square(6)

Rect.area()
my_sqre.area()

class employee():#Super class
     def __init__(self,name,age,salary):
          self.name = name
          self.age = age
          self.salary = salary
class childemployee1(employee):#First child class
     def __init__(self,name,age,salary):
          self.name = name
          self.age = age
          self.salary = salary
 
class childemployee2(childemployee1):#Second child class
     def __init__(self, name, age, salary):
          self.name = name
          self.age = age
          self.salary = salary
emp1 = employee('harshit',22,1000)
emp2 = childemployee1('arjun',23,2000)
 
print(emp1.age)
print(emp2.age)