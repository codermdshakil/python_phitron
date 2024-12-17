class Book:
    
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    
    def __init__(self, id,name, password):
        self.id = id 
        self.name = name
        self.password = password
        self.bbooks = []
        self.rbooks = []
        
        