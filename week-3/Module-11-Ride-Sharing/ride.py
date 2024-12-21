
from datetime import datetime

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
        
    
    def det_driver(self, driver):
        self.driver = driver
        
        
    def start_ride(self):
        self.start_time = datetime.now()
        
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        
    def __repr__(self):
        return f"Ride Details. Started {self.start_location} to {self.end_location}"


# Dhaka - Sylhet
# Ride request a ki ki thake
# 1. Ke request korteche -- rider
# 2. Se kothay jabe -- end_location

class RideRequest():

    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location
        
class RideMatching:
    
    def __init__(self, drivers):
        self.available_drivers = drivers
        
    
    def find_driver(self,ride_request):
        
        if len(self.available_drivers) > 0:
            print("Looking for drivers......")
            driver = self.available_drivers[0]
            
            # make a ride usin rider current location to end location
            ride = Ride(ride_request.rider.current_location,ride_request.end_location)
            
            driver.accept_request(ride)
            return ride
            
        
        

