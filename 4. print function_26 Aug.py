"""print function in python"""

"""
The print function in python is used to provide an output to the user in CUI programs

The print function prints the values of all the arguments that we have provided it with

Q. How many arguments can be provided to the print function?
A. We can provide as many arguments as we like, it will print the values of all of them

Q. What type of arguments can be provided to the print function?
A. We can provide any type of arguments. We can provide variables, values, functions, classes,
conditions, methods, loops, etc.....


Syntax to use print function:
print(comma separated arguments)
"""

# a = 7
# b = 98.6
# c = "Hello"
#
# print(a,b,c,"Welcome",87,36.45,type(a),len(c),range(10),a==b)

"""
Escape Characters: These are some special characters in any programming
language, which when printed, do not appear on the screen, rather we 
can see their effect on the screen

Examples:

\n :    New Line Character: Whenever the new line character is present in the string, it 
        will take the program into a new line
\t :    Tab Character: Whenever the tab character is present, it will provide a tab 
        space in the program 
"""

# s1 = "Welcome to python class"
# print(s1)
# print()
# s2 = "Welc\tome to pyt\nhon class"
# print(s2)

"""
Q1. Whenever we are using the print function then the values of the arguments are separated
with spaces instead of commas, How?

Q2. How does the program go into a new line after the last argument is printed?

Q3. How to print the values of arguments vertically?



A More advanced syntax of print function:

print(comma separated arguments, sep = ' ', end = '\n')


sep: The separator argument is printed after the value of each and every argument is printed
except the last argument

end: end is printed after the last argument has been printed


Default Arguments: These are the arguments of a function to which some values are provided
when the function is created
If we do not provide any value to the default arguments, then their default values are 
considered, but if we provide some values to those arguments, then our values will be given 
priority and they wil be considered
"""


# a = 7
# b = 98.6
# c = "Hello"
# 
# print(a,b,c,"Welcome",87,36.45,type(a),len(c),range(10),a==b, sep = '', end = '')

"""
Q. Use 5 variables a, b, c, d and e with values 2, 3, 4, 5 and 6 respectively 
and write a 
program to give the following output:

4#5@2%3^6Hello

"""

# a, b, c, d, e = 2, 3, 4, 5, 6
#
# print(c, d, sep = '#', end = '@')
# print(a, b, sep = '%', end = '^')
# print(e, end = 'Hello')

"""
Output:

6Hello3*2!4$5&^
"""
# a, b, c, d, e = 2, 3, 4, 5, 6
#
# print(e, b, sep = 'Hello', end = '*')
# print(a, c, sep = '!', end = '$')
# print(d, end = '&^')


"""
output:


4@5^

2!3&

6Hello@
"""

# a, b, c, d, e = 2, 3, 4, 5, 6
#
# print(c, d, sep = '@', end = '^\n\n')
# print(a,b, sep = '!', end = '&')
# print()
# print()
# print(e, end = 'Hello@')

