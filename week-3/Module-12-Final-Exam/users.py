
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
    def add_employee(self,emp):
        employee = Employee(id=emp.id,name=emp.name,email=emp.email,address=emp.address,age=emp.age,destionation=emp.destination,salary=emp.salary)
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
    def add_customer(self,customer_object):
        customer = Customer(id=customer_object.id,name=customer_object.name,email=customer_object.email,address=customer_object.address)
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
    def add_item(self,item_object):
        item = Item(id=item_object.id,name=item_object.name,price=item_object.price,quantity=item_object.quantity)
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

# create restaurent
restaurent = Restaurent("Cholen Khai")
# Create Admin
admin1 = Users(1,"Admin","admin@gmai.com","Dhaka")

ad = Admin(admin1, restaurent)


# emp_id = int(input("Enter employee id : "))
# emp_name = input("Enter employee name : ")
# emp_email = input("Enter employee email : ")
# emp_address = input("Enter employee address : ")
# emp_age = input("Enter employee age : ")
# emp_destination = input("Enter employee destination : ")
# emp_salary = input("Enter employee Salary : ")

# # create a employee object
# emp1 = Employee(emp_id, emp_name, emp_email, emp_address, emp_age, emp_destination, emp_salary)

# # add employee object
# ad.add_employee(emp1)


# customer_id = int(input("Enter Customer id : "))
# customer_name = input("Enter Customer name : ")
# customer_email = input("Enter Customer email : ")
# customer_address = input("Enter Customer address : ")

# # # create a customer object
# customer1 = Customer(customer_id, customer_name, customer_email,customer_address)
# ad.add_customer(customer1)
# ad.view_customers()


item_id = int(input("Enter item id : "))
item_name = input("Enter item name : ")
item_price = int(input("Enter item price : "))
item_quantity = int(input("Enter item quantity : "))

# # # create a customer object
item1 = Item(item_id,item_name,item_price,item_quantity)
ad.add_item(item1)

item_id = int(input("Enter item id : "))
item_name = input("Enter item name : ")
item_price = int(input("Enter item price : "))
item_quantity = int(input("Enter item quantity : "))

# # # create a customer object
item2 = Item(item_id,item_name,item_price,item_quantity)
ad.add_item(item2)

customer1 = Customer(1,"Noyon","noyon@gmail.com","Ranigonj")
# customer2 = Customer(2,"Nadim","nadim@gmail.com","Folbaria")
customer1.menu()
customer1.add_order()
customer1.list_of_orders()





