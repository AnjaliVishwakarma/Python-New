"""Strings in python"""

"""
A string is a datatype in python which stores collection of characters. It is an immutable 
iterable.
"""

# s = '''Welcome to python class'''
# res = s.upper()
# print(s)
# print(res)

# s = "WELCOME TO PYTHON CLASS"
# res = s.lower()
# print(s)
# print(res)

# s = "welCOMe To pytHON cLasS"
# res = s.title()
# print(s)
# print(res)

# s = "welCOMe To pytHON cLasS"
# res = s.swapcase()
# print(s)
# print(res)

# s = "WELCOME TO PyTHON CLASS"
# res = s.isupper()
# print(s)
# print(res)

# s = "WELCOMETOPyTHONCLASS"
# res = s.isalpha()
# print(s)
# print(res)

# s = "WELCOMETOPyTHONCLASS123"
# res = s.isalnum()               # Checks for alpha-numeric characters
# print(s)
# print(res)

# # New Program
# s = "123.56"                    # According to us this is a number, but according to a string
#                                 # . is a special character, nd neither an alphabet nor a number
# res = s.isalnum()               # Checks for alpha-numeric characters
# print(s)
# print(res)


# s = "1235.45"
# res = s.isdecimal()
# print(s)
# print(res)

"""
isdecimal() :   checks if all the characters in the string are numeric

isnumeric() :   It checks if all the character in the string are numeric and also checks 
                for superscripts and subscripts

isdigit()   :   It checks if all the character in the string are numeric and also checks 
                for superscripts and subscripts as well as special numbers like roman number 10
                (X) and fractions like 1/3
"""

# s = "Welcome to python class"
# res = s.count('e', 3, 15)
# print(s)
# print(res)

# s = "Welcome to python class"
# res = s.index('o ', 6)
# print(s)
# print(res)

# s = "Welcome to python class"
# res = s.rindex('o')
# print(s)
# print(res)


# s = "Welcome to python class"
# res = s.find('ome1')
# print(s)
# print(res)


# s = "Welcome to python class"
# res = s.index('ome1')
# print(s)
# print(res)


# s = "Welcome to python class"
# res = s.startswith('Welcome')
# print(s)
# print(res)

# s = "Welcome to python class"
# res = s.endswith('class')
# print(s)
# print(res)

# s = "Welc.om.e to. pyth.on cl.as.s"
# res = s.split(sep = '.', maxsplit = 3)
# print(s)
# print(res)

# s = "Welc.om.e to. pyth.on cl.as.s"
# res = s.rsplit(sep = '.', maxsplit = 3)
# print(s)
# print(res)


# s = "Hello"
# res = s.zfill(8)
# print(s)
# print(res)


# s = "Welcome to python class"
# res = s.split()
# print(res)
# res1 = " ".join(res)
# print(res1)

# s = "Welcome TO Python CLASS"
# res = s.casefold()
# print(res)

# s = "Welcome TO Python CLASS"
# res = s.capitalize()
# print(res)

# s = "      Welcome To Python Class                "
# res = s.strip()
# print(s)
# print(res)

# s = "abccbabccbbacWelcome to python classcbabacbbacbabc"
# res = s.strip('abc')
# print(res)


# s = "Welcome to python class"
# res = s.replace(" ", "##")
# print(res)

# s = "Welc\tome to pyth\ton class"
# res = s.expandtabs(10)
# print(s)
# print(res)

# n = input("Enter your name: ")
# a = int(input("Enter your age: "))
#
# print("Your name is n and your age is a")
# print("Your name is", n, "and your age is", a)
# print(f"Your name is {n} and your age is {a}")
# print("Your name is {} and your age is {}".format(n, a))
# print("Your name is %s and your age is %d"%(n, a))
# print("Your name is {name} and your age is {age}".format(age = a, name = n))


s = r"Welc\tome to python \nyou are at cetpa noida"
print(s)


