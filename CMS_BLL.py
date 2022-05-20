# BLL Starts Here
import pymysql
class Customer:

    cus_list = []                           # cus_list = [1000, 2000, 3000, 4000]
    delete_cus = []

    def __init__(self):
        self.id = 0
        self.name = 0
        self.age = 0
        self.mob = 0

    def addCustomer(self):
        Customer.cus_list.append(self)

        con = pymysql.connect(host = 'localhost', user = 'root', password = 'root123')
        cur = con.cursor()

        cur.execute("create database IF NOT EXISTS customer")
        cur.execute("use customer")
        cur.execute("create table IF NOT EXISTS cusdata(id int, name varchar(30), age int, mob int)")
        cur.execute(f"insert into cusdata values({self.id}, '{self.name}', {self.age}, {self.mob})")

        con.commit()


    def searchCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                return e
        else:
            raise NotImplementedError("Customer Not Found")

    def updateCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                break
        else:
            raise NotImplementedError("Customer Not Found")

    def deleteCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                Customer.cus_list.remove(e)
                break
        else:
            raise NotImplementedError("Customer Not Found")



# BLL Ends Here