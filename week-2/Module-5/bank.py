


class Bank:
    
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
        
    def get_balance(self):
        return self.balance
     
     
    def deposite(self, amount):
        if amount>0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"You can't withdraw below {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(F"Bank fokir hoye jabe. You can't withdraw more then {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f"here is your money {amount}")
            print(f"Your balance after withdraw {self.balance}")
        
        
brac = Bank(10500)

# print(brac.balance)
# print(brac.get_balance())
# print(brac.deposite(50000))
# print(brac.get_balance())
# print(brac.withdraw(1000))

dbdl = Bank(5000)
dbdl.deposite(1000)
dbdl.deposite(2000)

print(dbdl.get_balance())

 


        
    