
# Encapsulation -- hide details
# Access Modifier - Public, Private, Protected

# implementaton details I don't show It keep in a class (capsule) that's why it's emcapsulation 

class Bank:
    
    def __init__(self, holder_name,address,inisial_deposit):
        
        self.holder_name = holder_name # Public Access Modifier
        # self.address = address
        self._branch = address # Protected Access Modifier
        self.__balance = inisial_deposit # Private Access Modifier
        
    def deposit(self, amount):
        self.__balance += amount
        
    def getBalance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return f"You cash out {amount} tk and  You Current Balance is : { self.__balance})"
        else:
            return f'You have no enough money to Withdraw'
    
        

rafsun = Bank('Chooto Bro','banani 11' ,10000)

# Private

# rafsun.initial_deposit = 0 
# print(rafsun.getBalance()) # 10000
# rafsun.deposit(40000)
# print(rafsun.getBalance())


# Public
# rafsun.holder_name = 'Boro vai'
# print(rafsun.holder_name) # Boro vai

# Protected

# print(rafsun.address)
# print(rafsun._branch)

# print(rafsun.withdraw(11000))

# Pongtami he he
# print(dir(rafsun))
# print(rafsun._Bank__balance) # 10,000
rafsun._Bank__balance = 500
print(rafsun._Bank__balance) # 500



