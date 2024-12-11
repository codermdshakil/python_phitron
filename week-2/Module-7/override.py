
class Person:
    
    def __init__(self, name ,age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print("Vat mangso  polaw korma")
        
    def exercise(self):
        raise NotImplementedError

class Criketer(Person):
    
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    
    # Override 
    def eat(self):
        print("Vegitables")
    
    def exercise(self):
        print("Do everyday exercise")
        
    
sakib = Criketer('sakib', 38, 68, 91, 'BD')
sakib.eat()
sakib.exercise()


