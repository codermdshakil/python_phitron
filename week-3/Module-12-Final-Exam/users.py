
from abc import ABC

class Users(ABC):
    
    def __init__(self,name,email,address):
        self.name = name
        self.email = email
        self.address = address
        


class Employee(Users):
    
    def __init__(self, name, email, address,age, destionation,salary):
        super().__init__(name, email, address)
        self.age = age
        self.destination = destionation
        self.salary = salary
        

# c
