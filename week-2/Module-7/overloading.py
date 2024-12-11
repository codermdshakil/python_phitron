
class Person:
    
    def __init__(self, name ,age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print("Vat mangso  polaw korma")
        
    def exercise(self):
        raise NotImplementedError

class Criketer(Person):
    
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    
    # Override 
    
    def eat(self):
        print("Vegitables")
    
    def exercise(self):
        print("Do everyday exercise")
        
        
        
        
    # Overload
    
    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age
    
    
    # * sign operator overload
    def __mul__(self, other):
        return self.age * other.age
    
    
    # Len overload
    def __len__(self):
        return self.height
    
    
    # > sign operator overload
    def __gt__(self, other):
        return self.age > other.age
 
        
        
    
sakib = Criketer('sakib', 38, 68, 91, 'BD')
mosfiq = Criketer('mosfiq', 36, 65, 78, 'BD')
# sakib.eat()
# sakib.exercise()



# overLoading

print(45+73)
print('sakib' + 'rakib')
print([12,3,54,14] + [10, 11,56])

# We can't +  sakib and mosfiq because they are class to that we should use overloading/magic method or dunder methods
print(sakib + mosfiq)  
print(sakib * mosfiq)  
print(len(sakib))
print(sakib > mosfiq)  




