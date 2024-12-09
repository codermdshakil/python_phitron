
class Family:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class School:
    def __init__(self, id, level):
        self.id = id
        self.level = level

class Sports:
    def __init__(self, game):
        self.game = game
        pass
        
class Student(Family, School, Sports):
    
    def __init__(self, name, age, id, level, game):
        Family.__init__(self,name,age)
        School.__init__(self, id, level)
        Sports.__init__(self, game)
        super().__init__(name, age)
        
        
        
# Multi Inheritence
# that take multiple level inheritence
# Student(Family, School, Sports) 
        
        