"""JSON and Pickling"""

"""
We use file handling to permanently store data on the hard drive for personal use.

But sometimes, it is possible that the data that we have saved is required by some other 
developer to use in his/her software.
In this case, we will need to share our data files with that other developer.
But to share the data files with other developers, we first save the data in JSON or Pickle 
format

Pickling: Pickling is python internal standard used to share data between two python 
applications
Here data is saved in the form of bytes

JSON: JSON is the common standard to share data between any two types of applications.
It can be between one Java and other python program, or it can be between a python 
and a C++ program or between a PHP and R program

JSON: Java Script Object Notation
Here data is saved in the form of JSON Objects

[{'roll': '1', 'name': 'Aakash', 'age': 17, 'marks': 84},
{'roll': '2', 'name': 'Abhay', 'age': 16, 'marks': 89}, 
{'roll': '3', 'name': 'Ayushi', 'age': 17, 'marks': 95},
.
.
.
.]

[] ---> array
{} ---> object
"""

# # New Program
# import pickle
# data =[54, 3.64, 98.6574, "Hello", "Welcome", 45.210025, [1, 2, 3, 4]]
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\pickle.txt", 'wb')
# pickle.dump(data, f)
# f.close()


# # New Program
# import pickle
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\pickle.txt", 'rb')
# data = pickle.load(f)
# print(data)
# f.close()


# # New Program
# import json
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\json.txt", 'w')
# data = [54, 3.64, 98.6574, "Hello", "Welcome", 45.210025, [1, 2, 3, 4]]
# json.dump(data, f)
# f.close()


# # New Program
# import json
# f = open(r"C:\Personal\Jai\Programming\Cetpa\Python\Python 18 Aug Batch\json.txt", 'r')
# data = json.load(f)
# print(data)
# f.close()


"""
Delegation: Using delegation model, we can leave a scope in a function to add some new 
functionalities to it in the future


l1 = [32, 12, 56, 42, 10, 35, 60, 24, 22, 20, 18]
l1 = [12, 32, 56, 42, 10, 35, 60, 24, 22, 20, 18]
l1 = [10, 32, 56, 42, 12, 35, 60, 24, 22, 20, 18]
l1 = [10, 12, 56, 42, 32, 35, 60, 24, 22, 20, 18]
l1 = [10, 12, 42, 56, 32, 35, 60, 24, 22, 20, 18]
l1 = [10, 12, 32, 56, 42, 35, 60, 24, 22, 20, 18]
l1 = [10, 12, 24, 56, 42, 35, 60, 32, 22, 20, 18]
.
.
.
.
l1 = [10, 12, 18, 20, 22, 24, 32, 35, 42, 56, 60]
"""
# Developer 1
# def mySort(L):
#     for i in range(len(L)):
#         for j in range(i+1, len(L)):
#             if L[i]>L[j]:
#                 L[i], L[j] = L[j], L[i]
#
#
# l1 = [32, 12, 56, 42, 10, 35, 60, 24, 22, 20, 18]
# mySort(l1)
# print(l1)


# Developer 2
def mySort(L, key = None):
    if key == None:
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                if L[i] > L[j]:
                    L[i], L[j] = L[j], L[i]

    else:
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                if key(L[i]) > key(L[j]):
                    L[i], L[j] = L[j], L[i]

def inverse(e):
    if e == 0:
        return 0
    else:
        return 1/e

def square(e):
    return e**2

def negative(e):
    return -e

# l1 = [32, 12, 56, 42, 10, 35, 60, 24, 22, 20, 18]
# mySort(l1, key = inverse)
# print(l1)

l1 = [32, 12, -56, -42, 10, 35, 60, -24, 0, 22, -20, 18]
mySort(l1, key = negative)
print(l1)

# def add(no1 = 1, no2 = 1):
#     res = no1 + no2
#     return res
#
# add()
#
# x = add
# x()


