"""Functions continued"""

"""
Pointer: A pointer is a variable which stores the address of value

Function Pointer: A function pointer is a variable which stores the address of a function
"""
# a = 5
# b = 7.84
# c = "Hello"
#
# print(type(a))
# print(type(b))
# print(type(c))

# def add(no1 = 1.5, no2 = 1):
#     res = no1 + no2
#     return res
#
# print(type(add))
# print(add)
#
# x = add
#
# print(type(x))
# print(x)
#
# print(x())

"""
The name of the function that we provide acts as a variable of the function
"""

"""
Types of functions: As we discussed yesterday, functions are of 6 types::

1. Required Argument Functions / Positional Argument Functions
2. Keyword Argument Functions
3. Default Argument Functions
4. Variable Length Argument Functions
5. Variable Length Keyword Argument Functions
6. Lambda Functions
"""

"""
1. Required Argument Functions: These are the functions in which we have to provide as many 
actual arguments while calling the function as there are the formal arguments and they have to 
provided in the same order.
"""

def add(no1, n3=6, no2=1):
    print(no1, no2)
    res = no1 + no2
    return res

sum = add(5, 7)
print(sum)

"""
2. Keyword Argument Functions: These are the functions in which we have to provide as many 
actual arguments while calling the function as there are the formal arguments. But they can be 
provided in different order.
"""

# def add(no1, no2):
#     print(no1, no2)
#     res = no1 + no2
#     return res
#
# sum = add(no2 = 5, no1 = 7)
# print(sum)

"""
3. Default Argument Functions: In these functions we provide some default value to the 
formal arguments while creating the function. Now, it is not mandatory for us to provide 
values in the actual arguments.
In case we provide values in the actual arguments, then our values are given priority and they
are considered, otherwise the default values are considered
"""

# def add(no1 = 1, no2 = 1):
#     print(no1, no2)
#     res = no1 + no2
#     return res
#
# sum = add(7, 11)
# print(sum)


"""
4. Variable Length Argument Functions: Here we can provide as many positional arguments as we 
want. These functions are tuple based. In these functions we provide a single tuple 
type argument and all the values are saved in that tuple
"""

# def func1(*t):
#     print(t)
#
#
# func1(1, 2, 3)
# func1()
# func1("Hello", "Welcome", 9, 78, 51, 63.54)

"""
Python recommends that the argument of Variable Length Argument Function should be named 
'args'

add function using variable length arguments
"""

# def add(*args):
#     res = 0
#     for no in args:
#         res+=no
#
#     return res
#
# sum1 = add(1, 2, 3, 4, 5)
# print(sum1)
#
# sum2 = add(2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10)
# print(sum2)
#
# sum3 = add(100, 200, 300, 400, 500, 600, 700, 800)
# print(sum3)


"""
5. Variable Length Keyword Argument Functions: Here we can provide as many keyword arguments as 
we want. It is dictionary based
"""

# def func1(**d):
#     print(d)
#
# func1(no1 = 1, no2 = 2, no3 = 3, no4 = 4)
# func1(a = "Hello", b = "Welcome", c = "Python")
# func1()

"""
Python prefers to call the argument of variable length keyword argument functions as 'kwargs'

add function using variable length keyword arguments
"""

# d1 = {'no1': 1, 'no2': 2, 'no3': 3, 'no4': 4}
# print(d1)
#
# print(d1.values())


# def add(**kwargs):
#
#     res = 0
#     for no in kwargs.values():
#         res+=no
#
#     return res
#
# sum1 = add(no1 = 1, no2 = 2, no3 = 3, no4 = 4, no5 = 5)
# print(sum1)
#
# sum2 = add(a = 2.2, b = 3.3, c = 4.4, d = 5.5, e = 6.6, f = 7.7, g = 8.8, h = 9.9, i = 10)
# print(sum2)
#
# sum3 = add(m = 100, n = 200, o = 300, p = 400, q = 500, r = 600, s = 700, t = 800)
# print(sum3)

"""
6. Lambda functions: These are single lined anonymous functions which return the value of the 
expression that they calculate

Syntax: 

lambda arguments: expression
"""

# x = lambda no1, no2: no1 + no2
#
# y = lambda no1, no2: no1 - no2
#
# print(x(4, 5))
#
# print(y(8, 2))






