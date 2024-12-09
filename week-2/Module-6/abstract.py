
# Import ABC - Abstract Base Class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod # using this @abstractmethod keyword Enforce to use eat method on every object 
    
    def eat(self):
        pass
    @abstractmethod 
    def move(self):
        pass
    
    
class Monkey(Animal):
    
    def __init__(self, name):
        self.name = name
        super().__init__()
    
    def eat(self):
        return f'Hi nana, I am eating banana'
    def move(self):
        return f'Hanging on the branch'
            
layka = Monkey('Layka')
print(layka.eat())



# Abstraction 
# Abstraction is th process of hiding the internal details of an application from the outer word. Abstraction is used to describe things in simple terms. It's used to create a boundary between the application and the client programs


