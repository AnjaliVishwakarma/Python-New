"Regular Expressions"

"""
RE is a small programming language which is used to find out patterns from the strings.
It has integrations with other programming languages through libraries 
"""

# # New Program
# import re
# s = """ nsdljnf 34597 hjaks anurag@xyz.org m 'almf charukalra01@hotmail.com ang35 sfaat@abc.in
# jai@cetpa.com s;jrntg462 anc1@gmail.com"""
# p = r"\w+@\w+[.]\w+"
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = "Welcome to cetpa infotech. cetpa is a training company. you are at cetpa noida center"
# p = 'cetpa'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = """Pranaam, hum hai akhandanand tripathi.
# Pehle tum vyaapari akhandanand se mile the
# Aj baahubali akhandanand se mil rahe ho"""
# p = "akhandanand"
# res = re.findall(p, s)
# print(res)


"""
Metacharacters:


^       : cap / caret / hat             Done
$                                       Done
*                                       Done
+                                       Done
?                                       Done
.                                       Done
[]      : character matcher class       Done
{}      : quantity matcher class        Done
()      : group matcher class
|                                       Done
\                                       Done


The patterns in RE are of 4 types:
1. Character Matching Patterns
2. Quantity Matching Patterns
3. Location matching Patterns
4. Group matching patterns


1. Character Matching Patterns: Character Matcher Class []
In character matching patterns, the characters which are provided inside the character matcher 
class are found out one at a time using ORing technique 

"""

# # New Program
# import re
# s = "Welcome to cetpa"
# p = r'[cetpa]'
# res = re.findall(p, s)
# print(res)

"""
[abcd]          :   It will find out any character either a or b or c or d
[a-d]           :   It will find out any character either a or b or c or d
[a-z]           :   It will find out any lower case alphabet using OR
[A-Z]           :   It will find out any upper case alphabet using OR
[0-9]           :   It will look for digits using OR
[a-zA-Z]        :   It will look for all alphabets using OR
[a-zA-Z0-9_]    :   It will look for all alphanumeric characters using OR

Note: RE considers _ to be an alphanumeric character
"""

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[abcd]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[a-d]'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[a-z]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[A-Z]'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[0-9]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[a-zA-Z]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[a-zA-Z0-9_]'
# res = re.findall(p, s)
# print(res)


"""
[^abcd]         :   It will search for everything except a or b or c or d
[^a-d]          :   It will search for everything except a or b or c or d
[^a-z]          :   It will search for everything except lower case alphabet using OR
[^A-Z]          :   It will search for everything except upper case alphabet using OR
[^0-9]          :   It will search for everything except digits using OR
[^a-zA-Z]       :   It will search for everything except alphabets using OR
[^a-zA-Z0-9_]   :   It will search for everything except alphanumeric characters using OR
"""

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[^abcd]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[^a-d]'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[^a-z]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[^A-Z]'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[^0-9]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[^a-zA-Z]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[^a-zA-Z0-9_]'
# res = re.findall(p, s)
# print(res)


"""
[0-9]           :   \d      :   digits
[^0-9]          :   \D      :   not digits
[a-zA-Z0-9_]    :   \w      :   words
[^a-zA-Z0-9_]   :   \W      :   not words
.               :   Everything except new line character
\s              :   It searches for all the white spaces
\S              :   It searches for everything except the white spaces
"""

"""
2. Quantity Matching Patterns: Quantity Matcher Class {}
Note: The quantity Matching patterns are always used in combination with character 
matching patterns
There are two ways of using them:

First Way

{m}         :   It will search for a patterns containing exactly m number of characters
{m, n}      :   It will search for a patterns containing min m and max n characters
{m,}        :   It will search for a patterns containing min m characters
{,n}        :   It will search for a patterns containing max n characters

"""


# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'[a-zA-Z0-9_]{4}'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'\w{4}'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome 1234 @#456 to \tCET\npa 634'
# p = r'\w{2,7}'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome alkrasdrnlkt1234 @#456 h to \tCET\npa 634'
# p = r'\w{2,}'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'welcome alkrasdrnlkt1234 @#456 h to \tCET\npa 634'
# p = r'\w{1,7}'
# res = re.findall(p, s)
# print(res)

"""
1. User Name    :   alphanumeric with min 1 character
2. @ symbol
3. Domain Name  :   alphanumeric with min 1 character
4. . symbol
5. Website type :   alphanumeric with min 1 character

"""


# # New Program
# import re
# s = """ nsdljnf 34597 hjaks anurag@xyz1.org m 'almf charukalra01@hotmail.com ang35
# sfaat@abc.co.in jai.chitkara@cetpa.com s;jrntg462 abc.xyz1@gmail.co.xyz"""
# p = r'\w{1,}@\w{1,}\.\w{1,}'
# res = re.findall(p, s)
# print(res)

"""
Second Way

*   :   It will search for a patterns containing min 0 characters   :   {0,}
+   :   It will search for a patterns containing min 1 characters   :   {1,}   
?   :   It will search for a pattern with either 0 or 1 characters  :   {0,1}
"""


# # New Program
# import re
# s = """ nsdljnf 34597 hjaks anurag@xyz1.org m 'almf charukalra01@hotmail.com ang35
# sfaat@abc.co.in jai.chitkara@cetpa.com s;jrntg462 abc.xyz1@gmail.co.xyz"""
# p = r'\w+[.]?\w*@\w+[.]\w+[.]?\w*'
# res = re.findall(p, s)
# print(res)


"""
3. Location Matching Patterns: They help us to find out a given pattern at a location

^   :   It is used to find a pattern at the beginning of the string
$   :   It is used to find a pattern at the end of the string
"""


# # new Program
# import re
# s = "Anurag kapil gyanendra anshikakartik shruti Anurag"
# p = r'^Anurag'
# res = re.findall(p, s)
# print(res)


# # new Program
# import re
# s = "Anurag kapil gyanendra anshikakartik shruti Anurag"
# p = r'Anurag$'
# res = re.findall(p, s)
# print(res)


# # new Program
# import re
# s = "Anurag kapil gyanendra anshikakartik shruti Anurag"
# p = r'^Anurag$'
# res = re.findall(p, s)
# print(res)


# # new Program
# import re
# s = "Anurag"
# p = r'^Anurag$'
# res = re.findall(p, s)
# print(res)



# New Program
import urllib.request as rq
import re
f = rq.urlopen("https://www.nistinstitute.com/contact_us.php")
data = f.read()
# print(data)
print(type(data))
data = str(data)
print(type(data))

pMob = r'\d{10}'
mobData = re.findall(pMob, data)
print(mobData)
print(len(mobData))
mobData = set(mobData)
print(mobData)
print(len(mobData))
#
# pemail = r'\w+[.]?\w*@\w+[.]\w+[.]?\w*'
# emailData = re.findall(pemail, data)
# print(emailData)
# print(len(emailData))
# emailData = set(emailData)
# print(emailData)
# print(len(emailData))
#
# pData = r'\w+[.]?\w*@\w+[.]\w+[.]?\w*|\d{10}'
# Data = re.findall(pData, data)
# print(Data)
# print(len(Data))
# Data = set(Data)
# print(Data)
# print(len(Data))

"""
Group Matching Patterns: Group Matcher Class ()
"""

# # New PRogram
# import re
# s = "123_ 23456_ 12_ 9874_"
# p = r'(\d{2})_'
# res = re.findall(p, s)
# print(res)









