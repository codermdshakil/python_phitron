
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


class SavingAccount(Account):
    
    def __init__(self, name, accNum, balance, password, accType, irate):
        self.irate = irate
        super().__init__(name, accNum, balance, password, "Savings")
    
    def showInfo(self):
        print(f"Account Name : {self.name}")
        print(f"Account Type  : {self.accType}")
        
        
class SpecialAccount(Account):
    
    def __init__(self, name, accNum, balance, password, accType, limit):
        self.limit = limit
        super().__init__(name, accNum, balance, password, "Special")
    
    def showInfo(self):
        print(f"Account Name : {self.name}")
        print(f"Account Type  : {self.accType}")
        
    def withdraw(self, amount):
        if amount > 0 and self.limit >= amount:
            self.balance  -= amount
            


myacc = SpecialAccount('shakil', 1231,500, 1234, 'Savings', 200)
print(myacc.name)
 

 




    