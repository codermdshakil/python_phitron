

def outer_function():
    print('Outer function')
    
    def inner_function():
        print("Inner Function")
                
         
    inner_function()
    return 200           

# print(outer_function())


# Functon received as a parameter and print that function
def do_somthing(work):
    print("work started")
    # print(work)
    work() 
    print("work ended")

# do_somthing('Coding with python')

def coding():
    print("Coding coding and coding and logic is important")
    

# do_somthing(coding)

def sleeping():
    print("Sleeping and dreaming with python")
    
do_somthing(sleeping)

        