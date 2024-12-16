
import random
from school import School
class Person:
    def __init__(self,name):
        self.name = name

class Teacher(Person):
    
    def __init__(self, name):
        super().__init__(name)
    
    # evaluate exam by teacher from number 1 to 100 
    def evaluate_exam(self):
        return  random.randint(1, 100)
    
    
class Student(Person):
    
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {} #{'english' : 78, 'ICT': 90}
        self.subject_grade = {} #{"eng" : 'A'}
        self.grade = None
        
        
    def final_grade(self):
        
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade) # 5.00
            sum += point
        
        gpa = sum / len(self.subject_grade) # 7 / 2 = 3.50
        self.grade = School.all_value_to_grade(gpa)
         
    
    # Getter VS Setter  
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
            
        
        avg = sum
    
