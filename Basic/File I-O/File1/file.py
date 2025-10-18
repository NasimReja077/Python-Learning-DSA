# . What is File I/O in Python?

# File I/O (Input and Output) refers to reading data from files and writing data into files using Python.
# Input means reading data from a file.
# Output means writing data to a file.
# Python provides a built-in function called open() to handle files.
'''
Parameters:         Mode	Description
'r'	Read mode (default). File must exist.
'w'	Write mode. Creates new file or overwrites existing one.
'a'	Append mode. Adds new data to the end of file.
'x'	Exclusive creation mode. Fails if file already exists.
'b'	Binary mode (useful for images, PDFs).
't'	Text mode (default).
'r+'	Read and write mode.'''



# Reading Files
# Example 1: Read Entire File
f = open("data.txt", "r")
data = f.read()
print(data)
f.close()

# Example 2: Read Only First 10 Characters
f = open("data.txt", "r")
print(f.read(10))
f.close()

# Example 3: Read Line by Line
f = open("data.txt", "r")
for line in f:
    print(line.strip())  # removes newline
f.close()

# Example 4: readline() and readlines()
f = open("data.txt", "r")
print(f.readline())   # reads one line
print(f.readlines())  # reads all lines as list
f.close()

# 4. Writing Files
# Example 1: Write Mode ('w')
f = open("newfile.txt", "w")
f.write("Hello, this is a new file!\n")
f.write("Python File I/O is simple.")
f.close()


# ⚠️ Note: "w" mode overwrites existing data.
# Example 2: Append Mode ('a')
f = open("newfile.txt", "a")
f.write("\nAdding another line.")
f.close()

# ✅ 5. Using with Statement (Recommended)
# Using with automatically closes the file.

with open("example.txt", "r") as f:
    data = f.read()
    print(data)


# You don’t need to call f.close() — it’s done automatically!
# 💾 6. Working with Binary Files
# Binary files include images, videos, etc.

with open("image.jpg", "rb") as f:
    data = f.read()

with open("copy.jpg", "wb") as f:
    f.write(data)
    
    
    
# File Copy Program
with open("source.txt", "r") as src:
    data = src.read()

with open("destination.txt", "w") as dest:
    dest.write(data)


# Exception Handling in File Operations
try:
    with open("unknown.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Error while reading the file!")
    
    
# tell() Returns the current position of the file cursor (in bytes).
f = open("demo.txt", "r")
f.read(10)
print(f.tell())
f.close()

# seek(offset, whence) - Moves the file cursor to a specific position.
# Syntax:
# f.seek(offset, whence)

# Parameter	Description
# offset	Number of bytes to move
# whence	0 → beginning (default), 1 → current position, 2 → end
# Example:
f = open("demo.txt", "r")
print(f.read(5))  # read 5 chars
f.seek(0)         # move back to start
print(f.read(5))  # read again
f.close()

# close() - Closes the file and releases system resources.
# Example:
f = open("demo.txt", "r")
data = f.read()
f.close()

# flush() - Forces writing buffered data to the file immediately.
# Example:
f = open("temp.txt", "w")
f.write("Hello")
f.flush()  # forces data to save immediately
f.close()

# name - Returns the name of the file.
# Example:
f = open("demo.txt", "r")
print(f.name)
f.close()

# mode - Shows the mode in which the file was opened.
# Example:
f = open("demo.txt", "r")
print(f.mode)
f.close()


# readable(), writable(), seekable() - Returns True/False based on file’s properties.
# Example:
f = open("demo.txt", "r")
print(f.readable())  # True
print(f.writable())  # False
print(f.seekable())  # True
f.close()

# truncate(size) - Truncates (cuts) the file to the given size (in bytes).
# Example:
f = open("demo.txt", "w")
f.write("Python is fun!")
f.truncate(6)
f.close()

f = open("demo.txt", "r")
print(f.read())
f.close()


# fileno() - Returns the file’s descriptor number (an integer handle).
f = open("demo.txt", "r")
print(f.fileno())
f.close()

# isatty() - Returns True if the file is connected to a terminal device (usually False for files).
f = open("demo.txt", "r")
print(f.isatty())  # False
f.close()



'''
Summary Table of File Methods
Method	               Description
read(size)	          Reads file content.
readline()	          Reads one line.
readlines()	          Reads all lines into a list.
write(string)	          Writes string to file.
writelines(list)	     Writes list of strings.
seek(offset, whence)     Moves cursor to position.
tell()	               Returns cursor position.
close()	               Closes the file.
flush()	               Flushes buffer to disk.
truncate(size)	          Cuts file to specific size.
name	                    Returns filename.
mode	                    Returns file mode.
readable()	          Returns True if file is readable.
writable()	          Returns True if writable.
seekable()	          Returns True if seek is allowed.
fileno()	               Returns file descriptor number.
isatty()	               Returns True if file is a terminal.
'''