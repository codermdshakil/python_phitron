

class Classroom:
    
    def __init__(self, name):
        self.name = name
        self.students = [] # list of students objects
        self.subjects = [] # list of subjects objects
        
        
    # add student
    def add_student(self, student): # rahim, 8
        roll_No = f"{self.name} - {len(self.students)+1}"
        student.id = roll_No
        self.students.append(student)
        
    def add_subject(self, subject):
        self.subjects.append(subject)
        
    def take_semester_final_exam(self):
        
        for subject in self.subjects:
            subject.exam(self.students)
            
        for student in self.students:
            student.all_value_to_grade(student)
        
        
        