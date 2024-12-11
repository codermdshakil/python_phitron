
import math

def timer(func):
    
    def inner(*args, **kwargs):
        
        print("Time started")
        func(*args, **kwargs)
        print("Time ended")
        
    return inner

# decorator
@timer
def get_Factorial(n):
    print("Factorial starting")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    

# get_Factorial(5) # *args
get_Factorial(n=120) # **kwargs









        