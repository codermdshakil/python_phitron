
# Customer
# Employee
# Admin

from abc import ABC


class User(ABC):
    
    def __init__(self, name, email, phone, address):
        
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        
        
class Employee(User):
    
    def __init__(self, name, email,  phone, address, age, desgination, salary):
        self.age = age
        self.desgination = desgination
        self.salary = salary
        super().__init__(name, phone, email, address)
    
# emp = Employee("rahim", "rahim@gmail.com", 12312, "Dhaka", 20, "Chef", 12000)

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
            item.quantity = quantity
            self.cart.add_item(item)
            print("item added!!")
        else:
            print("Item not Found!")
        
    def view_cart(self):
        print("--- View Cart ------")
        print("Name\tPrice\tQuantity")
        
        for item, quantity in self.cart.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print("Total Price: ", {self.cart.total_price})

class Order:
    
    def __init__(self):
        self.items = {}
    
    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # jodi card a item thake tahole quantity increase
        else:
             self.items[item] = item.quantity  # jodi card a item na thake
        
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
     
    
    def clear(self):
        self.items = {}
         
    
class Admin(User):
    
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
   
    # from here we called restuarent function
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
        
    def view_employee(self, restuarent):
        restuarent.view_employee()

    def add_new_item(self, restuarent, item):
        restuarent.menu.add_menu_item(item)
        
    def remove_item(self, restuarent, item):
        restuarent.menu.remove_item(item)
    
    

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()
    
    def add_employee(self, employee):
        self.employees.append(employee) 
        print(f"{employee.name} is added!!")
        
    def view_employee(self):
        print("Employee List : ")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone,emp.address)
            
            
   
        

class Menu:
    
    def __init__(self):
        self.items = [] # items database
    
    # add items to menu
    def add_menu_item(self, item):
        self.items.append(item)
    
    # find item from item list
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    # remove item from item list
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
          self.items.remove(item)
          print(f"{item_name} Item Deleted!")
        else:
            print("Item not found!")
            
    # show all menu
    def show_menu(self):
        print("---- Show Menu Items ------")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

    
class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity



mamar_res = Restaurent('Pizzaburg')
mn = Menu()

# create item
item = FoodItem('Pizza', 12.45, 10)
item2 = FoodItem('Burger', 10, 30)

# admin add items
ad = Admin('Noyon', 'noyon@gmail.com', 12342, "Ranigonj")
ad.add_new_item(mamar_res, item)
ad.add_new_item(mamar_res, item2)



customer1 = Customer('Rahim', "rahim@gmail.com", 1234123, "Dhaka")
customer1.view_menu(mamar_res)




  
        
    
     
    

