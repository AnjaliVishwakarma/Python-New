"""input function in python"""

"""
The input function in python is used to take input values from the user
"""

# n1 = 5
# n2 = 78
# sum = n1 + n2
# print(sum)

"""
Whenever we are studying a function then we should know 3 things about it:

1. How to call / use that function ?

2. What type of and how many arguments can a function take ?

3. What does the function return ?


Input function:

1. How is the input function called?
A. By using the input keyword and providing a () after it

2. How many and what type of arguments does it take?
A. It takes a single str type argument

3. What does it return?
A. It returns the value provided by the user in str format

Syntax of input function:

var_name = input(string)


"""

# n1 = input("Enter First Number: ")
# n2 = input("Enter Second Number: ")
#
# print(type(n1))
# print(type(n2))
#
# sum = n1 + n2
# print("The sum of numbers is:", sum)

"""
Typecasting: It is a process in which the values of one data type are 
converted into another data type

Syntax:

var_name = target_class(data_source)
"""

# n1 = input("Enter First Number: ")
# n2 = input("Enter Second Number: ")
#
# print(type(n1))
# print(type(n2))
#
# n1 = int(n1)
# n2 = int(n2)
#
# print(type(n1))
# print(type(n2))
#
# sum = n1 + n2
# print("The sum of numbers is:", sum)


n1 = float(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))

print(type(n1))
print(type(n2))

sum = n1 + n2
print("The sum of numbers is:", sum)





