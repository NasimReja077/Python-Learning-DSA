cars = ["Ford", "Volvo", "BMW", "TATA", "Marutie"]
# print(cars)

# x = cars[1] # Get the value of the first array item
# print(x)

# cars[0]="BMW-5" # Modify the value of the first array item:
# print(cars)


# x = len(cars) # The Length of an Array
# print(x) # Return the number of elements in the cars array:


# for i in (cars): # loop
#      print(i)


cars.append("Honda") # Adding Array Elements
cars.append("Hero Motor")
print(cars)

# cars.pop(0) # Removing Array Elements
# cars.pop(1)
# print(cars)

# cars.remove("TATA")
# print(cars)

# cars.clear()
# print(cars)

# x = cars.count("Volvo")
# print(x)

# fruits = ['apple', 'banana', 'cherry']
# cars.extend(fruits)
# print(cars)


# cars.insert(1,"HERO")
# print(cars)

# cars.pop(1)
# print(cars)

cars.reverse()
print(cars)

# ********** Python List sort() Method**********
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# A function that returns the length of the value:

# def myFunc(e):
#   return len(e)
# cars2 = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars2.sort(key=myFunc)
# print(cars2)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

car = ['Ford', 'Mitsubishi', 'BMW', 'VW']

car.sort(reverse=True, key=myFunc)

print(car)
