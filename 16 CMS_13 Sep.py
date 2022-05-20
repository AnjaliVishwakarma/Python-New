"Customer Management System"

# BLL Starts Here

cusID = []
cusName = []
cusAge = []
cusMob = []

def addCustomer(id, name, age, mob):
    cusID.append(id)
    cusName.append(name)
    cusAge.append(age)
    cusMob.append(mob)


def searchCustomer(id):
    index_no = cusID.index(id)
    name = cusName[index_no]
    age = cusAge[index_no]
    mob = cusMob[index_no]

    return name, age, mob

def updateCustomer(id, name, age, mob):
    index_no = cusID.index(id)
    cusName[index_no] = name
    cusAge[index_no] = age
    cusMob[index_no] = mob

def deleteCustomer(id):
    index_no = cusID.index(id)
    cusID.pop(index_no)
    cusName.pop(index_no)
    cusAge.pop(index_no)
    cusMob.pop(index_no)


# BLL Ends Here

# PL Starts Here

while True:

    choice = input("""
    Press 1 to add new customer
    Press 2 to Search Customer
    Press 3 to Update Customer
    Press 4 to Delete Customer
    Press 5 to View All Customers
    Press 6 to exit
    
    Enter your choice: """)

    if choice == '1':
        newID = int(input("Enter Customer ID: "))
        newName = input("Enter Customer Name: ")
        newAge = int(input("Enter Customer Age: "))
        newMob = int(input("Enter Customer Mob: "))
        addCustomer(newID, newName, newAge, newMob)
        print()
        print("Customer Added Successfully!!")
        print()

    elif choice == '2':
        searchID = int(input("Enter Customer ID to search details: "))
        searchName, searchAge, searchMob = searchCustomer(searchID)
        print("The required customer details are:")
        print(f'ID: {searchID}, Name: {searchName}, Age: {searchAge}, Mob: {searchMob}')

    elif choice == '3':
        updateID = int(input("Enter Customer ID to update details: "))
        updateName = input("Enter Updated Name: ")
        updateAge = int(input("Enter Updated Age: "))
        updateMob = int(input("Enter Updated Mob: "))

        updateCustomer(updateID, updateName, updateAge, updateMob)
        print()
        print("Customer Updated Successfully")
        print()

    elif choice == '4':
        deleteID = int(input("Enter Customer ID to delete details: "))
        deleteCustomer(deleteID)
        print()
        print("Customer Deleted Successfully")
        print()

    elif choice == '5':
        print("The Customer details are:")
        print("ID\t\tName\t\tAge\t\tMob\n")

        for i in range(len(cusID)):
            print(f"{cusID[i]}\t\t{cusName[i]}\t\t{cusAge[i]}\t\t{cusMob[i]}\n")

    elif choice == '6':
        print("Thanks for using our CMS")
        break

    else:
        print("Incorrect Choice")





# PL Ends Here