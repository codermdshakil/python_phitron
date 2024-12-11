

def outer_function():
    print('Outer function')
    
    def inner_function():
        print("Inner Function")
                
         
    inner_function()
    return 200           

print(outer_function())

        