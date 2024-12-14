

from food_item import FoodItem
from menu import Menu
from users import User, Customer, Employee, Admin
from restaurent import Restaurent
from orders import Order


def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter phone number: ") 
    address = input("Enter your address : ")
    
    customer = Customer(name=name, email=email, phone=phone, address=address)
    
    
    mamar_res = Restaurent("Mamar Restaurent")
    
    while(True):
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")
        
        choise = int(input("Enter your choise: "))
        
        if choise == 1:
            customer.view_menu(mamar_res)
        elif choise == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter Item Quanity: "))
            customer.add_to_card(mamar_res,item_name, item_quantity)
        elif choise == 3:
            customer.view_cart()
        elif choise == 4:
            customer.pay_bill()
        elif choise == 5:
            break
        else:
            print("Invalid Input!!")
            
            
            
        

def admin_menu():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    phone = input("Enter phone number : ") 
    address = input("Enter your address : ")
    
    admin = Admin(name=name, email=email, phone=phone, address=address)
     
    
    mamar_res = Restaurent("Mamar Restaurent")
    
    while(True):
        print(f"Welcome {admin.name}")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete items")
        print("6. Exit")
        
        choise = int(input("Enter your choise : "))
        
        if choise == 1:
            new_item_name = input("Enter item Name : ")
            new_item_price = int(input("Enter item Price : "))
            new_item_quantity = int(input("Enter item Quantity : "))
            
            # create new item
            new_item = FoodItem(new_item_name, new_item_price, new_item_quantity)
            admin.add_new_item(mamar_res, new_item)
            

        elif choise == 2:
            new_emp_name = input("Enter employee Name : ")
            new_emp_email =  input("Enter employee Email : ") 
            new_emp_phone = int(input("Enter employee Phone: "))
            new_emp_address = input("Enter employee Address: ") 
            new_emp_age = int(input("Enter employee Age : "))
            new_emp_destination = input("Enter employee Destination : ")
            new_emp_salary = int(input("Enter employee salary: "))
            
            # create new employee
            new_employee = Employee(new_emp_name,new_emp_email, new_emp_phone, new_emp_address, new_emp_age,  new_emp_destination, new_emp_salary)
            
            # add new employee
            admin.add_employee(mamar_res,new_employee)
            
        elif choise == 3:
            admin.view_employee(mamar_res)
            
        elif choise == 4:
            admin.view_menu(mamar_res)
            
        elif choise == 5:
            item_name = input("Enter item Name for Delete: ")
            admin.remove_item(mamar_res, item_name)
            
            
        elif choise == 6:
            break
        else:
            print("Invalid Input!!")
            
while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    
    choise = int(input("Enter your choise number : "))
    
    if choise == 1:
        customer_menu()
    elif choise == 2:
        admin_menu()
    elif choise == 3:
        break
    else:
        print("Invalid Input!!")

        
    
    