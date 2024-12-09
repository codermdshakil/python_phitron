
class Vehical:
    
    def __init__(self, name, price):
        
        self.name = name
        self.price = price
        pass
    
    def move(self):
        pass
    
    def __repr__(self):
        return f'{self.name}'
    

class Bus(Vehical):
    
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)
    
    def __repr__(self):
        return super().__repr__()
        
class Truck(Vehical):
    
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)
        
    def __repr__(self):
        return super().__repr__()
    

class PickUpBuss(Truck):
    
    # Multi level Inheritence
    # Vehical <-- Truck <--  PickUp it inherit like these way
      
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)
        
        
    def __repr__(self):
        return super().__repr__()
    
        

class ACBus(Bus):
    
    def __init__(self, name, price, seat, tempareture):
        self.tempareture = tempareture
        super().__init__(name, price, seat)
   
    # call to representation 
    def __repr__(self):
        return super().__repr__()
    

green_line = ACBus('Green', 120000000, 16, 22)
print(green_line.name)
print(green_line.price)
print(green_line.seat)

print()


