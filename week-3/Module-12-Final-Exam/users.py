
from abc import ABC
# create users class
class Users(ABC):
    
    def __init__(self,id,name,email,address):
        self.id = id
        self.name = name
        self.email = email
        self.address = address

class Restaurent():
    
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.customers = []
        self.items = []
        
    def show_menu(self):
        print("\n")
        print("---------- List Of Items ----------")
        print(f"ID\tName\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.id}\t{item.name}\t{item.price}\t{item.quantity}")

# create Employee object
class Employee(Users):
    
    def __init__(self, id, name, email, address,age,destionation,salary):
        super().__init__(id, name, email, address)
        self.age = age
        self.destination = destionation
        self.salary = salary
        
        
# Create Item 
class Item():
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

# Create Customer
class Customer(Users):
    def __init__(self, id, name, email, address):
        super().__init__(id, name, email, address)
        self.wallet = 0
        self.orders = []
    
    def menu(self):
        restaurent.show_menu()
        
    def add_order(self):
        if self.wallet == 0:
            print(f"You Balance is {self.wallet}. Add some money!")
            self.add_money()
        else:
            item_id = int(input("Enter Item Id for order : "))
            for item in restaurent.items:
                    if item.id == item_id:
                        self.orders.append(item)
                        self.wallet -= item.price
                        item.quantity = item.quantity-1
                        print(f"{item.id} id item order Successfully!")
                        print(f"Now, Your Balance = {self.wallet}")
                            

    def list_of_orders(self):
        print("\n")
        print("---------- List Of Order Items ----------")
        print("Id\tName")
        for item in self.orders:
            print(f"{item.id}\t{item.name}")
    
    def add_money(self):
        amount = int(input("Enter Amount: "))
        self.wallet += amount
        print(f"{amount} added to your wallet!!")
    
    def check_balance(self):
        return self.wallet

# Create Admin
class Admin(Users):
    
    def __init__(self,object, restaurent):
        super().__init__(id=object.id, name=object.name, email=object.email, address=object.address)
        self.employees = restaurent.employees 
        self.customers = restaurent.customers
        self.items = restaurent.items
        
    # create employee
    def add_employee(self):
        emp_id = int(input("Enter employee id : "))
        emp_name = input("Enter employee name : ")
        emp_email = input("Enter employee email : ")
        emp_address = input("Enter employee address : ")
        emp_age = input("Enter employee age : ")
        emp_destination = input("Enter employee destination : ")
        emp_salary = input("Enter employee Salary : ")
        employee = Employee(id=emp_id,name=emp_name,email=emp_email,address=emp_address,age=emp_age,destionation=emp_destination,salary=emp_salary)
        
        self.employees.append(employee)
        print(f"Employee {employee.name} id Added Successfully!!")
    
    # remove employee
    def remove_employee(self):
        emp_id = int(input("Enter id of employee: "))
        for emp in self.employees:
            if emp.id == emp_id:
                self.employees.remove(emp)
                print(f"This {emp.name} Removed!!")
    
    # view employee
    def view_employees(self):
        print("\n")
        print("---------- List Of Employees ----------")
        print(f"ID\tName\tEmail\tAddress\tAge\tDestination\tSalary")
        for emp in self.employees:
            print(f"{emp.id}\t{emp.name}\t{emp.email}\t{emp.address}\t{emp.age}\t{emp.destination}\t{emp.salary}")
    
    # add customer
    def add_customer(self):
        customer_id = int(input("Enter Customer id : "))
        customer_name = input("Enter Customer name : ")
        customer_email = input("Enter Customer email : ")
        customer_address = input("Enter Customer address : ")
        customer = Customer(id=customer_id,name=customer_name,email=customer_email,address=customer_address)
        self.customers.append(customer)
        print(f"Customer {customer.name} Added Successfully!!")
    
    # remove customer
    def remove_customer(self):
        cus_id = int(input("Enter id of Customer: "))
        for customer in self.customers:
            if customer.id == cus_id:
                self.customers.remove(customer)
                print(f"Customer {customer.name} Removed Successfully!!")
    
    # view customer
    def view_customers(self):
        print("\n")
        print("---------- List Of Customers ----------")
        print(f"ID\tName\tEmail\tAddress")
        for customer in self.customers:
            print(f"{customer.id}\t{customer.name}\t{customer.email}\t{customer.address}")
    
    
    # add item
    def add_item(self):
        item_id = int(input("Enter item id : "))
        item_name = input("Enter item name : ")
        item_price = int(input("Enter item price : "))
        item_quantity = int(input("Enter item quantity : "))
        item = Item(id=item_id,name=item_name,price=item_price,quantity=item_quantity)
        self.items.append(item)
        print(f"{item.name} Added Successfully!!")
    
    # remove item
    def remove_item(self):
        item_id = int(input("Enter id of Item : "))
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                print(f"{item.name} Removed Successfully!!")
    
    def update_item_price(self):
        item_id = int(input("Enter item id : "))
        value = int(input("Enter item Price : "))
        for item in self.items:
            if item.id == item_id:
                item.price = value
                print(f"Updated {item.name} with price {item.price} Successfully!!")
                
        
    # view item
    def view_menu(self):
        print("\n")
        print("---------- List Of Items ----------")
        print(f"ID\tName\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.id}\t{item.name}\t{item.price}\t{item.quantity}")
            

while(True):
    
    restaurent = Restaurent("Cholo Kisu Khai")
    
    # create admin
    ad = Users(1,"Admin","admin@gmail.com","Dhaka")
    ad = Admin(ad,restaurent)
    
    print("Restaurent Management System!")
    print("1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")
    
    
    option = int(input("Enter your Option: "))
    
    if option == 1:
        ad_name = input("Enter Admin Name: ")
        if ad.name == ad_name:
            print('\n')
            print(f"Welcome {ad_name}")
            print("------ Admin Menu --------")
            print("1. Create Customer Account")
            print("2. Remove Customer Account")
            print("3. View All Customers")
            print("4. Manage Restaurent Menu")
            print("5. Exit")
        
            op = int(input("Enter Option: "))
            
            if op == 1:
                ad.add_customer()
            elif op == 2:
                ad.remove_customer()
            elif op==3:
                ad.view_customers()
            elif op == 4:
                pass
            elif op == 5:
                break
            else:
                print("Invalid Option!!")
            

