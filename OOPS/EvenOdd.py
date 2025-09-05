class Number:
     evens = []
     odds = []
     def __init__(self, num):
          self.num = num
          if num%2==0:
               Number.evens.append(num)
          else:
               Number.odds.append(num)
N1 = Number(21)
N2 = Number(20)
N3 = Number(30)
N4 = Number(48)
N5 = Number(62)

print("Even Number are: ", Number.evens)
print("Odd Number are:", Number.odds)
