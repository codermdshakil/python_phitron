
from abc import ABC, abstractmethod

class User(ABC):
    
    def __init__(self, name,email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError 

# create rider class

class Rider(User):
    
    def __init__(self, name, email, nid, current_location, inisial_amount):
        super().__init__(name, email, nid, inisial_amount)
        self.current_ride = None
        self.wallet = inisial_amount
        self.current_location = current_location
        
    def display_profile(self):
        print(F"Rider : {self.name} and email {self.email}")
        
    
    # add cash to wallet
    def load_cash(self, amount):
        
        if amount > 0:
            self.wallet += amount
        else:
            print("Amount less than 0")
    
    
    # update location
    
    def update_location(self, current_location):
        self.current_location =  current_location
        
    def request_ride(self, ride_sharing, destination):
        pass
    
    
    def show_current_ride(self):
        print(self.current_ride)
        
    
# create driver class
class Driver(User):
    
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0
        
        
    def display_profile(self):
        print(f"Driver Name : {self.name}")
        
    def accept_ride(self, ride):
        ride.set_driver(self) # Driver Object (self) mean Driver Object full
        
    
    
    
        
        
        