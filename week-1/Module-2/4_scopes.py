
## Global variable
balance = 3000

def buy_things(item,price):
    
    ## local variable
    # you can access global variable without using the global keyword
    # dream_phone = "iPhone"
    
    global balance ## if you want to modify a global variable, you have to use the global keyword
    print("previous balance value ", balance)
    balance = balance- price
    print(f"Balance afer buying {item} ", balance)

buy_things("sunglasss", 1000)
print("Global Balance after buying things ", balance)

    