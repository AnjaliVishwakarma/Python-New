"""OOPS Contd"""

"""
Today we are going to study about a special method which is present in every class.

That method is called the __init__() method
This method is the constructor of the class in which it is present

The constructor helps to create the object of the class

The constructor method is called automatically when the statement to create the object of a 
class is executed
"""

# # New Program
# class C1:
#
#     def __init__(self):
#         print("Constructor is called")
#
# ob = C1()

# # New Program
# class C1:
#     def __init__(self):
#         self.a = 5
#         self.b = 7
#
#     def showData(self):
#         print(self.a, self.b)
#
#
# ob = C1()
# ob.showData()

# def func1():
#     print("This is func1")
#
# def func1():
#     print("You are in func1")
#
# func1()

# # New Program
# class C1:                       # Line 1
#     def __init__(self):         # Line 2, Line 6: self = ob1, Line 10: self = ob2
#         self.a = 5              # Line 7, Line 11
#         self.b = 7              # Line 8, Line 12
#
#     def incData(self):          # Line 3, Line 14, self = ob1
#         self.a += 3             # Line 15
#         self.b += 11            # Line 16
#
#     def showData(self):         # Line 4, Line 18: self = ob1, Line 21: self = ob2
#         print(self.a, self.b)   # Line 19
#
#
# ob1 = C1()                      # Line 5
# ob2 = C1()                      # Line 9
# ob1.incData()                   # Line 13
# ob1.showData()                  # Line 17
# ob2.showData()                  # Line 20



"""
There are some special properties of OOPS:

Abstraction

Encapsulation: Making Capsules

Inheritance: It is a property of classes in which one class can use / inherit the properties
of another class.
Here the concept of parent and child is used.
"""

# class C1:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     pass
#
# ob = C2()
# print(ob.a, ob.b)
# ob.showData()

# # New Program
# class C1:
#     def __init__(self):
#         self.a = 2
#         self.b = 3
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 4
#         self.d = 5
#         super().__init__()
#
# ob = C2()
# ob.showData()
# print(ob.a, ob.b, ob.c, ob.d)


"""
Types of Inheritance:

1. Single Level Inheritance
2. Multi Level Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance 1
6. Hybrid Inheritance 2
"""

"""
MultiLevel Inheritance
"""

# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     # def showData(self):
#     #     print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#     # def showData(self):
#     #     print("This is class C2")
#
# class C3(C2):
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#         super().__init__()
#
#     # def showData(self):
#     #     print("This is class C3")
#
#
# ob = C3()
# print(ob.a, ob.b, ob.c, ob.d, ob.e, ob.f)
# ob.showData()

"""
Note: In python, there is a class called the 'object' class. This class is by default
the parent class of eah and every other class, either user-defined or pre-defined
"""
"""
Hierarchical Inheritance:
"""
# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#     def showData(self):
#         print("This is class C2")
#
# class C3(C1):
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#         super().__init__()
#
#     def showData(self):
#         print("This is class C3")
#
# class C4(C1):
#     def __init__(self):
#         self.g = 7
#         self.h = 8
#         super().__init__()
#
#     def showData(self):
#         print("This is class C4")
#
#
# ob = C4()
# print(ob.a, ob.b, ob.g, ob.h)
# ob.showData()

"Multiple Inheritance"
# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2:
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#     def showData(self):
#         print("This is class C2")
#
# class C3:
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#         super().__init__()
#
#     def showData(self):
#         print("This is class C3")
#
# class C4(C1, C2, C3):
#     def __init__(self):
#         self.g = 7
#         self.h = 8
#         super().__init__()
#         C2.__init__(self)
#         C3.__init__(self)
#
#     def showData(self):
#         print("This is class C4")
#
#
# ob = C4()
# print(ob.a, ob.b, ob.c, ob.d, ob.e, ob.f, ob.g, ob.h)
# ob.showData()
# print(C4.__mro__)


