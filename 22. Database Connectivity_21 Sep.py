"""Database Connectivity"""

"""
How to connect our program with a database for permanent storage of data

For this, we will be needing to install two things:

1. MySQL Database Server
2. pymysql library

Before studying databases, we should know about a few terms:

1. table: It is a collection og rows and columns and the data is saved in the cells of the 
table grid
2. database: It is a collection of tables in which information is stored
3. database server: It is a collection of databases



Database: It is a software, which is used to store information permanently and to process it

There are two types of databases in general:

1. Relational databases: These are the databases in which data is stored in the form of tables
in rows and columns format.
Examples:
a. MySQL Database
b. Oracle
c. MS SQL Server
d. MS Access
e. PostGre / PostGre S / PostGre SQL

Note: Relational databases are also known as SQL databases.

2. Non-relational databases: These are the databases in which data is not stored in tabular
format. Rather it stored with the help of some key like the primary key
For Example:
a. HBase
b. Mongo DB
etc

Note: Non relational databases are also known as non-SQL databases



MySQL Server

SQL: Structured Query Language: This is a language which is used to store and modify data 
stored in a database

We are going to look at CRUD Queries


To use the database from our python application, first of all, we will need to 
connect our program with the database.

For this, we will need to create a connection
Requirements:

1. Address : IP Address of the location where the database server is installed.
For local system, IP address is always: 127.0.0.1 or 'localhost'
(mandatory)

2. Authentication: user id, password. default user name: root, password: jo bhi set kia hai
(mandatory)

3. database name: not mandatory

Connection create ho gya

Ab mujhe ek cursor chahiye hoga
"""

# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123', database = 'python_class')
# cur = con.cursor()
#
# print(type(con))
# print(type(cur))
#
# con.close()


# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123', database = 'python_class')
# cur = con.cursor()
#
# q = "select * from student"
# cur.execute(q)
#
# data = cur.fetchall()
#
# for e in data:
#     print(e)
#
# con.close()


# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123')
# cur = con.cursor()
#
# cur.execute("use python_class")
# q = "select * from student"
# cur.execute(q)
#
# data = cur.fetchall()
# print(data)
#
# for e in data:
#     print(e)
#
# for roll, name, age, marks in data:
#     print(roll, name, age, marks)
#
# # cur.execute("insert into student values(1, 'abc', 11, 98)")
#
# con.commit()
# con.close()

# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123')
# cur = con.cursor()
#
# cur.execute("use python_class")
# q = "select * from student"
# cur.execute(q)
#
# data = cur.fetchall()
# f = open(r"C:\Users\Jai\PycharmProjects\18 Aug Batch\database data.csv", 'w')
# f.write("Roll Number,Name,Age,Marks\n")
# for roll, name, age, marks in data:
#     f.write(f"{roll},{name},{age},{marks}\n")
#
# cur.execute("insert into student values(1, 'abc', 11, 98)")
#
# con.commit()
# con.close()