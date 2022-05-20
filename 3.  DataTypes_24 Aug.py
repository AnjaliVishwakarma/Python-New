"""Data Types"""

"""
Data Types are a technique, using which the language determines how much amount of 
memory is required by a variable / value to be saved in the Memory

Similar values are grouped under similar data types and then each data type is assigned a 
fixed value of memory that it will need to be saved in the memory

5, 78, 1025, 36521564, 875132184, -78, -523, -75103

51354.541. -520354.131, 54.23, -65.451

"""

# a = 5
# b = 45.87
# c = "Hello"

"""
In python there are a lot of data types:

int         :   it stores integer type values
float       :   It stores decimal values
str         :   It stores collection of character or individual characters
list        :   It is a data type which can store multiple heterogeneous data types
tuple       :   It is a data type which can store multiple heterogeneous data types
dictionary  :   It can also store multiple heterogeneous data types but in key-value pairs
set         :   It can store multiple unique heterogeneous values
frozen set  :   It can store multiple unique heterogeneous values
NoneType    :   It stores None Values
bool        :   It stores boolean values (True , False)
etc...
"""

# a = 7
# b = 12.65
# c = "Welcome to python class"
# d = [54, 65.98, "Welcome", [1, 2, 3, 4]]
# e = (54, 65.98, "Welcome", [1, 2, 3, 4])
# f = {'roll': 10, 'name': "Aniket", 'age':15, 'mob': 1234}
# g = {5, 2, 3.65, 5, "Welcome", "Hello", "Welcome"}
# h = None
# i = True
# j = False
#
# # print(g)
#
# print("Data type of a:", type(a))
# print("Data type of b:", type(b))
# print("Data type of c:", type(c))
# print("Data type of d:", type(d))
# print("Data type of e:", type(e))
# print("Data type of f:", type(f))
# print("Data type of g:", type(g))
# print("Data type of h:", type(h))
# print("Data type of i:", type(i))
# print("Data type of j:", type(j))



"""
Classification of data types:
In python data types are divided into two groups:

    1. Single Valued data types: They are the data types which store single values only.
    Example: int, float, NoneType, bool
    
    2. Multi valued data types (iterables): These are the data types which store multiple 
    values in them. These are some special data types on which the for loop of python can 
    be applied
    Examples: str, list, tuple, dict, set, frozen set, etc.
    
    The iterables are further divided into two categories:
        a. mutable iterables: These are the iterables in which the values at particular indexes
        can be changed using the technique of indexing even after they are created
        Examples: list, dict, set, etc.
        
        b. immutable iterables: These are the iterables in which the values cannot be 
        changed using indexing once they are created.
        Examples: str, tuple, frozen set, etc.


Indexing:
This is a technique, using which we can access the element present at a particular index

Syntax:
var_name[index_number]

"""

# x = "Welcome"
#
# print(x[4])


# l = [5, 7.69, "Welcome", 54, "Hello", 3000012.5478]
# print(l)
# l[3] = 5000
# print(l)


# s = "WELcOME"
# print(s)
# s[3] = 'C'
# print(s)


"""
Strings in python: it is an iterable data type which can store multiple characters in it and 
it is immutable in nature

Q. Are there any different types of strings?
A. Yes, there are two types of strings:

    1. Single lined strings: These are the strings which start in the same line and end in the
    same line. They can be created in 4 ways:
        
        a. Using single quotes ('')
        b. Using double quotes ("")
        c. Using triple single quotes ('''''')
        d. Using triple double quotes ("""""")
    
    
    2. Multi lined strings: These are the strings which start in one line, but end in some
    other line
    They can be created in two ways:

        a. Using triple single quotes ('''''')
        b. Using triple double quotes ("""""")

"""

# s1 = "Welcome to python class"          # Single Lined String
#
# s2 = 'Welcome to python class'
#
# s3 = """Welcome to python class"""
#
# s4 = '''Welcome to python class'''
#
# s5 = '''Welcome to python class
# You are at CETPA Noida'''
#
# s6 = """Welcome to python class
# You are at CETPA Noida"""

"""
Ctrl + /
"""


"""
Comments in python: Comments in any programming language are the lines in the code which we 
do not wish to execute with the main code.

How are comments created?
There are two ways:

1. Official Way: Provide a '#' symbol before every line you want to comment


2. Unofficial Way: Write the lines you want to comment inside a string and DO NOT provide a 
variable to that string
"""

















