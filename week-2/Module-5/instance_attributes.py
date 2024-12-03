
class Shop:
    
    
    def __init__(self, owner):
        self.owner = owner
        self.cart = [] #instance attributes
        
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
