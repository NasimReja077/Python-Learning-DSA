class Mother:
     def Mother_method(self):
          print("This method comes from Mother DNA.")
class Father:
     def Father_method(self):
          print("This method comes from Father DNA.")
class Child(Mother,Father):
     def Child_method(self):
          print("We made a Child DNA.")
child_instance = Child()
child_instance.Mother_method()
child_instance.Father_method()
child_instance.Child_method()


class Addition:
     def add(self, a,b):
          return a + b
class Subtraction:
     def sub(self, a, b):
          return a - b
class Multiplication:
     def mul(self, a,b):
          return a * b
class Division:
     def div(self, a, b):
          if b == 0:
            return "Error! Division by zero is not allowed."
          return a / b 
class Modulus:
     def mod(self, a, b):
          if b==0:
               return "Error! Modulus by zero is not allowed."
          return a % b

# Multiple Inheritance - Calculator Inheriting from All Math Classes
class Calculator(Addition, Subtraction, Multiplication, Division, Modulus):
    def calculate(self, a, b, operator):
         if operator == "+":
              return self.add(a,b)
         elif operator == "-":
              return self.sub(a,b)
         elif operator == "*":
              return self.mul(a,b)
         elif operator == "/":
              return self.div(a,b)
         elif operator == "%":
              return self.mod(a,b)
         else:
              return "Invalid operator! Please use +, -, *, /, or %."
calc = Calculator()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /, %): ")

result = calc.calculate(num1, num2, operator)
print(f"Result: {result}")