# "Hybrid Inheritance 1"
#
# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#     def showData(self):
#         print("This is class C2")
#
# class C3(C1):
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#         super().__init__()
#
#     def showData(self):
#         print("This is class C3")
#
# class C4(C2, C3):
#     def __init__(self):
#         self.g = 7
#         self.h = 8
#         super().__init__()
#         C3.__init__(self)
#
#     def showData(self):
#         print("This is class C4")
#
#
# ob = C4()
# print(ob.a, ob.b, ob.c, ob.d, ob.e, ob.f, ob.g, ob.h)
# ob.showData()
# print(C4.__mro__)



"Hybrid Inheritance 2"

# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#     def showData(self):
#         print("This is class C2")
#
# class C3:
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#
#
#     def showData(self):
#         print("This is class C3")
#
# class C4(C2, C3):
#     def __init__(self):
#         self.g = 7
#         self.h = 8
#         super().__init__()
#         C3.__init__(self)
#
#     def showData(self):
#         print("This is class C4")
#
#
# ob = C4()
# print(ob.a, ob.b, ob.c, ob.d, ob.e, ob.f, ob.g, ob.h)
# ob.showData()
# print(C4.__mro__)

"""
Polymorphism: 

Polymorphism is another property of OOPS which is used when 2 or more methods with the same 
name occur in same or different classes

Polymorphism is of two types:

1. Compile Time Polymorphism: Since there is no compile time in python, therefore this 
does not exist in python

2. Run Time Polymorphism:
It is further of two types:

    a. Method Overloading: This occurs, when there are two or more methods with the same name
    in the same class.
    This does not exist in python.
    
    b. Method Overriding: This occurs when there are two method with the same name, one in 
    parent class and the other in child class
"""

# class C1:
#
#     def __init__(self):
#         self.a = 6
#         self.b = 8
#
#     def showData(self):
#         print(self.a, self.b)
#
#     def showData(self):
#         self.a +=3
#         self.b +=5
#         print(self.a, self.b)
#
# ob = C1()
# ob.showData()


# class C1:
#     def __init__(self):
#         self.a = 6
#         self.b = 8
#
#     def showData(self):
#         print(self.a, self.b)
#
# class C2(C1):
#
#     def showData(self):
#         self.a += 3
#         self.b += 5
#         print(self.a, self.b)
#
# ob = C2()
# ob.showData()

"""
How to create and access static variables and static methods
Static variables and static methods are also known as class variables and class methods
They are created and accessed with the class name only, even though they can be accessed 
with object names also

Static Variables:

Q. How are static variables created?
A. These variables are created inside the class just like normal variables, but outside
any methods.


Note: Static variables are shared between all the objects of a class
"""

# class C1:
#
#     x = 11
#
#     def __init__(self):
#         self.a = 5
#         self.b = 7
#
# ob = C1()
# print(ob.a, ob.b)
# print(C1.x)
# print(ob.x)



# class C1:
#     x = 0
#
#     def __init__(self):
#         self.a = 0
#
#     def incData(self):
#         self.a += 1
#         C1.x += 1
#         print(self.a, C1.x)
#
# ob = C1()
# ob.incData()
# ob.incData()
# ob.incData()




# 1 1
# 1 1
# 1 1
#
#
# 1 1
# 1 0
# 1 0
#
# 1 1
# 2 2
# 3 3
#
#
# 1 1
# 1 2
# 1 3
#
# Error

# class C1:
#     x = 0
#
#     def __init__(self):
#         self.a = 0
#
#     def incData(self):
#         self.a += 1
#         C1.x += 1
#         print(self.a, C1.x)
#
# ob1 = C1()
# ob1.incData()
# ob2 = C1()
# ob2.incData()
# ob3 = C1()
# ob3.incData()


"""
Static Methods:
These are the methods inside a class which are created and used without objects
They are preferably accessed with Class Name

a decorator can change the functionality of a function or a method
"""

# class C1:
#
#     @staticmethod
#     def staticMethod1():
#         print("This is staticMethod1")
#
#
# ob = C1()
# C1.staticMethod1()
# # ob.staticMethod1()



# d1 = {1: 11, 2: 22, 3: 33, 4: 44}
# l = [3, 4, 5, 6]
#
# # d2 = d1.fromkeys(l)
# # print(d2)
#
# d2 = dict.fromkeys(l)
# print(d2)






