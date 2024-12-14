
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


        
class Admin(User):
    
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
   
    # from here we called restuarent function
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
        
    def view_employee(self, restuarent):
        restuarent.view_employee()

        
    
    

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
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
        print("---- Show Menu ------")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

                
    

# ad = Admin('Karim', 'karim@gamil.com', 123123, "Dhaka")
# ad.add_employee("Shakil", "shakil@gmail.com", 123124, "Kapasia", 20, 'Teacher', 16000)
# ad.view_employee()

  
        
    
     
    

