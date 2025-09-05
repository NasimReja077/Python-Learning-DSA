class Parent:
     def parent_method(self):
          print("This is the parent method.")
class Child(Parent): # Child inherits from Parent
     def child_method(self):
          print("This is the child method.")
# Using the classes
child_instance = Child()
child_instance.parent_method() # Accessing the parent's method
child_instance.child_method()  # Accessing the child's own method


# Animal and Dog Class with Inheritance and Method Overriding
class Animal:
     def __init__(self, name):
          self.name = name

     def sound(self):
          pass  # Placeholder for subclasses to implement

class Dog(Animal):
     def sound(self):
          return f"{self.name} says Woof Woof!"

# Creating an instance of Dog
dogie = Dog("Tomie")

# Correct way to call instance method
print(dogie.sound())  # Calling the sound() method on the object


class Person:
     def __init__(self, name, id):
          self.name = name
          self.id = id
     
     def get_Person_details(self):
          return f"Name: {self.name}, ID: {self.id}"
class Student(Person):
     def __init__(self, name, id, grade, courses):
          super().__init__(name, id)
          self.grade = grade
          self.courses = courses
     def get_Person_details(self):
          return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}, Courses: {', '.join(self.courses)}"
student_1 = Student("Nasim", 5678, "B+", ["Math", "Physics", "Computer Science"])
print(student_1.get_Person_details())