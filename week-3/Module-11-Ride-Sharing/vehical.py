
from abc import ABC

class Vehical(ABC):
    
    speed ={
        'car':50,
        'bike':60,
        'cng':15
    }
    
    def __init__(self, vehical_type, lisense_plate, rate):
        self.vehical_type = vehical_type
        self.license_plate = lisense_plate
        self.rate = rate
        

# create vehicals
class Car(Vehical):
    def __init__(self, vehical_type, lisense_plate, rate):
        super().__init__(vehical_type, lisense_plate, rate)


class Bike(Vehical):
    
    def __init__(self, vehical_type, lisense_plate, rate):
        super().__init__(vehical_type, lisense_plate, rate)
    
 