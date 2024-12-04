
class Student:
    
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    
    
    # class representation
    def __repr__(self) -> str:
        return f"Student with name :{self.name}, Class : {self.current_class}, Id : {self.id}"\
            
            
class Teacher:
    
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    
    
    # class representation
    def __repr__(self) -> str:
        return f"Teacher with name :{self.name}, Class : {self.subject}, Id : {self.id}"
    

class School:
    
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
        
    def enroll(self, name, fee):
        if fee > 6500:
            return "Not Enough fee"
        else:
            id = len(self.students) + 1
            student = Student(name,'C',id)
            self.students.append(student)
            return f"{name} is enrolled with id:{id}, extra money {fee - 6500}"
        
    
    def __repr__(self) -> str:
        print('Wecome to ', self.name)
        print(' ------------ Our Teachers ------------')  
        for teacher in self.teachers:
            print(teacher)
        
        print(' ------------ Our Students ------------')  
        
        for teacher in self.teachers:
            print(teacher)
        return 'All done for now'

# alia = Student('Alia', 9, 1)
# ranbeer = Teacher('Douran Beer', 'Algorithms', 101)

# print(alia)
# print(ranbeer)


phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwariya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)



