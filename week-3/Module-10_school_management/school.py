
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
    
        