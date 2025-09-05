# Single Thread
from time import sleep
class A:
     def run(self):
          for i in range(5):
               print("Nasim")
               sleep(1)
class B:
     def run(self):
          for i in range(5):
               print("Reja")
               sleep(1)

t1=A()
t2=B()

t1.run()
t2.run()
