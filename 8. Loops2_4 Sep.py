"""Loops Contd."""


"""
ASCII Encoding: Every character has been provided with a special code into which it is converted
first, and then read by the machine

A   :   65                      a   :   97
B   :   66                      b   :   98
C   :   67                      c   :   99
.
.
.
.
Z   :   90                      z   :   122
"""

"""
ord() function: This function takes one str type character as an input and provides its 
integer type ASCII code as an output
"""

# code = ord('A')
# print(code)

"""
chr() Function: This function takes one int type ASCII code as an input and provides the 
corresponding str type character
"""

# code = ord('A')
# print(code)
#
# char = chr(code)
# print(char)

# # New Program
#
# inp_str = input("Enter a string: ")
#
# i = 0
# while i < len(inp_str):
#     char = inp_str[i]
#     code = ord(char)
#
#     if code >= 65 and code <= 90:
#         print("character", char, "at index", i, "is a capital character")
#
#     elif code >= 97 and code <= 122:
#         print("character", char, "at index", i, "is a small character")
#
#     else:
#         print("character", char, "at index", i, "is not an English alphabet")
#
#     i+=1

"""
Q. Write a program to convert all characters of an input string into upper case
"""

# inp_str = input("Enter a string: ")
# res_str = ''
#
# for e in inp_str:
#
#     code = ord(e)
#
#     if code >= 97 and code <= 122:
#         code-=32
#
#     char = chr(code)
#     res_str+=char
#
# print(res_str)


# inp_str = input("Enter a string: ")
# res_str = ''
#
# for e in inp_str:
#
#     code = ord(e)
#
#     if code >= 65 and code <= 90:
#         code+=32
#
#     char = chr(code)
#     res_str+=char
#
# print(res_str)



# inp_str = input("Enter a string: ")
# res_str = ''
#
# i = 0
# while i < len(inp_str):
#     e = inp_str[i]
#     code = ord(e)
#
#     if code >= 97 and code <= 122:
#         code-=32
#
#     elif code >= 65 and code <=90:
#         code +=32
#
#     char = chr(code)
#     res_str+=char
#     i+=1
#
# print(res_str)


# s = 'welCOMe to PYthon clAss'
# s1 = s.title()
# print(s1)


"""
Write a program to convert the input string into title case:
"""

inp_str = input("Enter a string: ")
res_str = ''


i = 0
while i < len(inp_str):
    char = inp_str[i]
    code = ord(char)

    if i == 0:
        if code >= 97 and code <= 122:
            code-=32

    else:
        if ord(inp_str[i-1]) == 32:
            if code >= 97 and code <= 122:
                code -= 32

        else:
            if code >= 65 and code <= 90:
                code += 32

    char = chr(code)
    res_str += char
    i+=1

print(res_str)










