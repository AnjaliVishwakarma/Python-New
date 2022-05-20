"""Functions Continued"""

"""
Local and Global Variables

Local variables: These are the variables which are defined inside the functions. The local 
variables can be accessed inside only those functions inside which they are created.
They do not have any existence outside the function in which they are created.

Global Variables: These are the variables which are created outside any function in the program.
They can be accessed anywhere in the program.
"""

# def add():
#     res = a + b
#     print(id(a))
#     print(id(b))
#     return res
#
# a = 4
# b = 5
# c = add()
# print(id(a))
# print(id(b))
# print(c)



# def add(no1, no2):
#     res = no1 + no2
#     print("Value of no1",no1)
#     print("Value of no2",no2)
#     print("Value of res",res)
#     return res
#
# def showData():
#     print("Value of no1", no1)
#     print("Value of no2", no2)
#     print("Value of res", res)
#
# sum = add(4, 5)
# print(sum)
# showData()


# def add(no1, no2):              # Line 1: add func is created, Line 5: no1 = n1, no2 = n2
#     res = no1 + no2             # Line 6
#     return res                  # Line 7: res value is returned
#
# n1 = 7                          # Line 2: n1 var is created
# n2 = 8                          # Line 3: n2 var is created
# sum = add(n1, n2)               # Line 4: add func is called, Line 8: sum = res
# print(sum)                      # Line 9



# def func1():
#     print(a)
#
# a = 8
# func1()
# a = 10
# func1()
# print(a)


# x = 10
# x = 8
# print(x)
# print(x)






def func1():        # Line 1, Line 4
    a = 10          # Line 5
    print(a)        # Line 6

a = 8               # Line 2
func1()             # Line 3
print(a)            # line 7


# def func1():        # Line 1, Line 4
#     global a
#     a = 10          # Line 5
#     print(a)        # Line 6
#
# a = 8               # Line 2
# func1()             # Line 3
# print(a)            # line 7


"""
Types of functions: There are 5 or 6 different types of functions. The only difference in them
is that we provide different type of arguments in them.

They are:

1. Required argument functions
2. Keyword Argument Functions
3. Default Argument Functions
4. Variable Length Argument Functions
5. Variable Length Keyword Argument Functions
6. lambda functions

Note: Some people do not consider lambda functions as a type of functions
"""





























