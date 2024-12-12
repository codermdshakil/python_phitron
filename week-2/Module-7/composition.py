
# Composition main tain Has a relation with object
class Engine:
    
    def __init__(self):
        pass
    
    def start(self):
        return "Engine started"

class Driver:
    def __init__(self):
        pass


# Car "Has a" engine
# Car "Has a" driver
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()
        pass
    

 