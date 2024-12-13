
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
    
emp = Employee("rahim", "rahim@gmail.com", 12312, "Dhaka", 20, "Chef", 12000)

