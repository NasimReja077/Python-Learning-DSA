from abc import ABC,abstractmethod
class Car(ABC):
     def Show(self):
          print("Every car has 4 wheels.....OK")
     @abstractmethod
     def Speed(self):
          pass

class Tovoyta(Car):
     def Speed(self):
          print("Tovoyta Max Speed is 100Km/H")

class Volvo(Car):
     def Speed(self):
          print("Volvo Max Speed is 300Km/H")
          
obj1 = Tovoyta()
obj1.Show()
obj1.Speed()

obj2 = Volvo()
obj2.Show()
obj2.Speed()

