"File Handling"

"""
File Handling is used for permanent storage of data on the hard disk

Database is used to save data when it is in large amounts
File handling is used to permanently store small quantities of data
"""

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File1.txt", 'w')
# data = "Welcome to python class"
# f.write(data)
# f.close()

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File1.txt", 'r')
# data = f.read()
# print(data)
# f.close()

"""
Factory Functions: These are the functions which return the object of a class when 
they are called
"""

# class C1:
#     pass
#
#
# def func1():
#     return C1()
#
# x = func1()
# print(type(x))
# y = func1()
# print(type(y))
# z = func1()
# print(type(z))
# w = func1()
# print(type(w))

"""
The class that is used to achieve file handling in python is called the TextIOWrapper Class
The open function is the factory function of this class
"""

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File1.txt", 'r')
# print(type(f))
# f.close()

"""
In file handling the data can be stored in the files in two different types.
It can be stored as a group of characters (Character Oriented Stream) and it can be stored 
in the form of a group of bytes (Byte Oriented Stream)

Modes in file handling:
1. Character Oriented Stream: There are 6 different modes to open a file in character oriented 
streams. They are:

    a. 'r'  :   read mode           : If we open a file in read mode, then if it is present 
                                    at the given location, then the data is read from it. But 
                                    if it is not present then it returns an error
    
    b. 'w'  :   write mode          : If we open a file in write mode and it is not present at
                                    the given location, then the file will be created and data
                                    will be written in it, but if the file is already present,
                                    then it will be truncated and new data would be stored
    
    c. 'a'  :   append mode         : If we open a file in append mode and it is not present at
                                    the given location, then the file will be created and data
                                    will be written in it. But  if the file is already present
                                    then new data would be stored at the end of the file
    
    d. 'r+' :   read and write
    
    e. 'w+' :   write and read
    
    f. 'a+' :   append and read   

2. Byte Oriented Stream: There are again 6 types of modes here. They are:

    a. 'rb'
    
    b. 'wb'
    
    c. 'ab'
    
    d. 'rb+'
    
    e. 'wb+'
    
    f. 'ab+'
"""


# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File2.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File2.txt", 'w')
# data = "You are in python class"
# f.write(data)
# f.close()

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File2.txt", 'w')
# data = "Welcome to CETPA Noida"
# f.write(data)
# f.close()


# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File3.txt", 'a')
# data = "Welcome to CETPA Noida"
# f.write(data)
# f.close()

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File3.txt", 'a')
# data = "We are in python class"
# f.write(data)
# f.close()

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File3.txt", 'r')
# data = f.read(12)
# print(data)
# data = f.read(10)
# print(data)
# f.close()

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File3.txt", 'r')
# data = f.read(12)
# print(data)
# f.close()
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File3.txt", 'r')
# data = f.read(10)
# print(data)
# f.close()

# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File3.txt", 'r')
# print(f.tell())
# data = f.read(12)
# print(data)
# print(f.tell())
# data = f.read(10)
# print(data)
# print(f.tell())
# f.close()


"""
seek() method

Syntax:

file_obj.seek(offset, whence)

whence: In byte oriented streams, the whence argument can have 3 values, i.e. 0, 1 and 2

0   :   It will send the cursor to a position wrt the start of the sile
1   :   It will send the cursor to a position wrt its current position 
2   :   It will send the cursor to a position wrt the end of the file

Note: In character oriented streams, whence can have only a single value, i.e. 0

offset: The offset argument is used to move the cursor by a certain number of places.
It takes and +ve or -ve int type value

If the value if +ve: the cursor will move that many places towards right
If the value if -ve: the cursor will move that many places towards left


seek(5, 0)
seek(-7, 1)
seek(10, 1)
seek(-15, 2)
"""


# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File3.txt", 'r')
# data = f.read(12)
# print(data)
# print(f.tell())
# f.seek(0, 0)
# print(f.tell())
# data = f.read(10)
# print(data)
# print(f.tell())
# f.close()


# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File3.txt", 'rb')
# data = f.read(16)
# print(data)
# print(f.tell())
# f.seek(6, 1)
# print(f.tell())
# data = f.read()
# print(data)
# print(f.tell())
# f.close()


# # New Program
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File1.txt", 'r')
# f1 = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\File4.txt", 'w')
#
# data = f.read()
# f1.write(data)
#
# f.close()
# f1.close()


# # New Program
# f = open(r"C:\Personal\Jai\Movies\Harry Potter Series\Harry Potter.pdf", 'rb')
# f1 = open(r"C:\Personal\Jai\Movies\Harry Potter Series\Harry Potter(1).pdf", 'wb')
# data = f.read()
# f1.write(data)
# f.close()
# f1.close()

# # New Program
# f = open(r"C:\Personal\Jai\Movies\MCU\3. Iron Man II.mkv", 'rb')
# f1 = open(r"C:\Personal\Jai\Movies\MCU\3. Iron Man II(1).mkv", 'wb')
#
# while True:
#     data = f.read(200)
#     if data == b'':
#         break
#     f1.write(data)
#
# f.close()
# f1.close()