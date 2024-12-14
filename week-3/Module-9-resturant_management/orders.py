

 


class Order:
    
    def __init__(self):
        self.items = {}
    
    # add item
    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # jodi card a item thake tahole quantity increase
        else:
             self.items[item] = item.quantity  # jodi card a item na thake
    
    # remove item
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
    
    @property
    # total price
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
     

    def clear(self):
        self.items = {}
         
        