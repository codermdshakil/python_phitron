class Book:
    
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    
    def __init__(self, id,name, password):
        self.id = id 
        self.name = name
        self.password = password
        self.bbooks = []
        self.rbooks = []
        
# create Library 
class Library:
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []
    
    # add book method
    def addBook(self, id, name, quantity):
        
        for book in self.books:
            if book.id == id:
                print(f"This  Book  {id} already Exist!!")
            else:
                 # create book using Book Object
                book = Book(id, name, quantity)
                self.books.append(book)
                print(f"{book.name} Added!")
            
    
    # add user method    
    def addUser(self, id, name,password):
        
         for user in self.users:
            if user.id == id:
                print(f"This User {id} already Exist!!")
            else:
                 # create user using User Object
                user = User(id, name, password)
                self.users.append(user)
                print(f"{user.name} Added!")
        
        