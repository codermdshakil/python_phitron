
class School:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # {'bangla': teacher_object}
        self.classrooms = {} # {'eight': classroom_object}
        
    
    # add classroom 
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    
    
    # add teacher
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    
    def student_addmission(self, student):
        pass
    
    
    @staticmethod
    
    def calculate_grade(self,marks):
        
        if marks >= 80 and marks <= 100:
            return 'A+'
        elif marks >= 70 and marks < 80:
            return 'A'
        elif marks >= 60 and marks < 70:
            return 'A-'
        elif marks >= 50 and marks < 60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return "Fail" 
        
        