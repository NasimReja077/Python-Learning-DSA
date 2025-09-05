# empty class
# class Humans:
#      def __init__(self):
#           pass

class Dog:
     def __init__(self, name, age): #Adding attributes to a class
          self.name = name  # Instance attribute
          self.age = age    # Instance attribute
     species = "Canine"  # Class attribute
# Creating an object of the Dog class     
dogbox1 = Dog("Tomie", 3) # Create an instance of Dog
dogbox2 = Dog("Buddy", 7)
dogbox2.species = "Labrador"
# print("Dog name is = ",dogbox1.name)
# print("Dog age is = ",dogbox1.age)
# print("Dog species is = ",dogbox1.species)
print(dogbox1.name, dogbox1.age, dogbox1.species)  # Access instance and class attributes
print(f"Hi! Dog name is {dogbox1.name}.and Dog Old is {dogbox1.age} years") # different values per instance, because they are instance attributes
print(dogbox2.name, dogbox2.age, dogbox2.species)
print(Dog.species)  # Access class attribute directly



class Human:
     #class attribute
     species = "Homo Sapiens"
     company_name = 'ABC Company'
     def __init__(self, name, age, gender, salary, role, userid, password):
          self.name = name
          self.age = age
          self.gender = gender
          self.salary = salary
          self.role = role
          self.userid = userid
          self.password = password
          
     #Instance Method
     def speak(self):
          return f"Hello everyone! My Name is {self.name}.I am {self.age} years old {self.gender}."
     def companyInfo(self):
          return f"I am Working in {self.company_name}.This is World bests Company.My role is {self.role}.I am so Happy for work hear."
     def emplyInfo(self):
          return f"Employ Name - {self.name},Employ Company Name - {self.company_name},Emply Role - {self.role},Emply Id - {self.userid},Emply Password - {self.password},Emply Salary - {self.salary}"
     
     # Creating an object of the Human class outside the class definition
person1 = Human("Nasim", 25, "male", 35000, "IT Support", "U0E1", "ER@007")

# Calling methods and printing results
print(person1.speak())
print(person1.companyInfo())
print(person1.emplyInfo())
          