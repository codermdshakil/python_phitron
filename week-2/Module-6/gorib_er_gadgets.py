

class laptop:
    
    def __init__(self, brand, price, color, memory):
        
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
        pass
    
    def run(self):
        return f"Runnint Laptop : {self.brand}"
    
    