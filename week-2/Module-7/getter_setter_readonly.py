
# read ony --> you can not set the value. value can not be change
# getter --> get a value of property through a method. Most of the time, you will get the value of a private attribute
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property


class User:
    def __init__(self, name ,age, money):
        
        self._name = name
        self._age = age
        self.__money = money
        
        
    #  gettter without any setter is readonly attributes
    @property # @property is a decorator to make method to attributes
    def age(self):
        return self._age
    
    
    @property
    def salary(self):
        return self.__money
    
    
    # setter we can modify attributes
    @salary.setter
    def salary(self, value):
        
        if value < 0:
            return 'salary can not be negative'
        else:
            self.__money += value
            
        
samsu = User('Kopa', 21, 12000)
# print(samsu.__money)  
# print(samsu.age())
# print(samsu.age) # make it attributes from method

# print(samsu.salary())
# after using setter we can assign values
samsu.salary = 4000
print(samsu.salary)






