
class Person:
    
    def __init__(self, name ,age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print("Vat mangso  polaw korma")
        
    

class Criketer(Person):
    
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    
    # Override 
    def eat(self):
        print("Vegitables")
        
    
sakib = Criketer('sakib', 38, 68, 91, 'BD')
sakib.eat()

