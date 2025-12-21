# class is a blueprent of creating object


# Noun -> class -> Employee
# Adjective -> Attributes -> name, age, salary
# Verbs -> Methods -> getSalary(), increment()


class Employee: # Employee is obj
     language = "py"  # This is class attributes
     salary = 12000
     
harry = Employee()
harry.name = "Harry Putar"  # This is instance attributes
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan putar"
print(rohan.name, rohan.salary, rohan.language)

# here name is instance attribute and salaly and language attributes as they directly belog to the class 


