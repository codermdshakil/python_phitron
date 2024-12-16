
import random

class Person:
    def __init__(self,name):
        self.name = name

class Teacher(Person):
    
    def __init__(self, name):
        super().__init__(name)
    
    # evaluate exam by teacher from number 1 to 100 
    def evaluate_exam(self):
        return  random.randint(1, 100)
    
    
    
    
