
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
        self.employees = [] # eta hocche amader database employee store korar jonno
        
    
    def add_employee(self, name, email,phone, address, age, designation, salary):
        
        # employee ekta object toiri hoye jabe 
        employee = Employee(name, email, phone, address, age, designation, salary)
        self.employees.append(employee) # employee object take employees a store kora
        print(f"{employee.name} is added!!")
        
    def view_employee(self):
        print("Employee List : ")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone,emp.address)
    

ad = Admin('Karim', 'karim@gamil.com', 123123, "Dhaka")
ad.add_employee("Shakil", "shakil@gmail.com", 123124, "Kapasia", 20, 'Teacher', 16000)
ad.view_employee()

        
    
     
    

