# PL

# New Program
from CMS_BLL import *
from tkinter import *
from tkinter import messagebox

def btnAdd_Click():
    try:
        cus = Customer()
        cus.id = varID.get()
        cus.name = varName.get()
        cus.age = varAge.get()
        cus.mob = varMob.get()
        cus.addCustomer()
        messagebox.showinfo("CMS", "Customer Added Successfully")
        varID.set("")
        varName.set("")
        varAge.set("")
        varMob.set("")

    except Exception as err:
        messagebox.showinfo("CMS", err)

def btnSearch_Click():
    try:
        cus = Customer()
        cus.id = varID.get()
        cus1 = cus.searchCustomer()

        search = Tk()
        lblHeadID = Label(search, text = "ID", font = ("Times New Roman", 24), width = 15, bg = 'Orange')
        lblHeadID.grid(row = 0, column = 0)

        lblHeadName = Label(search, text="Name", font=("Times New Roman", 24), width=15, bg='Orange')
        lblHeadName.grid(row=0, column=1)

        lblHeadAge = Label(search, text="Age", font=("Times New Roman", 24), width=15, bg='Orange')
        lblHeadAge.grid(row=0, column=2)

        lblHeadMob = Label(search, text="Mob", font=("Times New Roman", 24), width=15, bg='Orange')
        lblHeadMob.grid(row=0, column=3)

        lblInfoID = Label(search, text=f"{cus1.id}", font=("Times New Roman", 24), width=15, bg='Yellow')
        lblInfoID.grid(row=1, column=0)

        lblInfoName = Label(search, text=f"{cus1.name}", font=("Times New Roman", 24), width=15, bg='Yellow')
        lblInfoName.grid(row=1, column=1)

        lblInfoAge = Label(search, text=f"{cus1.age}", font=("Times New Roman", 24), width=15, bg='Yellow')
        lblInfoAge.grid(row=1, column=2)

        lblInfoMob = Label(search, text=f"{cus1.mob}", font=("Times New Roman", 24), width=15, bg='Yellow')
        lblInfoMob.grid(row=1, column=3)

    except Exception as err:
        messagebox.showinfo("CMS", err)


def btnUpdate_Click():
    try:
        cus = Customer()
        cus.id = varID.get()
        cus.name = varName.get()
        cus.age = varAge.get()
        cus.mob = varMob.get()
        cus.updateCustomer()

        messagebox.showinfo("CMS", "Customer Updated Successfully")
        varID.set("")
        varName.set("")
        varAge.set("")
        varMob.set("")

    except Exception as err:
        messagebox.showinfo("CMS", err)
        newCus = messagebox.askyesno("CMS", "Do you want to add this customer?")
        if newCus == True:
            btnAdd_Click()

def btnDelete_Click():
    try:
        cus = Customer()
        cus.id = varID.get()

        delCus = messagebox.askyesno("CMS", "Are you sure you want to delete Customer?")

        if delCus == True:
            cus.deleteCustomer()
            messagebox.showinfo("CMS", "Customer Deleted Successfully")
            varID.set("")

    except Exception as err:
        messagebox.showinfo("CMS", err)


def btnViewAll_Click():
    ViewAll = Tk()
    lblHeadID = Label(ViewAll, text="ID", font=("Times New Roman", 24), width=15, bg='Orange')
    lblHeadID.grid(row=0, column=0)

    lblHeadName = Label(ViewAll, text="Name", font=("Times New Roman", 24), width=15, bg='Orange')
    lblHeadName.grid(row=0, column=1)

    lblHeadAge = Label(ViewAll, text="Age", font=("Times New Roman", 24), width=15, bg='Orange')
    lblHeadAge.grid(row=0, column=2)

    lblHeadMob = Label(ViewAll, text="Mob", font=("Times New Roman", 24), width=15, bg='Orange')
    lblHeadMob.grid(row=0, column=3)

    i = 1
    for e in Customer.cus_list:
        lblInfoID = Label(ViewAll, text=f"{e.id}", font=("Times New Roman", 24), width=15, bg='Yellow')
        lblInfoID.grid(row=i, column=0)

        lblInfoName = Label(ViewAll, text=f"{e.name}", font=("Times New Roman", 24), width=15, bg='Yellow')
        lblInfoName.grid(row=i, column=1)

        lblInfoAge = Label(ViewAll, text=f"{e.age}", font=("Times New Roman", 24), width=15, bg='Yellow')
        lblInfoAge.grid(row=i, column=2)

        lblInfoMob = Label(ViewAll, text=f"{e.mob}", font=("Times New Roman", 24), width=15, bg='Yellow')
        lblInfoMob.grid(row=i, column=3)

        i+=1

def btnLoadfromDB_Click():
    con = pymysql.connect(host='localhost', user='root', password='root123')
    cur = con.cursor()
    cur.execute("use customer")
    cur.execute("select * from cusdata")
    data = cur.fetchall()

    for id, name, age, mob in data:
        cus = Customer()
        cus.id = id
        cus.name = name
        cus.age = age
        cus.mob = mob
        Customer.cus_list.append(cus)

    messagebox.showinfo("CMS", "Data Loaded from database")


def btnExit_Click():
    exit()

root = Tk()
root.geometry("900x500+300+150")

lblID = Label(root, text = "Enter Customer ID: ", font = ("Times New Roman", 24))
lblID.grid(row = 0, column = 0)
varID = StringVar()
entrID = Entry(root, font = ("Times New Roman", 24), textvariable = varID)
entrID.grid(row = 0, column = 1)

lblName = Label(root, text = "Enter Customer Name: ", font = ("Times New Roman", 24))
lblName.grid(row = 1, column = 0)
varName = StringVar()
entrName = Entry(root, font = ("Times New Roman", 24), textvariable = varName)
entrName.grid(row = 1, column = 1)

lblAge = Label(root, text = "Enter Customer Age: ", font = ("Times New Roman", 24))
lblAge.grid(row = 2, column = 0)
varAge = StringVar()
entrAge = Entry(root, font = ("Times New Roman", 24), textvariable = varAge)
entrAge.grid(row = 2, column = 1)

lblMob = Label(root, text = "Enter Customer Mob: ", font = ("Times New Roman", 24))
lblMob.grid(row = 3, column = 0)
varMob = StringVar()
entrMob = Entry(root, font = ("Times New Roman", 24), textvariable = varMob)
entrMob.grid(row = 3, column = 1)

btnAdd = Button(root, text = "Add Customer", font = ("Times New Roman", 24), command = btnAdd_Click)
btnAdd.grid(row = 4, column = 0)

btnSearch = Button(root, text = "Search Customer", font = ("Times New Roman", 24), command = btnSearch_Click)
btnSearch.grid(row = 4, column = 1)

btnUpdate = Button(root, text = "Update Customer", font = ("Times New Roman", 24), command = btnUpdate_Click)
btnUpdate.grid(row = 4, column = 2)

btnDelete = Button(root, text = "Delete Customer", font = ("Times New Roman", 24), command = btnDelete_Click)
btnDelete.grid(row = 5, column = 0)

btnViewAll = Button(root, text = "View All Customer", font = ("Times New Roman", 24), command = btnViewAll_Click)
btnViewAll.grid(row = 5, column = 1)

btnExit = Button(root, text = "Exit", font = ("Times New Roman", 24), command = btnExit_Click)
btnExit.grid(row = 5, column = 2)

btnLoadfromDB = Button(root, text = "Load from database", font = ("Times New Roman", 24), command = btnLoadfromDB_Click)
btnLoadfromDB.grid(row = 6, column = 1)

root.mainloop()

