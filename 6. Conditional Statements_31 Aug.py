"""Conditional Statements"""

"""
Before studying conditional statements, we are going to study types of statements in python

Types of statements in python:

1. Normal Statements: These are the statements which are written outside any condition, function
class, method or loop. They are always written at 0 indentation

2. Headings: These are the statements in which we define a class, condition, function, method or 
loop. They are also generally written at 0 indentation

3. Suites: These are the statements which are written inside a heading. They are written at
1 or more indentation
"""
#
# n1 = int(input("Enter first number: "))     # Normal Statement
# n2 = int(input("Enter second number: "))    # Normal Statement
#
# if n1 >= n2:                                # Heading
#     print("n1 is the greater number")       # Suite
#
# else:                                       # Heading
#     print("n2 is the greater number")       # Suite

"""
Conditional Statements: These are the statements in any programming language which are 
executed only when a certain condition comes out to be true 

The conditional statements in python are created with the help of 3 keywords:
1. if
2. else
3. elif


1. if keyword: Using the if keyword we can provide a condition and it is checked. 
The block of code written inside the if condition is executed only when the condition comes out
to be true.

Note: The if statement can either be used individually or it can be used in combination with
else and elif statements

Syntax:

if (condition):
    if block of code
        
        OR
        
if condition:
    if block of code

"""
"""
Q. Write a program to tell if the given input number is even
"""

# n = int(input("Enter a number: "))
#
# if n%2 == 0:
#     print("The number is even")
#
# print("Program terminated")

"""
2. else keyword: It is always used in combination with if keyword. We do not provide any 
condition with else. In case the condition provided in the if block comes out to be false, then
the else block is executed 

Q. Write a program to determine if the given input number is even or odd
"""

# n = int(input("Enter a number: "))
#
# if n%2 == 0:
#     print("The number is even")
#
# else:
#     print("The Number is odd")
#     print("We have checked the number")
#     print("Welcome to python class")
#
# print("Program Terminated")


"""
3. elif keyword: It is always used in combination with the if keyword. In case we want to check 
for multiple conditions, then we use the elif keyword

Syntax:

elif condition:
    elif block of code
    
Note: Order of using if-elif-else

if condition:
    if block of code
    
elif condition:
    elif block of code
    
elif condition2:
    elif block of code
.
.
.
.

else:
    else block of code
        

"""

# num = int(input("Enter any number between 1 to 6: "))
#
# if num == 1:
#     print("Go to study")
#
# elif num == 2:
#     print("Go to a mall")
#
# elif num == 3:
#     print("Buy a dress")
#
# elif num == 4:
#     print("Watch Netflix")
#
# elif num == 5:
#     print("Go to an adventure park")
#
# elif num == 6:
#     print("Go with your friends")
#
# else:
#     print("Tumse na ho payega. So Jao!!")
#
# print("Program Terminated")



# num = int(input("Enter any number between 1 to 6: "))
#
# if num == 1:
#     print("Go to study")
#
# elif num == 2:
#     print("Go to a mall")
#
# elif num == 3:
#     print("Buy a dress")
#
# elif num == 4:
#     print("Watch Netflix")
#
# elif num == 5:
#     print("Go to an adventure park")
#
# elif num == 6:
#     print("Go with your friends")
#
# else:
#     print("Tumse na ho payega. So Jao!!")
#
# print("Program Terminated")


"""
Write a program to create a calculator
"""

# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))
#
# choice = input("""
# Press + for addition
# Press - for Subtraction
# Press * for Multiplication
# Press / for Division
# Press % for Remainder
# Press // for Floor Division
# Press ** for power
#
# Enter your choice: """)
#
# if choice == '+':
#     sum = n1 + n2
#     print("The sum of numbers is", sum)
#
# elif choice == '-':
#     diff = n1 - n2
#     print("The difference of numbers is", diff)
#
# elif choice == '*':
#     prod = n1 * n2
#     print("The product of numbers is", prod)
#
# elif choice == '/':
#     quo = n1 / n2
#     print("The quotient is", quo)
#
# elif choice == '%':
#     rem = n1 % n2
#     print("The Remainder is", rem)
#
# elif choice == '//':
#     fldiv = n1 // n2
#     print("The floor division is", fldiv)
#
# elif choice == '**':
#     pow = n1 ** n2
#     print("The exponent of numbers is", pow)
#
# else:
#     print("Incorrect Choice")

"""
Write a program to determine the greatest of 3 input numbers
"""

# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))
# n3 = int(input("Enter Third Number: "))
#
# if n1 > n2:
#     if n1 > n3:
#         print("n1 is the greatest")
#     else:
#         print("n3 is the greatest")
#
# else:
#     if n2 > n3:
#         print("n2 is greatest")
#     else:
#         print("n3 is greatest")



# # New Program
# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))
#
# if n1 >= n2:
#     print("n1 is greater")
#
# else:
#     print("n2 is greater")


