"""Functions"""

"""
Functions: A function is a set of code which is used to perform a specific task repeatedly

Uses of functions:
1. It increases the re-usability of code
2. It makes the code scalable
3. Functions are the building blocks of layered approach of programming
4. Functions are the building blocks of modular approach of programming
"""

# n1 = 1
# n2 = 3
# n3 = float(n1) + float(n2)
# print(n3)
#
#
# a = 78
# b = 9
# c = float(a) + float(b)
# print(c)
#
#
# m = 11
# n = 12
# p = float(m) + float(n)
# print(p)

"""
Syntax to create a function:

def functionName(arguments):
    lines of code
    return expression
    
Note: It is not mandatory to provide a return statement
"""

# def add(no1, no2):              # no1, no2 are formal arguments; no1 = n1, no2 = n2,
#     res = float(no1) + float(no2)
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
# n1 = 1
# n2 = 3
# n3 = add(n1, n2)                     # actual arguments
# print(n3)
#
# a = 78
# b = 9
# c = sub(a, b)
# print(c)
#
#
# m = 11
# n = 12
# r = mul(m, n)
# print(r)
#
#
# import file
# x = 45
# y = 3
# z = file.div(x, y)
# print(z)



"""
A software has 2 parts:

1. Business Logic Layer (BLL): In this layer the while code of the program is written

2. Presentation Layer (PL): It takes input from the user and provides output to the user.
Apart from this it uses several functionalities of the BLL based on the input provided by the 
user

"""

# Calculator using functions

# BLL Starts Here

def add(no1, no2):
    res = no1 + no2
    return res

def sub(no1, no2):
    res = no1 - no2
    return res

def mul(no1, no2):
    res = no1 * no2
    return res

def div(no1, no2):
    res = no1 / no2
    return res

# BLL Ends Here

# PL Starts Here
while True:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    choice = input("""
    Press + for addition
    Press - for Subtraction
    Press * for multiplication
    Press / for Division
    
    Enter your choice: """)

    if choice == '+':
        sum = add(n1, n2)
        print("The sum of numbers is", sum)

    elif choice == '-':
        diff = sub(n1, n2)
        print("The difference of numbers is", diff)

    elif choice == '*':
        prod = mul(n1, n2)
        print("The product of numbers is", prod)

    elif choice == '/':
        quo = div(n1, n2)
        print("The quotient is", quo)


    else:
        print("Incorrect Choice")

    chYN = input("Do you want to continue, Y/N: ")
    if chYN == 'n' or chYN == 'N':
        print("Thanks for using our calculator")
        break


# PL Ends Here


















