'''
a = "a very long string with emails"
'''

f = open("fileR.txt", "r")
data = f.read()
print(data)
f.close()


# try:
#     file_path = r"c:\Users\User\Desktop\New folder\PYTHON_Home\Basic\File I-O\File1\fileR.txt"
#     with open(file_path, 'r') as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print(f"Error: Could not find the file")
# except IOError:
#     print("Error: Could not read the file")

