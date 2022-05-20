"Modules"

"""
Modules: Any user-defined or pre-defined .py or .pyc file is called a module

Agenda:
1. How to access modules
2. Which way of accessing modules is the best
3. How to access selected code of the program
4. How to access modules which are not in the current directory
5. How to create .pyc files
6. How to access .pyc files
7. How to create packages
8. How to download packages


1. How to access modules:
There are 5 different ways to access modules;
    a. import module_name
    b. import module_name as alias
    c. from module_name import feature 
    d. from module_name import feature as alias
    e. from module_name import *
"""
"import module_name"
# import python
# n1 = 7
# n2 = 11
# sum = python.add(n1, n2)
# print(sum)
#
# diff = python.sub(n1, n2)
# print(diff)

"import module_name as alias"
# import python as py
# n1 = 11
# n2 = 7
# sum = py.add(n1, n2)
# print(sum)
#
# diff = py.sub(n1, n2)
# print(diff)

"from module_name import feature"
# from python import add
#
# n1 = 11
# n2 = 7
#
# sum = add(n1, n2)
# print(sum)
#
# # diff = sub(n1, n2)
# # print(diff)


"from module_name import feature as alias"
# from python import add as a
#
# n1 = 11
# n2 = 7
# sum = a(n1, n2)
# print(sum)


"from module_name import *"

# from python import *
# n1 = 11
# n2 = 7
#
# sum = add(n1, n2)
# print(sum)
#
# diff = sub(n1, n2)
# print(diff)


# # New Program
# from math import *
#
# n1 = 5
# n2 = 2
#
# exp = pow(n1, n2)
# print(exp)

# # New Program
# from operator import *
#
# n1 = 5
# n2 = 2
#
# exp = pow(n1, n2)
# print(exp)


# # New Program
# import math as ma
# import operator as op
# import matplotlib.pyplot as plt
#
#
# n1 = 5
# n2 = 2
#
# exp = ma.pow(n1, n2)
# print(exp)
#
# exp1 = op.pow(n1, n2)
# print(exp1)



"""
3. How to access selected code of the program

For this we need to understand a pre-defined variable called __name__
In this variable the name of the file which is being executed is stored

If the file is executed directly, then the name of that file which is stored in this variable
is always '__main__' and if the file is being executed indirectly, then the actual name of the 
file is stored in this variable
"""

"""
4. How to access modules which are not in the current directory

For this we will study the path variable in the sys library
"""


# l = [1, 2, 3, 4]
# print(l)
# l.append(5)
# print(l)


# import sys
# print(sys.path)
#
# sys.path.append(r"E:\Cetpa")
#
# print(sys.path)
#
# import python as py
# n1 = 7
# n2 = 11
# sum = py.add(n1, n2)
# print(sum)

"""
5. How to create .pyc (python compiled) files

Q. What are compiled files?
A. These are the files which are created when our user understandable code is converted into
byte code.


Q. Why are compiled files created?



Q. How are compiled files created in python
A. Using another module called py_compile
"""

# import py_compile
# py_compile.compile('python.py')


# import python
# n1 = 5
# n2 = 11
#
# sum = python.add(n1, n2)
# print(sum)

"""
6. How to use .pyc files?
A. Same as .py files
"""

# import pythonC
# n1 = 5
# n2 = 11
#
# sum = pythonC.add(n1, n2)
# print(sum)



# import pythonC
#
# print(help(pythonC))


"""
7. How to create packages
"""

# from cetpa import *
# from cetpa import module3, module4
#
# n1 = 8
# n2 = 3
#
# remainder = module3.rem(n1, n2)
# print(remainder)
#
# flDiv = module4.floorDiv(n1, n2)
# print(flDiv)


"8. How to download packages"

"""
in command prompt:
pip install package_name
"""




