

from food_item import FoodItem
from menu import Menu
from users import User, Customer, Employee, Admin
from restaurent import Restaurent
from orders import Order

    
class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


