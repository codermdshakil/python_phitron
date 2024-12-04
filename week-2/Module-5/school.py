
class Student:
    
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    
    
    # class representation
    def __repr__(self) -> str:
        return f"Student with name :{self.name}, Class : {self.current_class}, Id : {self.id}"
    
    

alia = Student('Alia', 9, 1)
print(alia)
