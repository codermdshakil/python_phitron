
from datetime import datetime
from vehical import Car, Bike

class RideShaing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
        
    
    def add_rider(self, rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)
        
        
    def __repr__(self):
        return f"Company name {self.company_name} with riders : {len(self.riders)} and Drivers : {len(self.drivers)}"
        


class Ride:
    def __init__(self, start_location, end_location, vehical):
        self.start_location = start_location
        self.end_location = end_location
        self.vehical = vehical
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
        
    
    def find_driver(self,ride_request, vehical_type):
        
        if len(self.available_drivers) > 0:
            print("Looking for drivers......")
            driver = self.available_drivers[0]
            
           
            
            if vehical_type == 'car':
                vehical = Car("Car", "ABC456", 30)
            elif vehical_type == 'bike':
                vehical = Bike("Motor Bike", '1234BH', 50)
                
            
             # make a ride usin rider current location to end location
            ride = Ride(ride_request.rider.current_location,ride_request.end_location,vehical)
            
            driver.accept_request(ride)
            return ride
            
        
        
