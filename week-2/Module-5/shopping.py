
class Shopping:
    
    def __init__(self, name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self, item, price, quantity):
        product = {'item':item, 'price':price, 'quantity': quantity}
        self.cart.append(product)
        
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item) 
            total += item['price'] * item['quantity'] 
        print('Total Price', total)
        
        if amount < total:
            print(f"You need more money {total-amount} taka")
        else:
            extra = amount - total
            print(f"Here is your items and Extra Money { extra}")        
    
    def remove_from_cart(self, item_name):
         for i, item in enumerate(self.cart):
           if item['item'] == item_name:
            del self.cart[i]
            break
         
        
swapan = Shopping('Alan Shopon')
swapan.add_to_cart('Alu', 50, 5)
swapan.add_to_cart('dim', 12, 24)
swapan.add_to_cart('rice',50, 5)

# print(swapan.cart)
swapan.remove_from_cart('dim')
print(swapan.cart)


        
        
        
        