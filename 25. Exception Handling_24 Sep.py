"""Exception Handling"""

"""
When real world softwares are created, then in those softwares, we always use 
exception handling
This is done to handle the run time errors in the programs

The handling of errors can be done in two ways:

1. Manual Checking: In this process, we carefully input all the values in the program

2. Using pre-defined keywords: There are certain pre-defined keywords in python which are used
to handle the exceptions. These keywords are try, except, finally and raise.
This process of handling the errors using these pre-defined keywords is called exception 
handling
"""

# n1 = int(input("Enter First number: "))
# n2 = int(input("Enter Second number: "))
# res = n1 / n2
# print(res)

# s = "Welcome"
# s[11]

"""
In python there are a lot of different error classes, like:

1. ValueError
2. IndexError
3. ZeroDivisionError
4. NotImplementedError
5. FileNotFoundError
6. ModuleNotFoundError
7. Exception
.
.
.
.
etc.

There are more than 100+ error classes in python and Exception class is the parent class of all
the error classes
"""

"""
try - except keywords

The try keyword is always used in combination with the except keyword.
The code in which we think we might get an error is put inside the try block and the alternate
code to be executed in case there is an error is put in the except block
"""
# while True:
#     try:
#         n1 = int(input("Enter First number: "))
#         n2 = int(input("Enter Second number: "))
#         res = n1 / n2
#         print(res)
#         break
#
#     except:
#         print("Error in the program")


# while True:
#     try:
#         n1 = int(input("Enter First number: "))
#         n2 = int(input("Enter Second number: "))
#         res = n1 / n2
#         print(res)
#         break
#
#     except Exception as err:
#         print("Error", err)


"""
finally keyword: the block of code inside finally is executed in every case no matter what
"""

# while True:
#     try:
#         n1 = int(input("Enter First number: "))
#         n2 = int(input("Enter Second number: "))
#         res = n1 / n2
#         print(res)
#
#     except ValueError:
#         print("The Entered number should be in numerics only")
#
#     except ZeroDivisionError:
#         print("The second number should not be zero")
#
#     except Exception as err:
#         print("Error", err)
#
#     finally:
#         chYN = input("Do you want to perform another operation? Y/N: ")
#         if chYN == 'N' or chYN == 'n':
#             break

"""
raise keyword: This keyword is used to raise errors in the program
"""


# # BLL starts here
#
# def add(no1, no2):
#     res = no1 + no2
#     return res
#
# def sub(no1, no2):
#     res = no1 - no2
#     return res
#
# def mul(no1, no2):
#     res = no1 * no2
#     return res
#
# def floor_div(no1, no2):
#     res = no1 // no2
#     return res
#
# def rem(no1, no2):
#     res = no1 % no2
#     return res
# # BLL ends here
#
# # PL starts here
#
# i = 0
# while i ==0:
#     try:
#         op = input("""Press + for add
#                         Press - for sub
#                         Press * for multiply
#                         Press // for floor div
#                         Press % for remainder
#                         Press ! to terminate the program""")
#
#         n1 = int(input("Enter first number"))
#         n2 = int(input("Enter second number"))
#
#         if op == '+':
#             print(add(n1,n2))
#
#         elif op == '-':
#             print(sub(n1,n2))
#
#         elif op == '*':
#             print(mul(n1,n2))
#
#         elif op == '//':
#             print(floor_div(n1,n2))
#
#         elif op == '%':
#             print(rem(n1,n2))
#
#         elif op == "!":
#             break
#
#         else:
#             raise NotImplementedError
#
#     except ValueError:
#         print("Enter Numerics only")
#
#     except ZeroDivisionError:
#         print("The Entered Number should not be zero")
#
#     except NotImplementedError:
#         print("Enter a valid choice")
#
#     except Exception as err:
#         print("Error", err)


# l1 = [1, 2, 3, 4, 5, 6]
# print(l1[11])


# s = "Welcome"
# print(s[12])

"""
the raise keyword is actually used to provide different error statements to the 
same error class
"""

# BLL starts here

def add(no1, no2):
    res = no1 + no2
    return res

def sub(no1, no2):
    res = no1 - no2
    return res

def mul(no1, no2):
    res = no1 * no2
    return res

def floor_div(no1, no2):
    res = no1 // no2
    return res

def rem(no1, no2):
    res = no1 % no2
    return res
# BLL ends here

# PL starts here

i = 0
while i ==0:

        op = input("""Press + for add
                      Press - for sub
                      Press * for multiply
                      Press // for floor div
                      Press % for remainder
                      Press ! to terminate the program""")

        n1 = input("Enter first number")
        n2 = input("Enter second number")

        if n1.isdecimal() == False:
            raise NotImplementedError("First number should be integer only")

        if n2.isdecimal() == False:
            raise NotImplementedError("Second number should be integer only")

        n1 = int(n1)
        n2 = int(n2)

        if op == '+':
            print(add(n1,n2))

        elif op == '-':
            print(sub(n1,n2))

        elif op == '*':
            print(mul(n1,n2))

        elif op == '//':
            print(floor_div(n1,n2))

        elif op == '%':
            print(rem(n1,n2))

        elif op == "!":
            break

        else:
            raise NotImplementedError("Invalid Choice")

    # except ValueError:
    #     print("Enter Numerics only")
    #
    # except ZeroDivisionError:
    #     print("The Entered Number should not be zero")
    #
    # except NotImplementedError as err:
    #     print("Error", err)
    #
    # except Exception as err:
    #     print("Error", err)