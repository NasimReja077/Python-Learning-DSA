# f = open("fileR.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()


# try:
#     file_path = r"c:\Users\User\Desktop\New folder\PYTHON_Home\Basic\File I-O\File1\fileR.txt"
#     with open(file_path, 'r') as f:
#         lines = f.readlines()
#         print("Lines read from file:", lines)
#         print("Type of lines:", type(lines))
        
#         # Print each line separately for better readability
#         print("\nPrinting each line:")
#         for i, line in enumerate(lines, 1):
#             print(f"Line {i}: {line.strip()}")
# except FileNotFoundError:
#     print(f"Error: Could not find the file")
# except IOError:
#     print("Error: Could not read the file")
# except Exception as e:
#     print(f"An unexpected error occurred: {str(e)}")


# try:
#     file_path = r"c:\Users\User\Desktop\New folder\PYTHON_Home\Basic\File I-O\File1\fileR.txt"
#     with open(file_path, 'r') as f:
#         # Read lines one by one
#         print("Reading lines one by one:")
#         line1 = f.readline()
#         print(f"Line 1: {line1.strip()}, Type: {type(line1)}")
        
#         line2 = f.readline()
#         print(f"Line 2: {line2.strip()}, Type: {type(line2)}")
        
#         line3 = f.readline()
#         print(f"Line 3: {line3.strip()}, Type: {type(line3)}")
        
#         line4 = f.readline()
#         print(f"Line 4: {line4.strip()}, Type: {type(line4)}")
        
#         line5 = f.readline()
#         print(f"Line 5: {line5.strip()}, Type: {type(line5)}")
        
#         # Note: if the file has fewer than 5 lines, empty strings will be returned
#         if not line5:
#             print("\nNote: Reached end of file before line 5")
# except FileNotFoundError:
#     print(f"Error: Could not find the file")
# except IOError:
#     print("Error: Could not read the file")
# except Exception as e:
#     print(f"An unexpected error occurred: {str(e)}")


f = open("fileR.txt")

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))


line6 = f.readline()
print(line6 == " ")
f.close()


f = open("fileR.txt")
line = f.readline()
while(line != ""):
     print(line)
     line = f.readline()
f.close()

     