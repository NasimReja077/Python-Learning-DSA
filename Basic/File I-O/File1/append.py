st = "My Name Paku are you amazing"
f = open("myFileFly.txt", "a")
f.write(st)
f.close()


# st = "My Name Paku are you amazing"
# try:
#     file_path = r"c:\Users\User\Desktop\New folder\PYTHON_Home\Basic\File I-O\File1\myFileFly.txt"
#     with open(file_path, "a") as f:
#         f.write(st)
#         print("File appended successfully!")
# except IOError:
#     print("Error: Could not write to the file")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
