

class Shopping:
    cart = [] # class or static operators
    origin = 'China'
    
    def __init__(self, name, location):
        
        self.name = name  # Instance attribute
        self.location = location 
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying: {item} for price {price} and remaining: {remaining}')
        
    @staticmethod
     
    # we can use without sending self argument  because we use @staticmethod
    def multiply(a, b):
        print(a * b)

        
    @classmethod
    def hudai_dekhi(self, item):
        self.item = item
        print(self.name)
        print("Hudai dekhi kintu kinmu na just ac er hawa khaite aschi")

basundara = Shopping('basun en data', 'not popular location')
# basundara.purchase('Lungi', 500, 1000)
 
# basundara.hudai_dekhi("Pen")
# basundara.multiply(5,9)

# class method

# we can't access direactly it because if use @classmethod we can access it without creating object 
# Shopping.multiply(10, 20)
# Shopping.hudai_dekhi("Pent")

 # static method
Shopping.multiply(5, 10) # static method |  we can use without sending self argument 



