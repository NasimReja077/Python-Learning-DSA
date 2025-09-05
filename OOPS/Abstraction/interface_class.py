from abc import ABC,abstractmethod
class Shape(ABC):
     @abstractmethod
     def Show(self):
          pass
     
     @abstractmethod
     def Disp(self):
          pass
     
class Square(Shape):
     def Disp(self):
          pass
class Circle(Square):
     def Show(self):
          print("Circle has round shape..........haha.")
     def Disp(self):
          print("Square has 4 side ..........OK.")
c=Circle()
c.Show()
c.Disp()


# from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_a_noise():
        pass

class Pet(ABC):
    @abstractmethod
    def play():
        pass

class Dog(Animal, Pet):
    def make_a_noise():
        return "bark" 

    def play():
        return "fetch a ball" 

# check whether Dog is a sub class of Animal class
print(issubclass(Dog, Animal))
# check whether Dog is a sub class of Pet class
print(issubclass(Dog, Pet))
# Method resolution order 


# Multiple Interfaces (Multiple Inheritance) - Python allows a class to implement multiple interfaces using multiple inheritance.

from abc import ABC, abstractmethod
# First Interface
class Engine(ABC):
     @abstractmethod
     def Start_Engine(self):
          pass

# Second Interface
class Wheels(ABC):
     @abstractmethod
     def NO_Wheels(self):
          pass

# Implementing both interfaces
class Car(Engine, Wheels):
     def Start_Engine(self):
          return "Car Engine Started"
     
     def NO_Wheels(self):
          return 4

# Creating an object
MY_Car = Car()
print(MY_Car.Start_Engine()) # Output: Car engine started
print("Number of Wheels:", MY_Car.NO_Wheels()) # Output: 4


from abc import ABC, abstractmethod

# Defining the Payment Interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount): 
        return f"Paid {amount} using Credit Card."

class PhonePay(CreditCard):
    def pay(self, amount):
        return f"Paid {amount} using PhonePay."

# ✅ Move process_payment outside of class definitions
def process_payment(payment_method: PaymentMethod, amount):
    print(payment_method.pay(amount))

# Creating objects
CC = CreditCard()
PY = PhonePay()

# ✅ Now process_payment() is correctly defined before calling
process_payment(CC, 2000)  # Output: Paid 2000 using Credit Card.
process_payment(PY, 700)   # Output: Paid 700 using PhonePay.