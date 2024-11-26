

def full_name(first, last):
    name = f"Full name is : {first} {last}"
    return name

## sent arguments order wise
# name = full_name('Shakil', 'Ahmed')

## sent arguments as what is wish
name = full_name(last="Ahmed", first= 'Shakil')
print(name)

# args  save without parameter value in a tuple
def sum(num1, num2, *numbers):
    result = num1 + num2
    print(numbers) # *numbers =  (30, 20) [take it like args] 
    return result

# r = sum(10, 20, 30, 20, 50, 80, 90, 120)
# print(r)



# arges example with string
def full_name2(first, last, *names):
    name = f"{first} {last}"
    print("Agrs string values : ", names)
    return name

# name1 = full_name2('Shakil', 'Ahmed', 'Noyon', 'Nadim')
# print(name1)


# Kagrs store value with key and value

def full_names(first, last, **addition):
    name = f"{first} {last}"
    print("Kargs value : ", addition)
    print("--------------------")
     
    ## print addition values
    for key, value in addition.items():
        print(key, value)
                
    return name

# name3 = full_names("Shakil", "Ahmed", n_name="Noyon", n1_name="Nadim")
# print(name3)


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")


"""
# Summary 

*args
- Purpose: Allows a function to accept any number of positional arguments.
- Behavior: It collects additional positional arguments into a tuple.


**kwargs
- Purpose: Allows a function to accept any number of keyword arguments.
- Behavior: It collects additional keyword arguments into a dictionary.


Key Rules:
*args must come before **kwargs in the parameter list.
Both *args and **kwargs are optional; you can use either, both, or neither based on the need.
This flexibility makes Python functions powerful for handling dynamic inputs!

"""



