
# Ena Poribohon




class Company:
    
    def __init__(self, name, address):
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counters =[]
        self.manager = []
        self.supervisors = []
        self.fare = []
        
        
class Driver:
    
    def __init__(self,name, age ,license):
        self.name = name
        self.license = license
        self.age = age
        
        
    
class Counter:
    
    def __init__(self):
        pass
    def purchase_ticket(self, start, destionation):
        pass
    
class Passenger:
    
    pass

red_mia = Driver('Red Mia','123',32)


