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
        self.bBooks = []
        self.rBooks = []
        
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
                return
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
                return
            else:
                 # create user using User Object
                user = User(id, name, password)
                self.users.append(user)
                print(f"{user.name} Added!")
    
    # Borrow a Book
    def borrowBook(self, user, token):
        for book in self.books:
            if book.id == token:
                if book in user.bBooks:
                    print("Alreay borrow this book!!")
                    return
                elif book.quantity < 1:
                     print("No copy Available!")
                     return
                else:
                    user.bBooks.append(book)
                    book.quantity -= 1
                    print("Borrow Successfully!")

    # retrun a Book
    def returnBook(self, user, token):
        for book in self.books:
            if book.id == token:
                if book in user.bBooks:
                     book.quantity += 1
                     user.rBooks.append(book)
                     user.bBooks.remove(book)
                     print("Return Successfully!")
                     return
                else:
                    print("Not found in Borrow List!")
                 
                 
        
        