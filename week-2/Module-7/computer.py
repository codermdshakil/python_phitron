
class CPU:
    
    def __init__(self, core):
        self.core = core
        pass
    
class RAM:
    def __init__(self, size):
        self.size = size
        pass
    
class HardDrive:
    def __init__(self,capacity ):
        self.capacity = capacity
        pass
    

# Composition Maintain "Has a" relation with Objects
    
# Computer has a CPU
# Computer has a RAM
# Computer has a Capacity

class Computer:
    
    def __init__(self, core, size, capacity):
        self.core = CPU(core)
        self.size = RAM(size)
        self.capacity = HardDrive(capacity)
        pass