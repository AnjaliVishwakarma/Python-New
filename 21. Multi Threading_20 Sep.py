"""Multi Threading in python"""

"""
Q. Does the CPU execute one process at a time or multiple processes at
the same time?
A. It executes one process at a time.

Q. What is the main purpose of an OS?
A. The OS controls the switching of programs that means, it allocates the CPU to different
processes for short intervals of time
It helps us in making multitasking systems


Multitasking systems are of two types:
1. Multi processing systems: Multi processing is used in big stand alone applications where the
resources of one application cannot be used by another application

2. Multi threading systems: This is used in small applications where the resources of 
one program can be used by another program
"""

# # New Program
# def func1():
#     for i in range(100):
#         print("This is func1", i)
#
# def func2():
#     for i in range(100):
#         print("This is func2", i)
#
# func1()
# func2()

# # New Program
# import threading
# def func1():
#     for i in range(100):
#         print(threading.current_thread().getName(), i)
#
# def func2():
#     for i in range(100):
#         print(threading.current_thread().getName(), i)
#
# th1 = threading.Thread(target = func1)
# th2 = threading.Thread(target = func2)
#
# th1.setName("Thread 1")
# th2.setName("Thread 2")
#
# th1.start()
# th2.start()
#
# for i in range(30):
#     print(threading.current_thread().getName(), i)

"""
Advanced multithreading --> Shared variables
"""

# # New Program
# import threading
# def func1():
#     global x
#     for i in range(10):
#         x+=1
#
# def func2():
#     global y
#     for i in range(10):
#         y+=1
#
# x, y = 0, 0
# th1 = threading.Thread(target  = func1)
# th2 = threading.Thread(target  = func2)
#
# th1.start()
# th2.start()
#
# print(x, y)

"""
Cache: The data which has to be accessed frequently is saved in the cache memory
RAM
ROM


CPU --> Cache       : Fastest
CPU --> RAM         : Slower
CPU --> ROM         : More slow
CPU --> Hardware    : Slowest



"""

# # New Program
# import threading
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
#
# x, y = 0, 0
# th1 = threading.Thread(target  = func1)
# th2 = threading.Thread(target  = func2)
#
# th1.start()
# th2.start()
#
# # print(th1.is_alive())
# # print(th2.is_alive())
#
# while th1.is_alive() or th2.is_alive(): pass
#
# print(x, y)


# # New Program
# import threading
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
#
# x, y = 0, 0
# th1 = threading.Thread(target  = func1)
# th2 = threading.Thread(target  = func2)
#
# th1.start()
# th2.start()
#
# # print(th1.is_alive())
# # print(th2.is_alive())
#
# # while th1.is_alive() or th2.is_alive(): pass
#
# th1.join()
# th2.join()
#
#
# print(x, y)


# # New Program
# import threading
# def func1():
#     global x
#     for i in range(100):
#         print(threading.current_thread().getName(), i)
#
# def func2():
#     global y
#     for i in range(100):
#         print(threading.current_thread().getName(), i)
#
# x, y = 0, 0
# th1 = threading.Thread(target  = func1)
# th2 = threading.Thread(target  = func2)
#
# th1.setName("Thread 1")
# th2.setName("Thread 2")
# th1.setDaemon(True)
# th2.setDaemon(True)
#
# th1.start()
# th2.start()
#
# for i in range(20):
#     print(threading.current_thread().getName(), i)
#
# print(x, y)


# # New Program
# import threading
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# x = 0
# th1 = threading.Thread(target  = func1)
# th2 = threading.Thread(target  = func1)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
# print(x)


"""
Race condition:

The solution to race condition is that we have to make an object of the Lock class and 
hold the time critical code

"""
# New Program
import threading
lock = threading.Lock()

def func1():
    global x
    for i in range(100000):
        lock.acquire()
        x+=1
        lock.release()

x = 0
th1 = threading.Thread(target  = func1)
th2 = threading.Thread(target  = func1)

th1.start()
th2.start()

th1.join()
th2.join()
print(x)


