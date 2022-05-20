"""OOPS Contd"""

"""
Instance methods: These are the methods which are created inside a class using objects

Note: By default the methods that are created inside a class are instance mthods only
"""

# class C1:
#
#     def method1(self, b, c):           # a = obj, b = 1, c = 2
#         print(self, b, c)
#
# obj = C1()
# print(obj)
# obj.method1(1, 2)

"""
Since, in the first argument of instance methods, the object itself is saved, that is why
it is preferred to call the first argument of instance methods 'self'
"""

# l1 = [1, 2, 3, 4]
# l2 = [9, 8, 7, 6]
#
# list.append(l1, 5)
# print(l1)
# print(l2)
#
# l1.append(5)


"""
Back to instance variables:

Yesterday we had discussed that there are two ways to create an instance variable.
We also discussed the first way, that was creating instance variables outside the class

obj_name.var_name = value

Second way to create instance variables:
Creating instance variables inside the class

self.var_name = value

Note: instance variables are object specific
"""
# # BLL Starts Here
# class C1:                       # Line 1
#
#     def method1(self):          # Line 2, Line 6: self = ob
#         self.b = 5              # Line 7
#         print(self.a, self.b)   # Line 8
# # BLL Ends Here
#
# # PL Starts Here
# ob = C1()                       # Line 3
# ob.a = 10                       # Line 4
# ob.method1()                    # Line 5
# print(ob.a, ob.b)               # Line 9
# # PL Ends Here
"""
Here, data is being transferred between BLl and PL through objects
"""

# class C1:
#
#     def incData(self):
#         self.a+=5
#         self.b+=7
#
# ob1 = C1()
# ob2 = C1()
# ob1.a, ob1.b = 4, 7
# ob2.a, ob2.b = 4, 7
#
# ob1.incData()
# print(ob1.a, ob1.b, ob2.a, ob2.b)


"""
Option 1: 4, 7, 4, 7
Option 2: 9, 14, 4, 7
Option 3: 9, 14, 9, 14
Option 4: 9, 14, 4, 7, 4, 7
"""


class C1:
    def createVar(self):
        self.a = 11
        self.b = 12

ob1 = C1()
ob2 = C1()

ob1.createVar()
print(ob1.a, ob1.b, ob2.a, ob2.b)
























