# Polymorphism and Inheritance
# Method Overriding
# Like in other programming languages, the child classes in Python also inherit methods and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.

# Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.



class A: # Parent
     def info(self):
          print("Parent Class Method.")
class B(A): # Child
     def info(self):
          super().info() # <- this is Method Overriding for run both Parent and Child class.
          print("Child Class Method.")

obj = B()
obj.info()



class Parent():
     def __init__(self):
          self.value = "Insid the Parent"
     
     def show(self):
          print(self.value)
class child(Parent):
     def __init__(self):
          super().__init__()
          self.value = "Inside the Child"
     
     def show(self):
          print(self.value)

obj1 = Parent()
obj2 = child()

obj1.show()
obj2.show()




class B:
    def show(self):
        return "Show method from class B"
class C:
    def show(self):
        return "Show method from class C"
class D(B, C):
    def show(self):
        return "Show method from class D"

# Creating an object of class D
d = D()

# Calling the show method on the object of class D
print(d.show())  # Output: Show method from class D

# Displaying the MRO to see the order of inheritance