

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
    print(f"{customer.name}, {customer.email}, {customer.phone}, {customer.address}")
    
    
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
            
            
            
        
