
 

class Menu:
    
    def __init__(self):
        self.items = [] # items database
    
    # add items to menu
    def add_menu_item(self, item):
        self.items.append(item)
    
    # find item from item list
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    # remove item from item list
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
          self.items.remove(item)
          print(f"{item_name} Item Deleted!")
        else:
            print("Item not found!")
            
    # show all menu
    def show_menu(self):
        print("---- Show Menu Items ------")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

