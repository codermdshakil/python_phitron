
# Customer
# Employee
# Admin

# import order Module 

from abc import ABC
from orders import Order
 


# Common user 
class User(ABC):
    
    def __init__(self, name, email, phone, address):
        
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        
        
# create customer
class Customer(User):
    
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()
        
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_card(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        
        if item:
            if quantity > item.quantity:
                print("Item Quantity Exceeded!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added!!")
            
        else:
            print("Item not Found!")
    
    def view_cart(self):
        print("--- View Cart ------")
        print("Name\tPrice\tQuantity")
        
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
            print("Total Price: ", round(self.cart.total_price))
        
    def pay_bill(self):
        print(f"Total {round(self.cart.total_price)} paid successfully!")
        self.cart.clear()
        



# Create Employee 
class Employee(User):
    
    def __init__(self, name, email,  phone, address, age, desgination, salary):
        self.age = age
        self.desgination = desgination
        self.salary = salary
        super().__init__(name, phone, email, address)
    
    
# Create Admin 
class Admin(User):
    
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
   
    # from here we called restuarent function
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
        
    def view_employee(self, restuarent):
        restuarent.view_employee()
        
    # def view_items(self, restuarent):
    #     restuarent.menu.()

    def add_new_item(self, restuarent, item):
        restuarent.menu.add_menu_item(item)
        
    def remove_item(self, restuarent, item):
        restuarent.menu.remove_item(item)
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
        
    
    







  
        
    
     
    

