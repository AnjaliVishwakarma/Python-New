"""GUI Programming"""

"""
In GUI Programming, we are going to create desktop based applications
using tkinter framework

What do we need when we create a desktop based application?
First of all to create a desktop based application, we need a window
"""

# # New program
# import tkinter
#
# root = tkinter.Tk()
# root.geometry("500x400+300+150")
#
# root.mainloop()

"""
There are many different types of widgets that are already available in the tkinter framework
Some of them are: Label Widget, Entry Widget, Button Widget, Radio Button Widget, Text Widget, 
Menubar etc...

Label Widget: This widget is used to display data on the GUI window, just like the print 
function is used to display data on the CUI console
"""

# # New Program
# from tkinter import *
# root = Tk()
# root.geometry("500x400+300+150")
#
# lbl = Label(root, text = "Welcome to python class",
#             font = ("Times New Roman", 24, 'bold', 'italic', 'underline'), bg = "#000000",
#             fg = "Orange")
#
#
# root.mainloop()

"""
While creating a widget, we have to provide a geometry to the widget, to tell it, where it will be 
applied on the window
This can be dne in three ways:

1. Using pack geometry: 
Syntax: 
widget_obj.pack(side)

side can be 'top', or 'bottom' or 'left', or 'right'

2. using place geometry: Using this geometry, you can place your widget anywhere on the window
Syntax:
widget_obj.place(x, y)

3. using grid geometry: The grid geometry divides the GUI window into imaginary rows and 
columns and will put the widgets in the resulting cells
Syntax:
widget_obj.grid(row, column)
"""

# # New Program
# from tkinter import *
# root = Tk()
# root.geometry("500x400+300+150")
#
# lbl = Label(root, text = "Welcome to python class",
#             font = ("Times New Roman", 24, 'bold', 'italic', 'underline'), bg = "#000000",
#             fg = "Orange")
# lbl.pack()
#
# root.mainloop()


# # New Program
# from tkinter import *
# root = Tk()
# root.geometry("500x400+300+150")
#
# lbl = Label(root, text = "Welcome to python class",
#             font = ("Times New Roman", 24, 'bold', 'italic', 'underline'), bg = "#000000",
#             fg = "Orange")
# lbl.place(x = 150, y = 60)
#
# root.mainloop()


# # New Program
# from tkinter import *
# root = Tk()
# root.geometry("500x400+300+150")
#
# lbl = Label(root, text = "Welcome to python class",
#             font = ("Times New Roman", 24, 'bold', 'italic', 'underline'), bg = "#000000",
#             fg = "Orange")
# lbl.grid(row = 0, column = 0)
#
# lbl1 = Label(root, text = "Hello",
#             font = ("Monotype Corsiva", 24), bg = "#000000", fg = "Orange")
# lbl1.grid(row = 1, column = 1)
#
# lbl2 = Label(root, text = "Welcome",
#             font = ("Times New Roman", 24), bg = "#000000", fg = "Orange")
# lbl2.grid(row = 2, column = 0)
#
# lbl3 = Label(root, text = "Welcome to CETPA",
#             font = ("Times New Roman", 24, 'bold', 'italic', 'underline'), bg = "#000000",
#             fg = "Orange")
# lbl3.grid(row = 15, column = 10)
#
# root.mainloop()


"""
Button Widget
"""

# # New Program
# from tkinter import *
#
# def btn_Click():
#     print("Button is clicked")
#
# root = Tk()
# root.geometry("500x400+300+150")
#
# btn = Button(root, text = "Click me", font = ("Monotype Corsiva", 24), command = btn_Click)
# btn.pack()
#
# root.mainloop()

"""
Handlers: Handlers are those functions which are executed when a particular event occurs

event: any action performed is an event
Events are of two types:
1. Mouse events

2. keyboard events
"""

"""
Entry Widget: It is used to take input data from the user in GUI
"""

