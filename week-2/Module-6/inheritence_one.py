

# 1. Inheritence 
#------------------------

# Based class, parent class, common attributes + Functionality class
# derived class, child class, uncommon attributes + functionality class 

# Benifits of Inheritence 
# 
# 1. it provides the reuseability if a cde
# 2. we don't have to write same code again and again
# 3. It also allows us to add more features to a class without modifing it



class Gadgets:

    def __init__(self, brand, price, color, origin):    
    
    # common attributes and common method are here
      
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
        
    def run(self):
        return f"Runnint Laptop : {self.brand}"
        

class laptop:
    
    def __init__(self, memory):
        
        self.memory = memory
        pass
    
    def coding(self):
        return f"Learning python and practicing"


class Phone:
    
    def __init__(self,dual_sim):
        
        self.dual_sim = dual_sim
    
    def call(self, number, sms):        
        return f"Sending sms to : {number} with {sms}"
    
    
    

class Camera:
    
    def __init__(self, pixel):
        self.pixel = pixel
    
    def change_lens(self):
        pass
    

        
    
    