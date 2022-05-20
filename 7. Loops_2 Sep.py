"""Loops in python"""

"""
Loops: It is a set of instructions in all the programming languages which is used to execute a 
code repeatedly

In python there are two types of loops: 
1. while loop
2. for loop

The steps to execute a loop:
1. Initialize the loop variable
2. Provide the loop condition
3. Increment in the loop variable



while loop:

Syntax:

Initialize the loop variable
while condition:
    while-loop block of code
    increment in the loop variable


Q. Write a program to print the word 'Hello' 20 times
"""

# i = 0
# while i < 20:
#     print("Hello", i)
#     i+=1            # i = i + 1
#
# print(i)


"""
Q. Write a program to print the table of 5
"""


# i = 1
# while i <= 10:
#     print(5, 'x', i, '=', 5*i)
#     i+=1

"Write a program to print the table of any input number"

# n = int(input("Enter any number: "))
# i = 1
# while i <= 10:
#     print(n, 'x', i, '=', n*i)
#     i+=1

#New Program
# i = 0
# while True:
#     print(i)
#     i+=1


# while True:
#     n1 = int(input("Enter First Number: "))
#     n2 = int(input("Enter Second Number: "))
#
#     choice = input("""
#     Press + for addition
#     Press - for Subtraction
#     Press * for Multiplication
#     Press / for Division
#     Press % for Remainder
#     Press // for Floor Division
#     Press ** for power
#
#     Enter your choice: """)
#
#     if choice == '+':
#         sum = n1 + n2
#         print("The sum of numbers is", sum)
#
#     elif choice == '-':
#         diff = n1 - n2
#         print("The difference of numbers is", diff)
#
#     elif choice == '*':
#         prod = n1 * n2
#         print("The product of numbers is", prod)
#
#     elif choice == '/':
#         quo = n1 / n2
#         print("The quotient is", quo)
#
#     elif choice == '%':
#         rem = n1 % n2
#         print("The Remainder is", rem)
#
#     elif choice == '//':
#         fldiv = n1 // n2
#         print("The floor division is", fldiv)
#
#     elif choice == '**':
#         pow = n1 ** n2
#         print("The exponent of numbers is", pow)
#
#     else:
#         print("Incorrect Choice")
#
#     chYN = input("Do you want to exit, Y/N: ")
#     if chYN == 'Y' or chYN == 'y':
#         break
#
# print("Thanks for using our calculator")


#################

"""
For loop in python: The for loop in python is a special loop which works on iterables only.
It returns the elements of the iterable in the loop variable one by one

Syntax of for loop:


for var in iterable:
    for loop block

"""

# s = "Python"
#
# for e in s:
#     print(e)


# l = [34, 56.84, "Hello", [1, 2, 3, 4]]
#
# for e in l:
#     print(e)



"""
range class in python: This is a class which returns a collection of numbers in the given 
limit.

Syntax:

range(start = 0, stop, step = 1)

range(10)    :      range(start = 0, stop = 10, step = 1) ==> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(2, 10) :      range(start = 2, stop = 10, step = 1) ==> 2, 3, 4, 5, 6, 7, 8, 9
range(2, 10, 3):    range(start = 2, stop = 10, step = 3) ==> 2, 5, 8

"""

# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(2, 10, 3)))


# for i in range(2, 50, 2):
#     print(i)


# for i in range(20):
#     print(i)
#     i+=3


# for i in range(20):
#     i += 3
#     print(i)


# n = 5
#
# for i in range(10):
#     print(n*(i+1))


# for i in range(1, 11):
#     print(n*i)



# s = "Python"
#
# for e in s:
#     print(e)


# s = "Python"
#
# i = 0
# while i < len(s):
#     print(s[i])
#     i+=1


"""
print
input
datatypes
indexing
operators
conditional st
loops
"""


















