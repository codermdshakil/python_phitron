
from abc import ABC, abstractmethod

class Account(ABC):
    
    # class property
    accounts = []
    
    def __init__(self, name, accNum,balance, password, accType):
    # object property
        self.name = name
        self.accNum = accNum
        self.__balance = balance
        self.password = password
        self.accType = accType
        
        Account.accounts.append(self)
        
    def changeInfo(self,newName):
        self.name = newName
    
    # overloads the method changeInfo
    def changeInfo(self, newName, newPass):
        self.name = newName
        self.password = newPass
      
    def deposit(self, amount):
        if amount > 0:
            self.balance  += amount
    
    def withdraw(self, amount):
        if amount > 0 and self.balance > amount:
            self.balance  -= amount
            
    def getBalance(self):
        return self.__balance
    
    
    @abstractmethod
    def showInfo(self):
        pass


myacc = Account('shakil', 1231,500, 1234, 'Savings') 
# print(myacc.name)
# print(myacc.password)
# myacc.changeInfo('janina', 4321)
# print(myacc.name)
# print(myacc.password)
# myacc.deposit(1000)
# print(myacc.balance)
# print(myacc.getBalance())
# print(myacc.__balance)

# access pricate property value
# print(dir(myacc))
# print(myacc._Account__balance)



    
    
    
    
    
    
    
    
    
    
    
    
    