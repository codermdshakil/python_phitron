
class Shop:
    
    cart = [] # Class Attributes
    
    def __init__(self, owner):
        self.owner = owner
        
    def add_to_cart(self, item):
        self.cart.append(item)


mehzabeen = Shop('Mehzbeen')
mehzabeen.add_to_cart('Shoes')
mehzabeen.add_to_cart('phone')
mehzabeen.add_to_cart('mekeup')

print(mehzabeen.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('Watch')
nisho.add_to_cart('Hat')
nisho.add_to_cart('Shart')



print(nisho.cart)
print(mehzabeen.cart)

# both items are stored in one cart because cart is class attributes for this reason it store all object values

  
    
    
    
    
    
    