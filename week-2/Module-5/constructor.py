
class Phone:
    
    # constructor of python
    # using constructor we can make multiple object using multiple  values
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand 
        self.price = price
        
        
shakil_phone = Phone('Shakil Ahmed', 'Samsung', 20000)
noyon_phone = Phone('Noyon Rahman', 'POCO', 16000)
nadim_phone = Phone('Nadim Hassan', 'Redmi', 7000)

print(shakil_phone.owner, shakil_phone.brand, shakil_phone.price)
print(noyon_phone.owner, noyon_phone.brand, noyon_phone.price)
print(nadim_phone.owner,nadim_phone.brand, nadim_phone.price)


