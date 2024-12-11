
# poly --> Many (multiple)
# morph --> shape

class Animal:
    
    def __init__(self, name):
        self.name = name
        pass
    
    def make_sound(self):
            print("Animal sound")
        
class Cat(Animal):
    
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self):
        print("Meow meow")
        
    
class Dog(Animal):
    
    def __init__(self, name):
         super().__init__(name)
    
    def make_sound(self):
        print("Ghew ghew ")
        

class Goat(Animal):
    
    def __init__(self, name):
         super().__init__(name)
         
    def make_sound(self):
        print("Be be ")
         
    
don = Cat('Real Don')
don.make_sound()

laika = Dog('Laika')
laika.make_sound()

mess = Goat('L M')
mess.make_sound()


less = Goat('Gora gori')



animals = [don, laika, mess, less]

for animal in animals:
    animal.make_sound()
    


