# f = open("fileR.txt")
# print(f.read())
# f.close()
# thw same can be written using with statement link this

with open("fileR.txt") as f:
     print(f.read())
# you dont have to explicitly close the file 


