class Book:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    
    def __init__(self, id, name, password):
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
      
                 # create book using Book Object
        book = Book(id, name, quantity)
        self.books.append(book)
        print(f"{book.name} Added!")
        return book
            
    
    # add user method    
    def addUser(self, id, name,password):
        
        for user in self.users:
            if user.id == id:
                print(f"User id {id} already exits!")
                return
            
        user = User(id, name, password)
        self.users.append(user)
        print(f"{user.name} Added!")
        return user
                
                

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
                 
                 
pl = Library("Phitron Library")
admin = pl.addUser(1, "Admin", "1234")
shakil = pl.addUser(2, "Shakil", "1234")

# atomicHabit = pl.addBook(1, "Atomic Habit",10)

currentUser = admin

print(currentUser.name)



 
while True:
    
    if currentUser == None:
        
        print("\n No user Logged In! \n")
        
        option = input("Login\Register(L OR R) : ")
        
        if option == "L":
            
            id = int(input("Enter user Id : "))
            password = input("Enter user password : ")
            
            match = False
            
            for user in pl.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    match = True
                    break
                
            if match == False:
                print("\nNo user Found!")
                
        
        elif option == "R":
            
              # register
              id = int(input("Enter user Id : "))
              name = input("Enter user name : ")
              password = input("Enter user password : ")
              user = pl.addUser(id, name, password)
              currentUser = user
              break
        
    elif currentUser.name == "Admin":
        
        print(f"\nWelcome back {currentUser.name}!")
        
        if currentUser.name == "Admin":
            print("Options : ")
            print("1. Add Book : ")
            print("2. Add User : ")
            print("3. Show Books : ")
            print("4. Show Users : ")
            print("5. Logout : ")
            
        ch = int(input("\nEnter Options : "))
        
        if ch == 1:
            id = int(input("Enter Book Id: "))
            name = input("Enter Book name : ")
            quan = input("Enter Book quantity : ")
            pl.addBook(id,name,quan)
        
        elif ch == 2:
            id = int(input("Enter user Id: "))
            name = input("Enter user name : ")
            password = input("Enter user password : ")
            pl.addUser(id,name, password)
            
        elif ch == 3:
            for book in pl.books:
                print(book.name)
        elif ch == 4:
            for user in pl.users:
                print(user.name)
        elif ch == 5:
            currentUser = None
        else:
            print("Invalid Index!!") 
            
            
                
                
              

