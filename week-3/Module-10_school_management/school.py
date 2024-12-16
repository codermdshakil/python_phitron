
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
    
    
    # calculate marks wise grade
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
        
    
    # calculate grade to value
    @staticmethod
    def grade_to_value(self, grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00 
        }
        return grade_map[grade]
    
     # calculate overall marks to grade    
    @staticmethod
    def all_value_to_grade(self,value):
        
        if value >=  4.5 and value <= 5.00:
            return 'A+'
        elif value >= 3.5 and value < 4.5:
            return 'A'
        elif value >= 3.0 and value < 3.5:
            return 'A-'
        elif value >= 2.5 and value < 3.0:
            return 'B'
        elif value >= 2.0 and value < 2.5:
            return 'C'
        elif value >= 1.0 and value < 2.0:
            return 'D'
        else:
            return "Fail" 
        
    def __repr__(self):
        # All classrooms
        # All students
        # All Subjects
        # All Teachers
        # All Student Result
        pass
    