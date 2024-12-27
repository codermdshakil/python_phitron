
from abc import ABC
# create users class
class Users(ABC):
    
    def __init__(self,id,name,email,address):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        

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


# Create Admin
class Admin(Users):
    
    def __init__(self, id, name, email, address):
        super().__init__(id, name, email, address)
        self.employees = []
        self.customers = []
        self.items = []
        
    # create employee
    def add_employee(self,id,name,email,address,age,destionation,salary):
        employee = Employee(id,name,email,address,age,destionation,salary)
        self.employees.append(employee)
    
    # remove employee
    def remove_employee(self):
        emp_id = int(input("Enter id of employee: "))
        for emp in self.employees:
            if emp.id == emp_id:
                self.employees.remove(emp)
    
    # view employee
    def view_employees(self):
        print("\n")
        print("---------- List Of Employees ----------")
        print(f"ID\tName\tEmail\tAddress\tAge\tDestination\tSalary")
        for emp in self.employees:
            print(f"{emp.id}\t{emp.name}\t{emp.email}\t{emp.address}\t{emp.age}\t{emp.destination}\t{emp.salary}")
    
    # add customer
    def add_customer(self,id,name,email,address):
        customer = Customer(id,name,email,address)
        self.customers.append(customer)
    
    # remove customer
    def remove_customer(self):
        cus_id = int(input("Enter id of Customer: "))
        for customer in self.customers:
            if customer.id == cus_id:
                self.customers.remove(customer)
    
    # view customer
    def view_customers(self):
        print("\n")
        print("---------- List Of Customers ----------")
        print(f"ID\tName\tEmail\tAddress")
        for customer in self.customers:
            print(f"{customer.id}\t{customer.name}\t{customer.email}\t{customer.address}")
    
    
    # add item
    def add_item(self,id,name,price,quantity):
        item = Item(id,name,price,quantity)
        self.items.append(item)
    
    # remove item
    def remove_item(self):
        item_id = int(input("Enter id of Item : "))
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
    
    def update_item_price(self):
        item_id = int(input("Enter item id : "))
        value = int(input("Enter item Price : "))
        for item in self.items:
            if item.id == item_id:
                item.price = value
                
        
    # view item
    def view_items(self):
        print("\n")
        print("---------- List Of Items ----------")
        print(f"ID\tName\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.id}\t{item.name}\t{item.price}\t{item.price}")


ad = Admin(2,"Admin","a@gmail.com","Dhaka")
ad.add_employee(1,"Shakil","shakil@gmail.com","Ranigonj",25,"Teacher",15000)
ad.add_employee(2,"Noyon","noyon@gmail.com","Kaligonj",20,"Mentor",25000)
ad.add_customer(3,"Nadim","n@gmail.com","Kaligonj")
ad.add_customer(4,"Asraf","asraf@gmail.com","Gazipur")
ad.add_item(1,"Pizza",45.5,45)
ad.add_item(2,"Burger",15.5,50)
ad.add_item(3,"Pasta",25.5,60)
# ad.view_employees()
# ad.remove_employee()
# ad.view_employees()
# ad.view_customers()
# ad.remove_customer()
# ad.view_customers()
# ad.view_items()
# ad.remove_item()
ad.view_items()
ad.update_item_price()
ad.view_items()