# x = int()
# print(type(x))
# print(x)
#
# # New Program
# from tkinter import *
#
# def btn_Click():
#     id = varID.get()
#     name = varName.get()
#     age = varAge.get()
#     mob = varMob.get()
#     print(id, name, age, mob)
#     varID.set("")
#     varName.set("")
#     varAge.set("")
#     varMob.set("")
#
# root = Tk()
# root.geometry("700x700+300+150")
#
# lblID = Label(root, text = "Enter Customer ID: ", font = ("Times New Roman", 24))
# lblID.grid(row = 0, column = 0)
# varID = StringVar()
# entrID = Entry(root, font = ("Times New Roman", 24), textvariable = varID)
# entrID.grid(row = 0, column = 1)
#
# lblName = Label(root, text = "Enter Customer Name: ", font = ("Times New Roman", 24))
# lblName.grid(row = 1, column = 0)
# varName = StringVar()
# entrName = Entry(root, font = ("Times New Roman", 24), textvariable = varName)
# entrName.grid(row = 1, column = 1)
#
# lblAge = Label(root, text = "Enter Customer Age: ", font = ("Times New Roman", 24))
# lblAge.grid(row = 2, column = 0)
# varAge = StringVar()
# entrAge = Entry(root, font = ("Times New Roman", 24), textvariable = varAge)
# entrAge.grid(row = 2, column = 1)
#
# lblMob = Label(root, text = "Enter Customer Mob: ", font = ("Times New Roman", 24))
# lblMob.grid(row = 3, column = 0)
# varMob = StringVar()
# entrMob = Entry(root, font = ("Times New Roman", 24), textvariable = varMob)
# entrMob.grid(row = 3, column = 1)
#
# btn = Button(root, text = "Submit", font = ("Times New Roman", 24), command = btn_Click)
# btn.grid(row = 4, column = 1)
#
# root.mainloop()

"""
How to apply multiple handlers on a widget?
This is done with the help of bind() method
"""
# # New Program
# from tkinter import *
#
# def btn_Click(e):
#     btn['bg'] = "Orange"
#
# def btn_Click1(e):
#     btn.config(bg = "Red")
#
# def func1(e):
#     btn['bg'] = "Green"
#
# def func2(e):
#     btn['bg'] = "Blue"
#
# root = Tk()
# root.geometry("500x400+300+150")
#
# btn = Button(root, text = "Click me", font = ("Monotype Corsiva", 24))
# btn.pack()
# btn.bind("<Button 1>", btn_Click)
# btn.bind("<Button 3>", btn_Click1)
# btn.bind("<Enter>", func1)
# btn.bind("<Leave>", func2)
#
# root.mainloop()


"""
How to apply images on widgets?
We have to follow 2 different techniques for this, based on the type of image being used

1. For gif and png images
"""

# # New Program
# from tkinter import *
# root = Tk()
# root.geometry("500x400+300+150")
#
# image = PhotoImage(file = 'mario.png')
#
# btn = Button(root, image = image)
# btn.pack()
#
# root.mainloop()

"""
2. For all other type of images
"""
# from tkinter import *
# from PIL import Image, ImageTk
#
# root = Tk()
# image = Image.open('landscape.jpeg')
# photo = ImageTk.PhotoImage(image)
#
# lbl = Label(root, image = photo)
# lbl.pack()
#
# root.mainloop()

"""
How to apply a menu bar on a window 
"""

# # New Program
# from tkinter import *
# from tkinter import filedialog
# import tkinter.colorchooser as tkc
# def func1():
#     print("Save / Undo is clicked")
#
# def func2():
#     path = filedialog.askopenfilename()
#     print(path)
#     f = open(path, 'r')
#     data = f.read()
#     print(data)
#
# def func3():
#     exit()
#
# def func4():
#     print("Redo is clicked")
#
# def func5():
#     color = tkc.askcolor()
#     print(color)
#     btn['bg'] = color[1]
#
# root = Tk()
# root.geometry("500x400+300+150")
#
# menubar = Menu(root)
#
# filemenu = Menu(menubar)
# filemenu.add_cascade(label = "Save", command = func1)
# filemenu.add_cascade(label = "Open", command = func2)
# filemenu.add_separator()
# filemenu.add_cascade(label = "Exit", command = func3)
#
# menubar.add_cascade(label = "File", menu = filemenu)
#
# editmenu = Menu(menubar)
# editmenu.add_cascade(label = "Undo", command = func1)
# editmenu.add_cascade(label = "Redo", command = func4)
#
# menubar.add_cascade(label = "Edit", menu = editmenu)
#
# btn = Button(root, text = "Choose Color", font = ("Monotype Corsiva", 24), command = func5)
# btn.pack()
#
# root.config(menu = menubar)
# root.mainloop()
